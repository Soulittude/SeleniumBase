# Turkish Language Test
from seleniumbase.translate.turkish import DurumTesti
DurumTesti.main(__name__, __file__)


class BenimTestSınıfım(DurumTesti):
    def test_exemple_1(self):
        self.aç("https://fr.wikipedia.org/wiki/")
        self.yazı_kontrol("Wikipédia")
        self.eleman_kontrol('[alt="Wikipédia"]')
        self.eğer_görünüyorsa_tıkla('button[aria-label="Fermer"]')
        self.js_yaz("#searchform input", "Crème brûlée")
        self.tıkla("#searchform button")
        self.yazı_kontrol("Crème brûlée", "#firstHeading")
        self.eleman_kontrol('img[alt*="Crème brûlée"]')
        self.js_yaz("#searchform input", "Jardin des Tuileries")
        self.tıkla("#searchform button")
        self.yazı_kontrol("Jardin des Tuileries", "#firstHeading")
        self.eleman_kontrol('img[alt*="Jardin des Tuileries"]')
        self.geri_dön()
        self.url_iceriyor_kontrol("brûlée")
        self.ileri_git()
        self.url_iceriyor_kontrol("Jardin")
