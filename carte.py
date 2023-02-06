from enum import Enum

class Carte:
    def __init__(self, type, value):
        self.type: CarteType = type
        self.valeur: CarteValeur = value
    
    def __str__(self) -> str:
        return f"#{self.get_number()}: {self.valeur.name} de {self.type.name} \n"

    def get_number(self):
        return abs( 13 * self.type.value + self.valeur.value)

class CarteType(Enum):
    TREFLE = 0
    CARREAU = 1
    COEUR = 2
    PIQUE = 3

    JOCKER = -1 #nope

class CarteValeur(Enum):
    AS = 1
    _2 = 2
    _3 = 3
    _4 = 4
    _5 = 5
    _6 = 6
    _7 = 7
    _8 = 8
    _9 = 9
    _10 = 10
    VALET = 11
    DAME = 12
    ROI = 13

    NOIR = 53 # jope
    BLANC = 54 #nope

class CardGame:
    def __init__(self) -> None:
        self.cartes: list[Carte] = self.init_cards()
    
    def init_cards(self) -> list[Carte]:
        cartes = []
        for ct in CarteType:
            if ct != CarteType.JOCKER: # TODO can be avoided !!
                for cv in CarteValeur:
                    if cv != CarteValeur.NOIR and cv != CarteValeur.BLANC: # TODO can be avoided !!
                        cartes.append(Carte(ct, cv))
        cartes.append(Carte(CarteType.JOCKER, CarteValeur.NOIR)) # TODO SHOULD NOT BE AS! NEED REFACTORING !!
        cartes.append(Carte(CarteType.JOCKER, CarteValeur.BLANC ))

        return cartes

    def get_carte_pos(self, carte: Carte) ->int:
        for (i, c) in enumerate(self.cartes):
            if(c.get_number() == carte.get_number()):
                return i

    def __str__(self) -> str:
        s = ""
        for c in self.cartes:
            s += c.__str__()
        return s



