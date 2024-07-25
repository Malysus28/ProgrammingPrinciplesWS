class DNS:
    def __init__(self):
        self._dns = dict()  # empty dictionary

    def update(self, webAddress, IpAddress):
        self._dns[webAddress] = IpAddress

    def lookup(self, webAddress):
        return self._dns.get(webAddress, 'None')
        # Return 'None' if webAddress is not found

dns_table = DNS()
command = input("? ")

while command != "q":
    wordList = command.split()
    if len(wordList) == 3 and wordList[0] == "u":
        dns_table.update(wordList[1], wordList[2])  # Update DNS
    elif len(wordList) == 2 and wordList[0] == "l":
        result = dns_table.lookup(wordList[1])  # Look up DNS
        print(result)  # Print the result
    elif len(wordList) == 2 and wordList[0] == "b":
        # You need to implement a feature to check if an IP address is in the blacklist
        pass
    else:
        print("Bad command")
    command = input("? ")
