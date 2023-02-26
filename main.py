from keygen import *
from carte import *
from coder import Encoder, Decoder

from ui import Interface


message = "SALUT"

encoder = Encoder(KeyGenerator())
decoder = Decoder(KeyGenerator())

# encoded_msg = encoder.encode(message)
# print(f"{message} -> {encoded_msg} -> {decoder.decode(encoded_msg)} ")
# message = input('msg$  ')

Interface().show()

while(message !="end" and message !="q"):
    encoded_msg = encoder.encode(message)
    print(f"{message} -> {encoded_msg} -> {decoder.decode(encoded_msg)} ")
    message = input('msg$  ')
