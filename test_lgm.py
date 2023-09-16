import unittest
import lgm as m


class TestGateLogic(unittest.TestCase):
    
    def test_set_input_values(self):
        machine = m.LGM()
        machine.dip('10', "(a b)")
        self.assertEqual(machine.allPins, {'a': '1', 'b': '0'})
        machine.dip('01', "(a1 b)")
        self.assertEqual(machine.allPins, {'a': '1','a1': '0', 'b': '1'})

    def test_led_output_vaules(self):
        machine = m.LGM()
        machine.dip('101', "(a b c)")
        self.assertEqual(machine.led("(a b)"), '10')
        self.assertEqual(machine.led("(c b)"), '10')


    def test_make_logic_from_schema(self):
        machine = m.LGM()

        schema1 = "(c AND a b) c"
        result1 = {'LGC1': [('c', 'AND', 'a', 'b'), ('c',)]}
        machine.logic('LGC1', schema1)
        self.assertEqual(machine.allLogic, result1)

        schema2 = "(c AND a b)(x NOT c) c"
        result2 = {'LGC1': [('c', 'AND', 'a', 'b'), ('x', 'NOT', 'c'), ('c',)]}
        machine.logic('LGC1', schema2)
        self.assertEqual(machine.allLogic, result2)

        machine.logic('LGC1', schema1)
        machine.logic('LGC2', schema2)
        result3 = {'LGC1': [('c', 'AND', 'a', 'b'), ('c',)], 'LGC2': [('c', 'AND', 'a', 'b'), ('x', 'NOT', 'c'), ('c',)]}
        self.assertEqual(machine.allLogic, result3)



    def test_AND(self):
        machine = m.LGM()
        self.assertEqual(machine.gate('AND', 0, 0), 0)
        self.assertEqual(machine.gate('AND', 0, 1), 0)
        self.assertEqual(machine.gate('AND', 1, 0), 0)
        self.assertEqual(machine.gate('AND', 1, 1), 1)

    def test_OR(self):
        machine = m.LGM()
        self.assertEqual(machine.gate('OR', 0, 0), 0)
        self.assertEqual(machine.gate('OR', 0, 1), 1)
        self.assertEqual(machine.gate('OR', 1, 0), 1)
        self.assertEqual(machine.gate('OR', 1, 1), 1)

    def test_XOR(self):
        machine = m.LGM()
        self.assertEqual(machine.gate('XOR', 0, 0), 0)
        self.assertEqual(machine.gate('XOR', 0, 1), 1)
        self.assertEqual(machine.gate('XOR', 1, 0), 1)
        self.assertEqual(machine.gate('XOR', 1, 1), 0)

    def test_NOT(self):
        machine = m.LGM()
        self.assertEqual(machine.gate('NOT', 0), 1)
        self.assertEqual(machine.gate('NOT', 1), 0)


    def test_run_logic_from_allLogic(self):
        machine = m.LGM()

        schema1 = "(c AND a b) c"
        machine.logic('LGC1', schema1)

        machine.dip('11', "(a b)")
        self.assertEqual(machine.run('LGC1'), '1')
        machine.dip('10', "(a b)")
        self.assertEqual(machine.run('LGC1'), '0')


        schema2 = "(c AND a b)(x NOT c) c x"
        machine.logic('LGC2', schema2)

        machine.dip('11', "(a b)")
        self.assertEqual(machine.run('LGC2'), '10')
        machine.dip('01', "(a b)")
        self.assertEqual(machine.run('LGC2'), '01')







if __name__ == '__main__':
    unittest.main()