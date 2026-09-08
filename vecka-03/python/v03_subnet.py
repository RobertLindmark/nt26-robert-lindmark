import ipaddress    

#Byt ut mot den nat du vill räkna på.
text = "192.168.1.64/26"

# Moddulen ipadress gör räkningen åt dig
net = ipaddress.ip_network(text, strict=False)

#Alla adresser du kan ge till en enhet
usable = list(net.hosts())

print(f"Nat:                 {net.network_address}")
print(f"Natmask:             {net.netmask}")
print(f"Broadcast:           {net.broadcast_address}")
print(f"Forsta Adress:       {usable[0]}")
print(f"Sista Adress:        {usable[-1]}")
print(f"Antal enheter:       {len(usable)}")
