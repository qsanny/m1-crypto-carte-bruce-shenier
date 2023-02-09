from carte import CardGame, CarteType, CarteValeur, Carte

def encode(message, cle):
    message=message.upper()
    cle=cle.upper()
    encoded_msg = ""
    for i, m in enumerate(message):
        nm = ord(m) - 65 + 1
        nc = ord(cle[i]) - 65 + 1

        ne = (nm + nc)
        if ne > 26:
            ne = ne - 26
        # print(ne)
        encoded_msg+=chr(ne + 65 - 1)
    return encoded_msg


def decode(message):
    # to decode we need the init state of the cards
    pass

def generatekey(n):
    # key must have same lenth as the message. 
    # n is the size of the key we want to generate

    return "acrpm"


class KeyGenerator:
    def __init__(self) -> None:
        self.key = ""
        self.cards = CardGame()
    
    def generate_key(self, n: int):
        self.step_1()
    
    def step_1(self):
        '''
        Recul du joker noir d’une position : Vous faites reculer le joker noir d’une place (vous le permutez avec
        la carte qui est juste derrière lui). Si le joker noir est en dernière position il passe derrière la carte du
        dessus (donc, en deuxième position).
        '''
        print(self.cards)
        black_joker_pos = self.cards.get_carte_pos(Carte(CarteType.JOCKER, CarteValeur.NOIR))
        if black_joker_pos == 53:
            # last element
            self.cards.cartes.pop(black_joker_pos)
            self.cards.set_card_pos(Carte(CarteType.JOCKER, CarteValeur.NOIR), 1)
        else:
            self.cards.swap_cards(black_joker_pos, black_joker_pos+1)
        print(self.cards)

    def step_2(self):
        pass

    def step_3(self):
        pass

    def step_4(self):
        pass

    def step_5(self):
        pass
