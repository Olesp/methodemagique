def get_addresses(multiples: list, magic_number_index, ip):
    for i in range(len(multiples)):
        if multiples[i] <= int(ip[magic_number_index]):
            z = multiples[i + 1] - 1
        else:
            break
    last_address = []
    for i in range(0, 4, 1):
        if i < magic_number_index:
            last_address.append(ip[i])
        elif i == magic_number_index:
            last_address.append(z)
        else:
            last_address.append(255)
    return last_address


def get_multiples(magic_number):
    multiples = []
    i = 0
    while i <= 256:
        multiples.append(i)
        i += magic_number
    return multiples


def get_magic_number(netmask) -> list:
    for octet in netmask:
        if int(octet) != 255:
            magic_number = 256 - int(octet)
            magic_number_index = netmask.index(octet)
            return magic_number, magic_number_index

class Plage():
    """
    Classe représentant une plage d'adresses réseau ainsi que son masque
    """

    name = ""
    nb = 0
    netmask = ["","","",""]
    start = []
    end = []
    puissances = []
    magic_number = 0
    magic_number_index = 0

    def __init__(self, name: str, nb: int, start) -> object:
        self.set_name(name)
        self.set_nb(nb)
        for i in range(10):
            self.puissances.append(2**(i+1))
        self.set_netmask()
        self.set_start(start)
        self.set_end()

    def set_name(self, name):
        """
        Set the subnet name
        """
        self.name = name

    def get_name(self) -> str:
        """
        Return the subnet name
        """
        return  self.name

    def set_nb(self, nb):
        """
        Set the nb of adresses
        """
        self.nb = nb

    def get_nb(self) -> int:
        """
        Return the nb of adresses
        """
        return  self.nb

    def set_netmask(self):
        """
        Set the netmask
        """
        self.netmask = self.calculate_netmask()

    def get_netmask(self) -> list:
        """
        Return netmask
        """
        return self.netmask

    def calculate_byte(self, byte) -> str:
        """
        Return the string of bytes in binary to a bytes in string like "255"
        """

        byte = str(int(byte,2))
        return byte


    def calculate_netmask(self) -> list:
        """
        Return an array bytes["255","255","255","0"]
        """
        netmask = ["","","",""]
        for i in self.puissances:
            if self.nb < int(i):
                c = self.puissances.index(i)+1
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

    def set_start(self, start):
        self.start = start

    def set_magic_number(self):
        self.magic_number, self.magic_number_index = get_magic_number(self.netmask)

    def set_end(self):
        self.set_magic_number()
        self.end = get_addresses(get_multiples(self.magic_number),self.magic_number_index,self.start)

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end
