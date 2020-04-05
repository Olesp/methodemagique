def check_len(list):
    # Vérifie que la liste compoprte bien 4 éléments
    if len(list) < 4:
        print("Votre entrée doit contenir 4 octets")
        return False
    else:
        return True


def get_multiples(magic_number):
    multiples = []
    i = 0
    while i <= 256:
        multiples.append(i)
        i += magic_number
    return multiples


def get_addresses(multiples : list, magic_number_index, ip):
    i = 0
    for i in range(len(multiples)):
        if multiples[i] <= int(ip[magic_number_index]):
            x = multiples[i]
            z = multiples[i + 1] - 1
        else:
            break
    first_address = []
    last_address = []
    for i in range(0, 4, 1):
        if i < magic_number_index:
            first_address.append(ip[i])
            last_address.append(ip[i])
        elif i == magic_number_index:
            first_address.append(x)
            last_address.append(z)
        else:
            first_address.append(0)
            last_address.append(255)
    return first_address, last_address


def get_magic_number(netmask) -> list:
    for octet in netmask:
        if int(octet) != 255:
            magic_number = 256 - int(octet)
            magic_number_index = netmask.index(octet)
            return magic_number, magic_number_index


def check_int(list) -> bool:
    #Vérifie que la liste ne comporte que des entiers
    for i in list:
        try:
            i = int(i)
        except:
            print("Erreur votre entrée ne doit contenir que des nombres!")
            return False
    return True


def input_address() -> list:
    #Permet à l'utilisateur de rentrer une adresse IP
    ip_user = input("Entrez l'adresse (ex: 192.168.0.1) :")
    ip = ip_user.split(".")
    return ip


def input_mask() -> list:
    #Permet à l'utilisateur de rentrer un masque réseau
    netmask_user = input('Entrez un masque réseau (ex: 255.255.255.0) :')
    netmask = netmask_user.split(".")
    return netmask


class Network():
    address:[]
    netmask=[]
    start=[]
    end=[]
    magic_number = 0
    magic_number_index = 0
    name = ""

    def __init__(self):
        self.set_network_name()
        self.set_network_address()
        self.set_network_netmask()
        self.set_magic_number()
        self.set_addresses()

    def set_network_address(self):
        self.address = input_address()
        t = False
        while not t:
            if not check_len(self.address):
                self.address = input_address()
            else:
                if not check_int(self.address):
                    self.address = input_address()
                else:
                    t = True

    def set_network_name(self):
        self.name = input("Entrez un nom pour votre réseau : ")

    def set_network_netmask(self):
        self.netmask = input_mask()
        t = False
        while not t:
            if not check_len(self.netmask):
                self.netmask = input_mask()
            else:
                if not check_int(self.netmask):
                    self.netmask = input_mask()
                else:
                    t = True

    def set_magic_number(self):
        self.magic_number, self.magic_number_index = get_magic_number(self.netmask)
    
    def set_addresses(self):
        self.start, self.end = get_addresses(get_multiples(self.magic_number),self.magic_number_index,self.address)

    def get_address(self):
        return self.address

    def get_name(self):
        return self.name

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def get_netmask(self):
        return self.netmask

    def send_to_json(self):
        data = []
        data.append({
            'netmask' : self.netmask,
            'first_address': self.start,
            'last_address': self.end
        })
        return data