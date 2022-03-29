import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa(self):
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_lataus(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(self.maksukortti.saldo, 20)

    def test_nosto(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(self.maksukortti.saldo, 5)

    def test_nosto2(self):
        self.maksukortti.ota_rahaa(5)
        self.maksukortti.ota_rahaa(2)
        self.assertEqual(self.maksukortti.saldo, 3)

    def test_nosto3(self):
        self.maksukortti.ota_rahaa(5)
        self.maksukortti.ota_rahaa(10)
        self.assertEqual(self.maksukortti.saldo, 5)

    def test_nosto4(self):
        riittaako = self.maksukortti.ota_rahaa(5)
        self.assertEqual(riittaako, True)

    def test_nosto5(self):
        riittaako = self.maksukortti.ota_rahaa(12)
        self.assertEqual(riittaako, False)

    def test_saldo_euroissa(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")