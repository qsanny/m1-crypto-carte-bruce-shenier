from crypto import *

message = "SALUT"

key = generatekey(len(message))
message_enc = encode(message, key)

print(message)

print(message_enc)