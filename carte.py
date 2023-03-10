from enum import Enum


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
    ROUGE = 54 #nope

class Carte:
    def __init__(self, type: CarteType, value: CarteValeur):
        self.type: CarteType = type
        self.valeur: CarteValeur = value
    
    def __str__(self) -> str:
        return f"#{self.get_number()}: {self.valeur.name} de {self.type.name} \n"

    def get_number(self) -> int:
        if self.type == CarteType.JOCKER:
            return 53
        return 13 * self.type.value + self.valeur.value
    
    def get_number2(self) -> int:
        if self.type == CarteType.JOCKER and self.valeur == CarteValeur.NOIR:
            return 54
        elif self.type == CarteType.JOCKER and self.valeur == CarteValeur.ROUGE:
            return 53
        return 13 * self.type.value + self.valeur.value
        


class CardGame:
    def __init__(self) -> None:
        self.cartes: list[Carte] = self.init_cards()
    
    def init_cards(self) -> "list[Carte]":
        cartes = []
        for ct in CarteType:
            if ct != CarteType.JOCKER: # TODO can be avoided !!
                for cv in CarteValeur:
                    if cv != CarteValeur.NOIR and cv != CarteValeur.ROUGE: # TODO can be avoided !!
                        cartes.append(Carte(ct, cv))
        cartes.append(Carte(CarteType.JOCKER, CarteValeur.ROUGE ))
        cartes.append(Carte(CarteType.JOCKER, CarteValeur.NOIR)) # TODO SHOULD NOT BE AS! NEED REFACTORING !!

        return cartes

    def get_carte_pos(self, carte: Carte) ->int:
        for (i, c) in enumerate(self.cartes):
            if(c.type == carte.type and c.valeur == carte.valeur ):
                return i
    
    def get_card_from_num(self, num: int) -> Carte:
        for c in (self.cartes):
            if(c.get_number2() == num ):
                return c
    def set_card_pos(self, card: Carte, to):
        self.cartes.pop(self.get_carte_pos(card))
        self.cartes.insert(to, card)


    
    def swap_cards(self, pos1, pos2):
        """swap position of two cards"""

        tmp = self.cartes[pos1]
        self.cartes[pos1] = self.cartes[pos2]
        self.cartes[pos2] = tmp

    def __str__(self) -> str:
        s = ""
        for i, c in enumerate(self.cartes):
            s += f"{i}. "+c.__str__()
        return s



