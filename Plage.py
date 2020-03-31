
class Plage():

    name = ""
    nb = 0
    netmask = []
    start = []
    end = []
    puissances = []

    def __init__(self, name: str, nb: int, address = [], type = "plage",mask = []) -> object:
        super().__init__()
        self.set_name(name)
        self.set_nb(nb)
        for i in range(10):
            self.puissances.append(2**(i+1))
        if type == "network" or address:
            print(address)
            self.initiate_network(address)
            self.netmask = mask
        else:
            self.set_netmask()
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return  self.name

    def set_nb(self, nb):
        self.nb = nb

    def get_nb(self):
        return  self.nb

    def set_netmask(self):
        self.netmask = self.calculate_netmask()

    def get_netmask(self):
        return self.netmask

    def calculate_byte(self, byte):
        #Return the string of bytes in binary to a bytes in string like "255"
        byte = str(int(byte,2))
        return byte

    def initiate_network(self, address):
        for i in address:
            self.start.append(i)

    def calculate_netmask(self):
        netmask = ["","","",""]
        #Return an array bytes["255","255","255","0"]
        for i in self.puissances:
            if self.nb < int(i):
                c = self.puissances.index(i)
                break

        k = 32 - c
        for i in range(4):
            bytes = ""
            for q in range(8):
                if k > 0:
                   bytes += "1"
                else:
                    bytes += "0"
                k -= 1
            netmask[i] = self.calculate_byte(bytes)
        return netmask
