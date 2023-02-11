import unittest

from crypto import *
from carte import *

class Testing(unittest.TestCase):
    def test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)

class TestKeyGenerator(unittest.TestCase):
    def test_init_pos(self):
        kg = KeyGenerator()
        jn = Carte(CarteType.JOCKER, CarteValeur.NOIR)
        jr = Carte(CarteType.JOCKER, CarteValeur.ROUGE)

        self.assertEqual(kg.cards.get_carte_pos(jn), 53)
        self.assertEqual(kg.cards.get_carte_pos(jr), 52)
        
    def test_step1(self):
        kg = KeyGenerator()
        jn = Carte(CarteType.JOCKER, CarteValeur.NOIR)
        self.assertEqual(kg.cards.get_carte_pos(jn), 53)
        kg.step_1()
        self.assertEqual(kg.cards.get_carte_pos(jn), 1)

        #2
        kg = KeyGenerator()
        kg.cards.set_card_pos(jn, 12)
        self.assertEqual(kg.cards.get_carte_pos(jn), 12)
        kg.step_1()
        self.assertEqual(kg.cards.get_carte_pos(jn), 13)
    

    def test_step2(self):
        kg = KeyGenerator()
        jr = Carte(CarteType.JOCKER, CarteValeur.ROUGE)
        self.assertEqual(kg.cards.get_carte_pos(jr), 52)
        kg.step_2()
        self.assertEqual(kg.cards.get_carte_pos(jr), 1)

        #2
        kg = KeyGenerator()
        kg.cards.set_card_pos(jr, 12)
        self.assertEqual(kg.cards.get_carte_pos(jr), 12)
        kg.step_2()
        self.assertEqual(kg.cards.get_carte_pos(jr), 14)

        #3
        kg = KeyGenerator()
        kg.cards.set_card_pos(jr, 53)
        self.assertEqual(kg.cards.get_carte_pos(jr), 53)
        kg.step_2()
        self.assertEqual(kg.cards.get_carte_pos(jr), 2)
    
    def test_step3(self):
        kg = KeyGenerator()
        jr = Carte(CarteType.JOCKER, CarteValeur.ROUGE)
        jn = Carte(CarteType.JOCKER, CarteValeur.NOIR)

        kg.cards.set_card_pos(jr, 20)
        kg.cards.set_card_pos(jn, 40)
        self.assertEqual(kg.cards.get_carte_pos(jr), 20)
        self.assertEqual(kg.cards.get_carte_pos(jn), 40)

        before = kg.cards.cartes
        print(kg.cards)

        kg.step_3()
        print(kg.cards)
        
        self.assertEqual(kg.cards.cartes[kg.cards.get_carte_pos(jr): kg.cards.get_carte_pos(jn) +1], before[20:41] )
        self.assertEqual(kg.cards.cartes[:kg.cards.get_carte_pos(jr):], before[41:] )
        self.assertEqual(kg.cards.cartes[kg.cards.get_carte_pos(jn)+1:], before[:20] )

    
    def test_step4(self):
        pass

        


if __name__ == '__main__':
    unittest.main()