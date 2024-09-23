import asyncio
import aiohttp
import random
import json
import sys
from colorama import *
from src.utils import log_line,pth, mrh, hju, bru, kng, _banner, _clear

init(autoreset=True)

class DiceBettingBot:
    def __init__(self, config_file, tokens_file):
        self.config = self.load_config(config_file)
        self.tokens = self.get_tokens(tokens_file)
        self.base_bet = self.config['base_bet']
        self.multiplier = self.config['multiplier']
        self.bet_delays = random.uniform(0.2, 0.3)
        self.is_upper = self.config['is_upper']
        self.stop_win = self.config['stop_win']
        self.stop_lose = self.config['stop_lose']
        self.if_win = self.config['if_win']
        self.if_lose = self.config['if_lose']
        self.low = self.config['low_chance']
        self.high = self.config['high_chance']
        self.target_balance = self.config['target_balance']
        self.url = "https://api-dice.goatsbot.xyz/dice/action"
        self.headers = {
            "accept": "application/json, text/plain, */*",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "id,en-US;q=0.9,en;q=0.8,id-ID;q=0.7",
            "content-type": "application/json",
            "origin": "https://dev.goatsbot.xyz",
            "referer": "https://dev.goatsbot.xyz/",
            "user-agent": "Mozilla/5.0 (Linux; Android 12; K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36",
            "authorization": f"Bearer {self.tokens}"
        }
    
    def load_config(self, file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    def get_tokens(self, file_path):
        with open(file_path, 'r') as file:
            return file.read().strip()

    async def place_bet(self, session, payload):
        try:
            async with session.post(self.url, headers=self.headers, json=payload) as response:
                if response.status == 201:
                    return await response.json()
                else:
                    return None
        except aiohttp.ClientError as e:
            print(f"Request failed during placing bet: {e}")
            return None

    async def get_initial_balance(self, session):
        initial_balance_url = "https://api-me.goatsbot.xyz/users/me"
        try:
            async with session.get(initial_balance_url, headers=self.headers) as response:
                if response.status == 200:
                    result = await response.json()
                    return result['balance']
                else:
                    print(f"Failed to fetch balance, status code: {response.status}")
                    return None
        except aiohttp.ClientError as e:
            print(f"Request failed during fetching balance: {e}")
            return None

    async def start_betting(self):
        async with aiohttp.ClientSession() as session:
            bet = self.base_bet
            current_win = 0
            current_loss = 0
            total_profit = 0

            initial_balance = await self.get_initial_balance(session)
            if initial_balance is None:
                print("Failed to get initial balance. Exiting.")
                return

            balance = initial_balance
            previous_balance = balance
            print(bru + 
                f"W/L | CHANCE   | BET       | RESULT  | BALANCE         | Profit"
                )
            log_line()

            while True:
                chance = round(random.uniform(self.low, self.high), 2)

                if balance < bet:
                    print(f"{mrh}Insufficient balance to place the next bet. Stopping betting.")
                    print(f"Total Win: {current_win}, Total Loss: {current_loss}, Total Profit: {total_profit}")
                    break

                payload = {
                    "point_milestone": chance,
                    "is_upper": self.is_upper,
                    "bet_amount": bet
                }

                result = await self.place_bet(session, payload)

                if result:
                    balance = result['user']['balance']
                    is_win = result['dice']['is_win']
                    reward = round(result['dice']['reward'], 2)

                    if is_win:
                        current_win += reward
                        current_loss = 0
                        total_profit += reward - bet
                        
                        if balance >= previous_balance:
                            print(hju + 
                                f"[ W ] C: {pth}{chance:5,.1f} {hju}| " +
                                f"B: {pth}{bet:6,.2f} {hju}| " +
                                f"{pth}{reward:7.1f} {hju}| " +
                                f"Bal: {pth}{balance:10,.1f} {hju}| " +
                                f"Profit: {pth}{total_profit:7,.1f}"
                                )
                            bet = self.base_bet
                            previous_balance = balance
                        else:
                            print(kng + 
                                f"[ - ] C: {pth}{chance:5,.1f} {kng}| " +
                                f"B: {pth}{bet:6,.2f} {kng}| " +
                                f"{pth}{reward:7.1f} {kng}| " +
                                f"Bal: {pth}{balance:10,.1f} {kng}| " +
                                f"Profit: {pth}{total_profit:7,.1f}"
                                )
                            bet *= self.multiplier
                            continue

                        if reward >= self.stop_win:
                            print(f"{hju}Reached win target! Stopping bets.") 
                            break

                        if balance >= self.target_balance:
                            print(f"{hju}Reached target balance! Stopping bets.")
                            break

                        if self.if_win == 'reset':
                            bet = self.base_bet
                        elif self.if_win == 'multiply':
                            bet *= self.multiplier
                    else:
                        current_loss += bet
                        total_profit -= bet 

                        print(mrh + 
                            f"[ L ] C: {pth}{chance:5,.1f} {mrh}| " +
                            f"B: {pth}{bet:6,.2f} {mrh}| " +
                            f"{pth}{reward:7.1f} {mrh}| " +
                            f"Bal: {pth}{balance:10,.1f} {mrh}| " +
                            f"Profit: {pth}{total_profit:7,.1f}"
                            )

                        if current_loss >= self.stop_lose:
                            print(f"{mrh}Reached loss limit! Stopping bets.")
                            break

                        if self.if_lose == 'multiply':
                            bet *= self.multiplier
                        elif self.if_lose == 'reset':
                            bet = self.base_bet

                await asyncio.sleep(self.bet_delays)

async def main():
    bot = DiceBettingBot('config.json', 'tokens.txt')
    await bot.start_betting()

if __name__ == "__main__":
    _clear()
    _banner()
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n{mrh}Stopping betting loop...")
        sys.exit()
