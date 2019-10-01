import re
ident=input("Enet the identifier:")
matcher=re.fullmatch('^[a-k]{1}[0369]{1}[0-9a-zA-Z#]*',ident)
if matcher==None:
    print("Invalid identifier")
else:
    print("Your identifier is accepted!!")
