# Goats Dice (DICING) Betting Bot

A Python-based dice betting bot that uses the GoatsBot API in Telegram-based Bot @RealGoats_bot to automate dice game betting. The bot uses asynchronous operations with `aiohttp` for API interaction and dynamic betting strategies based on user configuration.

[TELEGRAM CHANNEL](https://t.me/Deeplchain) | [TWITTER](https://x.com/itsjaw_real)

## Register

To use this bot, you need to register it with the Goats Telegram Bot. 

1. Open the bot [t.me/Realgot_real](https://t.me/realgoats_bot/run?startapp=99effa5e-ac44-4be5-8f0d-64cf69f796e9)
2. Click on the "[Start App](https://t.me/realgoats_bot/run?startapp=99effa5e-ac44-4be5-8f0d-64cf69f796e9)" or "[Open App]([url](https://t.me/realgoats_bot/run?startapp=99effa5e-ac44-4be5-8f0d-64cf69f796e9))" button
3. Install This Real Goats Automations Bot
4. Have Fun 🦈

**Previous repository for Real Goats (Full Feature):** https://github.com/jawikas/goats-bot
=
## Features

- Automated betting with dynamic chance adjustment.
- Real-time tracking of wins, losses, balance, and profit.
- Configurable bet amounts and multiplier settings.
- Stop betting based on user-defined win/loss limits or target balance.
- Adjustable delays between bets to mitigate detection.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/jawikas/goats-dice-bot.git
    cd goats-dice-bot
    ```

2. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

The bot requires two configuration files: `config.json` and `tokens.txt`.

### `config.json`

This file contains various settings for the bot's operation. Below is a sample configuration:

```json
{
    "base_bet": 1,
    "multiplier": 1.533, 
    "low_chance": 49.1,
    "high_chance": 67.5,
    "is_upper": false,
    "stop_win": 10000,
    "stop_lose": 10000,
    "target_balance": 50000,
    "if_win": "reset",  
    "if_lose": "multiply"
}
```
`base_bet`: The initial amount to bet.

`multiplier`: The multiplier to apply after a loss.

`is_upper`: Whether to bet on higher dice rolls.

`stop_win`: The target amount of profit to stop betting.

`stop_lose`: The amount of loss to stop betting.

`if_win`: Strategy after a win ("`reset`" to reset bet, "`multiply`" to increase bet).

`if_lose`: Strategy after a loss ("`reset`" to reset bet, "`multiply`" to increase bet).

`low_chance`: Minimum chance to win.

`high_chance`: Maximum chance to win.

`target_balance`: Balance to stop betting.

### tokens.txt
This file should contain your token. Example:

1. Use PC/Laptop or Use USB Debugging Phone
2. open the `RealGoats Telegram bot`
3. Inspect Element `(F12)` on the keyboard
4. at the top of the choose "`Network`" 
5. then select "`User` or `Me` or `Banner`" 
6. Select the section "`Headers`" on "`Authorization`"
7. Take the value part of "`bearer {your token here}`"
8. take the part that looks like this:
```txt
eyJhbGciOiJIccxxxxUZjUwNjhjYjQ0NTU2NjM1MzFjIiwiaWF0IjoxU5NTExxxwOTQsInR5cGxxxUiOiJhY2Nlc3xxxxMihNssBJMy-268k5ZcFlLxxxKDTSI
```
9. Add it to `tokens.txt`
```txt
your_goats_token_here
```
### Usage
Run the bot:

```bash
python main.py
```
Stop the bot: Press Ctrl+C in the terminal to stop the bot gracefully.

### Example Output
The bot will print logs in the terminal, which might look like this:

```yaml
W/L | CHANCE   | BET       | RESULT  | BALANCE         | Profit
[ W ] C:  50.0 | B:   1.00 |     2.0 | Bal:   22,788.0 | Profit: 1,400.0
[ L ] C:  45.0 | B:   2.00 |     0.0 | Bal:   22,786.0 | Profit: 1,398.0
```
### Requirements
Create a requirements.txt file with the following content:

```bash
aiohttp==3.8.5
colorama==0.4.6
asyncio==3.4.3
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any questions or support, please contact https://t.me/DeeplChainSup.

## Disclaimer

```txt
**Use at Your Own Risk:** This bot is designed for educational and experimental purposes only. Betting and gambling carry inherent risks, and using this bot does not guarantee profits. Be aware of the legal and financial implications of online gambling in your jurisdiction before using this bot.

**API Limits and Changes:** The bot interacts with the GoatsBot API, which may have usage limits or change over time. The functionality of this bot may be affected by changes in the API or its policies.

**No Warranty:** The developers of this bot make no warranties regarding its performance, accuracy, or reliability. Use this bot at your own risk, and ensure you understand how it works before deploying it in a live environment.

**Financial Responsibility:** The creators and contributors of this bot are not responsible for any financial loss, damage, or legal issues that may arise from its use. Always gamble responsibly and only wager what you can afford to lose.
```
By using this bot, you acknowledge that you have read and understood this disclaimer and agree to use it responsibly.
