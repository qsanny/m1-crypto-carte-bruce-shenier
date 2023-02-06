from crypto import *
from carte import *

message = "SALUT"

key = generatekey(len(message))
message_enc = encode(message, key)

print(message)

print(message_enc)

cg = CardGame()
print((cg))