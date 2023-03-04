from typing import Union, List

from fastapi import FastAPI

from keygen import *
from carte import *
from coder import Encoder, Decoder

from ui import Interface
import json

message = "SALUT"

encoder = Encoder(KeyGenerator())
decoder = Decoder(KeyGenerator())

class Main:
    def __init__(self) -> None:
        self.encoder = Encoder(KeyGenerator())
        self.decoder = Decoder(KeyGenerator())
    
    def set_key_gen(self, key: List[str]):
        self.encoder = Encoder(KeyGenerator(key))
        self.decoder = Decoder(KeyGenerator(key))

    def encode(self, msg) -> str:
        return self.encoder.encode(msg)

    def decode(self, msg)-> str:
        return self.decoder.decode(msg)

app = FastAPI()
main = Main()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/set_deck/{deck}")
def set_deck_order(deck: str):
    deck = deck.replace('[', '')
    deck = deck.replace(']', '')
    key = deck.split(',')
    main.set_key_gen(key)

    return {"test": "test"}

@app.get("/encode/{message}")
def encode_msg(message: str):
    encoded_msg = main.encode(message)
    return {"encoded": encoded_msg}

@app.get("/decode/{message}")
def encode_msg(message: str):
    decoded_msg = main.decode(message)
    return {"decoded": decoded_msg}