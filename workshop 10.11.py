class goCard:
    def __init__(self, startBal):
        self.balance = startBal
        self.records = [startBal]
    def takeRide(self, amount):
        self.balance -= amount
        self.records.append(-amount)
    def TopUp(self, amount):
        self.balance += amount
        self.records.append(amount)
    def getBalance(self):
        print("Balance =", self.balance)
        return self.balance
    def PrintStatement(self):
        print("Statement:  ")
        print("{:20s} {:>15s} {:>15s}".format("event", "amount($)", "balance ($)"))
        currentBalance = self.records[0]
        print("{:20s} {:>15s} {:>15.2f}".format("Initial Balance", "   ", self.records[0]))
        for number in self.records[1:]:
            currentBalance = currentBalance + number
            if number < 0:
                print("{:20s} {:15s} {:15.2f} ".format("Ride", str(-number), currentBalance))
            else:
                print("{:20s} {:15s} {:15.2f} ".format("Top Up", str(number), currentBalance))
        print("{:20s} {:>15s} {:15.2f} ".format("Final Balance", "", currentBalance))


amount = float(input("Creating Account: Enter Initial Balance: "))
alanGoCardAccount = goCard(amount)
command = input("Enter command (r () /t () /b () /q () : ")

while command.strip() != "q":
    wordlist = command.strip().split()

    if len(wordlist) == 2 and wordlist[0] == "r":
        alanGoCardAccount.takeRide(float(wordlist[1]))

    elif len(wordlist) == 2 and wordlist[0] == "t":
        alanGoCardAccount.TopUp(float(wordlist[1]))

    elif len(wordlist) == 1 and wordlist[0] == "b":
        alanGoCardAccount.getBalance()

    else:
        print("Bad command. Try 'r', 't', 'b', or 'q'.")

    command = input('Enter command (r ()/t ()/b ()/q ()): ')

alanGoCardAccount.PrintStatement()
