from random import random;

successChance = .5;
wallet = 1000;
martingaleFactor = 2.1;
payout = .5*1.97/successChance;
minimumBet = 10;

def gamble(chance):
    return random() < chance;

def bet(amount, wallet, verbose):
    success = gamble(successChance);
    if(success):
        if(verbose):
            print("bet: " + str(amount) + " | WIN  | +" + str(amount*payout) + " | Wallet: " + str(wallet+amount*payout) + "TRX");
        return amount*payout-amount;
    else:
        if(verbose):
            print("bet: " + str(amount) + " | LOSE | -" + str(amount) + " | Wallet: " + str(wallet-amount) + "TRX");
        return -amount;

def martingale(startingBet, wallet, verbose):
    if(verbose):
        print("------------ martingale's ------------");
        print("simulating...");
    rounds = 0;
    peak = wallet;
    losingStreak = 0;
    currentBet = startingBet;
    while(wallet > currentBet):
        returns = bet(currentBet, wallet, verbose);
        wallet += returns;
        if(returns > 0):
            losingStreak = 0;
        else:
            losingStreak += 1;
        currentBet = pow(martingaleFactor, losingStreak) * startingBet;
        rounds += 1;
        if(wallet > peak):
            peak = wallet;
    if(verbose):
        print("survived " + str(rounds) + " rounds before we lost all our money");
        print("peak: " + str(peak) + "TRX");
    return [rounds, peak];

def prettyPrintResults(results):
    print('Rounds | Peak TRX');
    print('--------------------------');
    for result in results:
        print '{:6d} | {:10f}'.format(result[0], result[1]);

print("---------------- MARTINGALE'S SIMULATION -------------------");
print("Odds of success: " + str(successChance*100) + "%");
print("Payout: " + str(payout) + "x");
print("Starting wallet: " + str(wallet)) + "TRX";
results = [];
for i in range(1,5):
    results.append(martingale(minimumBet, wallet, False));
prettyPrintResults(results);
