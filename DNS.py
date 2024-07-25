class DNS:
    def __init__(self):
        self._dns = dict()  # empty dictionary

    def update(self, webAddress, IpAddress):
        self._dns[webAddress] = IpAddress


    def lookup(self, webAddress):
        return self._dns.get(webAddress, 'None')
        # Return 'None' if webAddress is not found

