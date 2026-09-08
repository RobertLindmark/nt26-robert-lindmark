
def vlan_config(number, name):
    rader = []
    rader.append(f"vlan {number}")
    rader.append(f" name {name}")
    return rader

#Nat på Nordvik. byt ut mot de du ska använda. (Configar Nordvik så den liknar)
vlans = {
    10: "KONTOR",
    20: "EKONOMI",
    30: "GAST",
    40: "DRIFT",
    }

for number in vlans:
    for rad in vlan_config(number, vlans[number]):
        print(rad)