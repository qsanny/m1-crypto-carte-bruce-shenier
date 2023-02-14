import unittest

from keygen import *
from carte import *
from coder import *

class TestKeyGenerator(unittest.TestCase):
    def test_init_pos(self):
        kg = KeyGenerator()
        jn = Carte(CarteType.JOCKER, CarteValeur.NOIR)
        jr = Carte(CarteType.JOCKER, CarteValeur.ROUGE)

        self.assertEqual(kg.deck.get_carte_pos(jn), 53)
        self.assertEqual(kg.deck.get_carte_pos(jr), 52)
        
    def test_step1(self):
        kg = KeyGenerator()
        jn = Carte(CarteType.JOCKER, CarteValeur.NOIR)
        self.assertEqual(kg.deck.get_carte_pos(jn), 53)
        kg.step_1()
        self.assertEqual(kg.deck.get_carte_pos(jn), 1)

        #2
        kg = KeyGenerator()
        kg.deck.set_card_pos(jn, 12)
        self.assertEqual(kg.deck.get_carte_pos(jn), 12)
        kg.step_1()
        self.assertEqual(kg.deck.get_carte_pos(jn), 13)

        #3
        kg = KeyGenerator()
        kg.deck.set_card_pos(jn, 0)
        self.assertEqual(kg.deck.get_carte_pos(jn), 0)
        kg.step_1()
        self.assertEqual(kg.deck.get_carte_pos(jn), 1)
    

    def test_step2(self):
        kg = KeyGenerator()
        jr = Carte(CarteType.JOCKER, CarteValeur.ROUGE)
        self.assertEqual(kg.deck.get_carte_pos(jr), 52)
        kg.step_2()
        self.assertEqual(kg.deck.get_carte_pos(jr), 1)

        #2
        kg = KeyGenerator()
        kg.deck.set_card_pos(jr, 12)
        self.assertEqual(kg.deck.get_carte_pos(jr), 12)
        kg.step_2()
        self.assertEqual(kg.deck.get_carte_pos(jr), 14)

        #3
        kg = KeyGenerator()
        kg.deck.set_card_pos(jr, 53)
        self.assertEqual(kg.deck.get_carte_pos(jr), 53)
        kg.step_2()
        self.assertEqual(kg.deck.get_carte_pos(jr), 2)

        #3
        kg = KeyGenerator()
        kg.deck.set_card_pos(jr, 0)
        self.assertEqual(kg.deck.get_carte_pos(jr), 0)
        kg.step_2()
        self.assertEqual(kg.deck.get_carte_pos(jr), 2)
    
    def test_step3(self):
        kg = KeyGenerator()
        jr = Carte(CarteType.JOCKER, CarteValeur.ROUGE)
        jn = Carte(CarteType.JOCKER, CarteValeur.NOIR)

        kg.deck.set_card_pos(jr, 20)
        kg.deck.set_card_pos(jn, 40)
        self.assertEqual(kg.deck.get_carte_pos(jr), 20)
        self.assertEqual(kg.deck.get_carte_pos(jn), 40)

        before = kg.deck.cartes
        kg.step_3()
        
        self.assertEqual(kg.deck.cartes[kg.deck.get_carte_pos(jr): kg.deck.get_carte_pos(jn) +1], before[20:41] )
        self.assertEqual(kg.deck.cartes[:kg.deck.get_carte_pos(jr):], before[41:] )
        self.assertEqual(kg.deck.cartes[kg.deck.get_carte_pos(jn)+1:], before[:20] )

    
    def test_step4(self):
        kg = KeyGenerator()
        vt = Carte(CarteType.TREFLE, CarteValeur.VALET)
        kg.deck.set_card_pos(vt, 53)
        self.assertEqual(kg.deck.cartes[-1].get_number(), 11 )

        before = kg.deck.cartes
        kg.step_4()

        self.assertEqual(kg.deck.cartes[42:53], before[:11] )
        self.assertEqual(kg.deck.cartes[:42], before[11:53] )
        self.assertEqual(kg.deck.cartes[-1], before[-1] )
        self.assertEqual(kg.deck.cartes[-1], vt )
    
    def test_step5(self):
        kg = KeyGenerator()
        vt = Carte(CarteType.TREFLE, CarteValeur.VALET)
        ap = Carte(CarteType.PIQUE, CarteValeur.AS)
        kg.deck.set_card_pos(vt, 0)
        kg.deck.set_card_pos(ap, 11)

        self.assertEqual(kg.deck.cartes[0].get_number(), 11 )
        self.assertEqual(kg.deck.cartes[11].get_number(), 40 )

        m = kg.step_5()
        self.assertEqual(m, 14) # 14 = 40 - 26
    
    def test_get_key(self):
        kg = KeyGenerator()
        k = kg.get_key()
        print(k)
    
    def test_generate_key(self):
        kg = KeyGenerator()
        k = kg.generate_key(5)
        print(k)
    
    def test_encode(self):
        msg = "BONJOUR"
        encoder = Encoder(KeyGenerator())
        encoded_msg = encoder.encode(msg)
        self.assertEqual(encoded_msg, "HLBMOFX")
    
    def test_decode(self):
        msg = "HLBMOFX"
        decoder = Decoder(KeyGenerator())
        decoded_msg = decoder.decode(msg)
        self.assertEqual(decoded_msg, "BONJOUR")


        



if __name__ == '__main__':
    unittest.main()