import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_paate_luotu(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_alkukassa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_ei_myyntia_alussa(self):
        myynti = self.kassapaate.edulliset + self.kassapaate.maukkaat
        self.assertEqual(myynti, 0)

    def test_syo_edullisesti_kateisella(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_syo_edullisesti_kateisella_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250), 10)

    def test_syo_edullisesti_kateisella_myynti(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset, 2)

    def test_syo_maukkaasti_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_syo_maukkaasti_kateisella_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_syo_maukkaasti_kateisella_myynti(self):
        self.kassapaate.syo_maukkaasti_kateisella(5000)
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 2)

    def test_syo_edullisesti_kateisella2(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_edullisesti_kateisella_vaihtoraha2(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def test_syo_edullisesti_kateisella_myynti2(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_maukkaasti_kateisella2(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kateisella_vaihtoraha2(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)

    def test_syo_maukkaasti_kateisella_myynti2(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kortilla(self):
        kortti = Maksukortti(1000)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), True)
        
    def test_syo_edullisesti_kortilla2(self):
        kortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)

    def test_syo_edullisesti_kortilla3(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 760)

    def test_syo_edullisesti_kortilla4(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kortilla5(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kortilla(self):
        kortti = Maksukortti(1000)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), True)
        
    def test_syo_maukkaasti_kortilla2(self):
        kortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)

    def test_syo_maukkaasti_kortilla3(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 600)

    def test_syo_maukkaasti_kortilla4(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaat_kortilla5(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortin_lataus(self):
        kortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(kortti=kortti, summa=1000)
        self.assertEqual(kortti.saldo, 1100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_kortin_lataus2(self):
        kortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(kortti=kortti, summa=-1000)
        self.assertEqual(kortti.saldo, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)