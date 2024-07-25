
from DNS import *

class DNSC(DNS):
    def __init__(self):
        DNS.__init__(self)
        self.__blacklist = set()

    def blacklist(self, IpAddress):
        self.__blacklist.add(IpAddress)

    def lookup(self, webAddress):
        IPresult = self._dns.get(webAddress, 'None')
        if IPresult in self.__blacklist:
            return None
        else:
            return IPresult
