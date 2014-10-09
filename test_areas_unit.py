import unittest

from areas import AreaCuadrado, AreaTriangulo, AreaRectangulo


class AreasTest(unittest.TestCase):
  
    def test_cuadrado5(self):
        self.assertEqual(AreaCuadrado(5), 25)

    def test_cuadrado0(self):
        self.assertEqual(AreaCuadrado(0), 0)

    def test_rectagulo_0(self):
        self.assertEqual(AreaRectangulo(5, 0), 0)

    def test_rectangulo_5_7_must_give_35(self):
        self.assertEqual(AreaRectangulo(5, 7), 35)

    def test_triangulo(self):
        self.assertEqual(AreaTriangulo(4, 3), 6)

    def test_Triangulo_con_decimales(self):
        self.assertEqual(AreaTriangulo(3.1, 4), 6.2)

if __name__ == '__main__':
    unittest.main()
