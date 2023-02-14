from keygen import *
from carte import *
from coder import Encoder, Decoder

message = "SALUT"

encoder = Encoder(KeyGenerator())
decoder = Decoder(KeyGenerator())

while(message !="end"):
    encoded_msg = encoder.encode(message)
    print(f"{message} -> {encoded_msg} -> {decoder.decode(encoded_msg)} ")
    message = input('msg$  ')
