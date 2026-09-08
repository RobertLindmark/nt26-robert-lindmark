
vendors = {
    "a4:c3:f0": "Intel",
    "3c:d9:2b": "HP",
    "00:1a:a1": "Cisco Systems",
    "00:1b:63": "Apple",
    "fc:fb:fb": "Cisco Systems",
    "00:02:b3": "Intel",
    "00:03:ff": "Microsoft",
    "00:00:f0": "Samsung",
    "00:14:22": "Dell",
    "ec:89:14": "Lenovo",
    "50:c7:bf": "TP-Link",
    "24:a4:3c": "Ubiquiti",
    "00:05:85": "Juniper",
    "9c:1c:12": "Aruba",
    "00:0c:29": "VMware",
    "08:60:6e": "ASUS",
    "08:bf:b8": "ASUS",
    "64:09:80": "Xiaomi",
    "44:94:fc": "Netgear",
    "b8:27:eb": "Raspberry Pi",
} 
#Adresser du ska kolla
addresses = [
    "a4:c3:f0:11:3a:b7",
    "3c:d9:2b:d2:11:88",
    "8c:85:90:44:12:0e",
]

for address in addresses:
    prefix = address [0:8]. lower()

    if prefix in vendors:
        name = vendors [prefix]
    else:
        name = "okand tillverkare"

    print(f"{address}   -->     {name}")
