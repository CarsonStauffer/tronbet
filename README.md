A simulation to show that martingale's DOES NOT WORK unless you have infinite money.

### Installation and usage

This project has no dependencies. Run the simulation with `python main.py`

### Modifying simulation parameters

Variables are self-explanatory. Payout is based on payout rate by Tronbet.

Pass verbose in as True into martingale() to get output for each bet and see how the Martingale algorithm increases the bets during losing streaks to try and recuperate losses.

In the output, "rounds" is how many bets you were able to make before you lost all your money. Having a larger wallet/minimumBet ratio lets you last more rounds. "Peak" is the most money you had during your run.

### The sad truth

Unless you have infinite money to keep doubling down, eventually you will run ALWAYS run into a losing streak large enough to bankrupt you. There is no way to see it coming, nor is there any way to predict when you are at a high and should quit while you're ahead.
