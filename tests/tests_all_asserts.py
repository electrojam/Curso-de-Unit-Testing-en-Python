import unittest

class AllAssertsTests(unittest.TestCase):

    def test_assert_equal(self):
        self.assertEqual(10, 10)
        self.assertEqual("Hola", "Hola")

    def test_assert_true_or_false(self):
        self.assertTrue(True)
        self.assertFalse(False)

    def test_assert_raises(self):   # prueba para métodos que arrojen expeción
        with self.assertRaises(ValueError):
            int("No soy un número")

    def test_assert_in(self):   
        self.assertIn(10, [2, 4, 5, 10])    # prueba para mirar que un elemento esté dentro de una lista
        self.assertNotIn(3, [2, 4, 5, 10]) # prueba para mirar que un elemento esté dentro de una lista

    def test_assert_dicts(self):    # prueba para comparar listas y  data sets
        user = {"fist_name": "Luis", "last_name": "Martínez"}
        self.assertDictEqual(
            {"fist_name": "Luis", "last_name": "Martínez"},
            user
        )
        self.assertSetEqual(
            {1, 2, 3},
            {1, 2, 3},
        )