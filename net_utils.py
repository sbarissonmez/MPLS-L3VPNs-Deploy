from netaddr import IPNetwork


def address(add):
    "The following code will extract the IP address from a given network address, such as "10.0.0.1/24", and return only the IP portion, which in this case would be '10.0.0.1'"
    add = str(IPNetwork(add).ip)
    return add


def mask(submask):
    "This code will extract the subnet mask from a network address such as "10.0.0.1/24" and return the corresponding subnet mask value, which in this case would be '255.255.255.0'"
    submask = str(IPNetwork(submask).netmask)
    return submask
