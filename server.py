from typing import Union

from fastapi import FastAPI

from keygen import *
from carte import *
from coder import Encoder, Decoder

from ui import Interface


message = "SALUT"

encoder = Encoder(KeyGenerator())
decoder = Decoder(KeyGenerator())

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/encode/{message}")
def encode_msg(message: str):
    encoded_msg = encoder.encode(message)
    return {"encoded": encoded_msg}
