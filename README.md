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