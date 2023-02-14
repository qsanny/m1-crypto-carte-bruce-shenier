from keygen import *
from carte import *
from encoder import EncodeDecoder

message = "SALUT"

encoder = EncodeDecoder(KeyGenerator())
encoded_msg = encoder.encode(message)