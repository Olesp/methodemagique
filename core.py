# Petit programme calculant les premières et dernières adresses d'un réseau


def get_magic_number(list):
    for octet in list:
        if int(octet) != 255:
            magic_number = 256 - int(octet)
            magic_number_index = list.index(octet)
            return magic_number, magic_number_index


def input_address():
    # Permet à l'utilisateur de rentrer une adresse IP
    ip_user = input("Entrez l'adresse (ex: 192.168.0.1) :")
    ip = ip_user.split(".")
    return ip


def input_mask():
    # Permet à l'utilisateur de rentrer un masque réseau
    netmask_user = input('Entrez un masque réseau (ex: 255.255.255.0) :')
    netmask = netmask_user.split(".")
    return netmask


def check_len(list):
    # Vérifie que la liste compoprte bien 4 éléments
    if len(list) < 4:
        print("Votre entrée doit contenir 4 octets")
        return False
    else:
        return True


def check_int(list):
    # Vérifie que la liste ne comporte que des entiers
    for i in list:
        try:
            i = int(i)
        except:
            print("Erreur votre entrée ne doit contenir que des nombres!")
            return False
    return True


def get_multiples(magic_number):
    multiples = []
    i = 0
    while i <= 256:
        multiples.append(i)
        i += magic_number
    return multiples


def get_addresses(multiples: list, magic_number_index, ip):
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


def main():
    """
    Entry point
    """

    ip = input_address()
    t = False
    while not t:
        if not check_len(ip):
            ip = input_address()
        else:
            if not check_int(ip):
                ip = input_address()
            else:
                t = True

    netmask = input_mask()
    t = False
    while not t:
        if not check_len(netmask):
            netmask = input_mask()
        else:
            if not check_int(netmask):
                netmask = input_mask()
            else:
                t = True

    magic_number, magic_number_index = get_magic_number(netmask)
    multiples = get_multiples(magic_number)
    first_address, last_address = get_addresses(
        multiples, magic_number_index, ip)

    print("La première adresse disponible est : {}\nLa dernière adresse du réseau est : {}".format(
        first_address, last_address))


if __name__ == "__main__":
    main()
