import unittest

from main.python.bestellungen_auswerten import filter_content, get_content_from_file, get_share, get_sum


class MyTestCase(unittest.TestCase):
    def test_get_dict(self):
        content = get_content_from_file('../resources/bestellungen.csv')

        self.assertEqual(len(content), 80, "Anzahl der Datensätze")

    def test_duschgel_zaehlen(self):
        content = get_content_from_file('../resources/bestellungen.csv')
        content_gefiltert = filter_content(content, "Produktname", "Duschgel")

        self.assertEqual(len(content_gefiltert), 14)

    def test_get_share(self):
        content = get_content_from_file('../resources/bestellungen.csv')
        content_gefiltert = filter_content(content, "Produktname", "Duschgel")
        percentage = get_share(content, content_gefiltert)

        self.assertEqual(percentage, 17.5)

    def test_get_sum(self):
        content = get_content_from_file('../resources/bestellungen.csv')
        content_vorname_gefiltert = filter_content(content, "Vorname", "Sibylla")
        content_nachname_gefiltert = filter_content(content_vorname_gefiltert, "Nachname", "Vogt")
        summe = get_sum(content_nachname_gefiltert)

        self.assertEqual(summe, 49.02)


if __name__ == '__main__':
    unittest.main()
