from main import comprobarSatisfacible
from main import generar3CNF
from pysat.formula import CNF
from pysat.solvers import Minisat22
import unittest

class TestComprobarSatisfacible(unittest.TestCase):
    def test(self):
        x = 5
        n_max = 20
        rep = 1000

        for k in range(3,x+1):
            for n in range(1, n_max+1):
                for i in range(rep):
                    formula = generar3CNF(n, k)
                    satisfacible1, foo = comprobarSatisfacible(formula)
                    _cnf = CNF(from_clauses=formula)
                    with Minisat22(bootstrap_with=_cnf) as m:
                        satisfacible2 = m.solve()
                    self.assertEqual(satisfacible1, satisfacible2)

if __name__ == '__main__':
    unittest.main()

