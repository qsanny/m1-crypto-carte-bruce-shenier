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
        self.step_2()
    
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
            self.cards.set_card_pos(Carte(CarteType.JOCKER, CarteValeur.NOIR), 1)
        else:
            self.cards.set_card_pos(Carte(CarteType.JOCKER, CarteValeur.NOIR), black_joker_pos+1)

        print(self.cards)

    def step_2(self):
        '''
        Recul du joker rouge de deux positions : Vous faites reculer le joker rouge de deux cartes. 
            S’il  ́etait en derni`ere position, il passe en troisi`eme position;
            s’il  ́etait en avant derni`ere position il passe en deuxi`em
        '''
        red_jocker_pos = self.cards.get_carte_pos(Carte(CarteType.JOCKER, CarteValeur.ROUGE))
        # self.cards.cartes.pop(red_jocker_pos) # remove the jocker from his current position

        if red_jocker_pos == 53:
            self.cards.set_card_pos(Carte(CarteType.JOCKER, CarteValeur.ROUGE), 2) # put it back on the 3th position
        elif red_jocker_pos == 52:
            self.cards.set_card_pos(Carte(CarteType.JOCKER, CarteValeur.ROUGE), 1) # put it back on the 2nd position
        else:
            self.cards.set_card_pos(Carte(CarteType.JOCKER, CarteValeur.ROUGE), red_jocker_pos+2) # put it back on the 2nd position

    def step_3(self):
        '''
        Double coupe par rapport aux jokers.
            Vouz rep ́erez les deux jokers et 
            vous intervertissez 
                le paquet des cartes situ ́ees au-dessus du joker qui est en premier avec 
                le paquet de cartes qui est au-dessous du joker qui est en second. 
        Dans cette op ́eration la couleur des jokers est sans importance
        '''
        red_jocker_pos = self.cards.get_carte_pos(Carte(CarteType.JOCKER, CarteValeur.ROUGE))
        black_joker_pos = self.cards.get_carte_pos(Carte(CarteType.JOCKER, CarteValeur.NOIR))

        first = red_jocker_pos if red_jocker_pos < black_joker_pos else black_joker_pos
        second = red_jocker_pos if red_jocker_pos > black_joker_pos else black_joker_pos

        top = self.cards.cartes[:first]
        center = self.cards.cartes[first:second+1]
        bottom = self.cards.cartes[second+1:]

        new_set = bottom + center + top
        self.cards.cartes = new_set

    def step_4(self):
        '''
        Coupe simple d ́etermin ́ee par la derni`ere carte :
            vous regardez la derni`ere carte et
                vous  ́evaluez son num ́ero selon l’ordre du Bridge
                Si le num ́ero de la derni`ere carte est n
                    vous prenez les n premi`eres cartes du dessus du paquet et
                    les placez derri`ere les autres cartes
                        `a l’exception de la derni`ere carte qui reste la derni`ere.
        '''
        last_card = self.cards.cartes[-1]
        n = last_card.get_number()
        top = self.cards.cartes[:n+1]
        reste = self.cards.cartes[n+2:-1]
        last = [self.cards.cartes[-1]]
        
        new_set = reste + top + last
        self.cards.cartes = new_set

    def step_5(self):
        pass
