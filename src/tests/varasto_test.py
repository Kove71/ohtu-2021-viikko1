import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.neg_varasto = Varasto(-1, -2)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_negatiivinen_tilavuus(self):
        self.assertAlmostEqual(self.neg_varasto.tilavuus, 0)

    def test_negatiivinen_saldo(self):
        self.assertAlmostEqual(self.neg_varasto.saldo, 0)

    def test_alkusaldo_isompi_kuin_tilavuus(self):
        varasto_saldo_suurempi = Varasto(1, 2)
        self.assertAlmostEqual(varasto_saldo_suurempi.saldo, varasto_saldo_suurempi.tilavuus)

    def test_lisaa_varastoon_neg_maara(self):
        temp_varasto = Varasto(10)
        temp_varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(temp_varasto.saldo, 0)
    
    def test_lisaa_varastoon_enemman_kuin_mahtuu(self):
        temp_varasto = Varasto(5)
        temp_varasto.lisaa_varastoon(10)
        self.assertAlmostEqual(temp_varasto.saldo, temp_varasto.tilavuus)
    
    def test_ota_varastosta_neg(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-5), 0)
    
    def test_ota_varastosta_enemman_kuin_saldo_palauttaa_oikein(self):
        temp_varasto = Varasto(10, 5)
        self.assertAlmostEqual(temp_varasto.ota_varastosta(10), 5)
    
    def test_ota_varastosta_enemman_kuin_saldo_ja_saldo_oikein(self):
        temp_varasto = Varasto(10, 5)
        temp_varasto.ota_varastosta(10)
        self.assertAlmostEqual(temp_varasto.saldo, 0)
    
    # def test_merkkijono_oikein(self):
    #     temp_varasto = Varasto(10, 5)
    #     merkkijono = "saldo = 5, vielä tilaa 5"
    #     self.assertEqual(merkkijono, str(temp_varasto))
    
    def test_merkkijono_oikein_rikki(self):
        temp_varasto = Varasto(10, 2)
        merkkijono = "saldo = 5, vielä tilaa 5"
        self.assertEqual(merkkijono, str(temp_varasto))
