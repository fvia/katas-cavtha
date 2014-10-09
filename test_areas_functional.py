import unittest
import scripttest as st

python = 'python3'
script = '../areas.py'

env = st.TestFileEnvironment('./test-output')


class AreasCliTest(unittest.TestCase):

    def test_cuadrado5(self):
        result = env.run(python, script, "cuadrado", "5")
        self.assertEqual(result.stdout, u'25.0\n')

    def test_cuadrado0(self):
        result = env.run(python, script, "cuadrado", "0")
        self.assertEqual(result.stdout, u'0.0\n')


#    def test_cuadrado0(self):
#        self.assertEqual(AreaCuadrado(0), 0) 

#    def test_rectagulo_0(self):
#        self.assertEqual(AreaRectangulo(5, 0), 0)

#    def test_rectangulo_5_7_must_give_35(self):
#        self.assertEqual(AreaRectangulo(5, 7), 35)

#    def test_triangulo(self):
#        self.assertEqual(AreaTriangulo(4, 3), 6) 

#   def test_Triangulo_con_decimales(self):
#        self.assertEqual(AreaTriangulo(3.1, 4), 6.2) 

if __name__ == '__main__':
