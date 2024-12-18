import unittest
import mainRK2


class TestMainMethods(unittest.TestCase):
    def setUp(self):
        self.one_to_many = [(c.name, c.power, m.name)
                            for m in mainRK2.micrs
                            for c in mainRK2.comps
                            if c.id_micr == m.id]

        self.many_to_many_temp = [(m.name, mc.id_micr, mc.id_comp)
                                  for m in mainRK2.micrs
                                  for mc in mainRK2.micrs_comps
                                  if m.id == mc.id_micr]

        self.many_to_many = [(c.name, c.power, micr_name)
                             for micr_name, id_micr, id_comp in self.many_to_many_temp
                             for c in mainRK2.comps if c.id == id_comp]

    def test_func_1(self):
        result = mainRK2.func_1(self.one_to_many)
        reference = [('asus', 'intel 4'), ('asus 2', 'intel 4'), ('asus 3', 'intel 4')]
        self.assertEqual(result, reference)

    def test_func_2(self):
        result = mainRK2.func_2(self.one_to_many)
        reference = [('intel', 2000), ('intel 5', 3000), ('intel 4', 4000)]
        self.assertEqual(result, reference)

    def test_func_3(self):
        result = mainRK2.func_3(self.many_to_many)
        reference = [
            ('mac', 2000, 'intel'),
            ('mac', 2000, 'intel 2'),
            ('hp', 3000, 'intel 5'),
            ('hp', 3000, 'intel 9'),
            ('asus 2', 4000, 'intel 4'),
            ('asus', 5000, 'intel 4'),
            ('asus 3', 6000, 'intel 4'),
        ]
        self.assertEqual(result, reference)


if __name__ == '__main__':
    unittest.main()
