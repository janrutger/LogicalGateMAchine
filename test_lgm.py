import unittest
import lgm as m


class TestGateLogic(unittest.TestCase):

    def test_burn_chip_from_schema(self):
        machine = m.LGM()
        schema1 = "(a1 a2)(b1 b2)(chip chip)(o1 o2)"
        result1 = {'burn1': ['(a1 a2)', '(b1 b2)', '(chip chip)', '(o1 o2)']}
        machine.burn('burn1', schema1)
        self.assertEqual(machine.allBurnt, result1)

    def test_run_chips_from_allBurnt(self):
        machine = m.LGM()
        and2 = "(c AND a b) c"
        machine.logic('and2', and2)
        and3 = "[(A B), (a b), and2, (d)], [(d C), (a b), and2, (D)]"
        machine.chip('and3', and3)


        burn = "(A B)(C)(and3)(D)"
        machine.burn('burn1', burn)
        self.assertEqual(machine.allBurnt, {'burn1': ['(A B)', '(C)', '(and3)', '(D)']})

        self.assertEqual(machine.run('burn1', ("11", "1")), "1")
        self.assertEqual(machine.run('burn1', ("01", "1")), "0")
        self.assertEqual(machine.run('burn1', ("11", "0")), "0")

    def test_make_chip_from_schema(self):
        machine = m.LGM()
        schema1 = "[(A1 A2 A3), (a b c), gate, (o1 o2 o3)], [(A1 A2 A3), (a b c), gate, (o1 o2 o3)]"
        result1 = {'CHIP1': [['(A1 A2 A3)', '(a b c)', 'gate', '(o1 o2 o3)'], ['(A1 A2 A3)', '(a b c)', 'gate', '(o1 o2 o3)']]}
        machine.chip('CHIP1', schema1)
        self.assertEqual(machine.allChips, result1)

    def test_run_chip_from_allChips(self):
        machine = m.LGM()
        and2 = "(c AND a b) c"
        machine.logic('and2', and2)
        machine.dip('111', "(A B C)")

        CHIP = "[(A B), (a b), and2, (d)], [(d C), (a b), and2, (D)]"
        machine.chip('CHIP', CHIP)
        machine.run('CHIP')
        self.assertEqual(machine.led("(D)"), '1')


    def test_run_logic_from_allLogic(self):
        machine = m.LGM()

        schema1 = "(c AND a b) c"
        machine.logic('LGM1', schema1)

        machine.dip('11', "(a b)")
        self.assertEqual(machine.run('LGM1'), '1')
        machine.dip('10', "(a b)")
        self.assertEqual(machine.run('LGM1'), '0')


        schema2 = "(c AND a b)(x NOT c) c x"
        machine.logic('LGM2', schema2)

        machine.dip('11', "(a b)")
        self.assertEqual(machine.run('LGM2'), '10')
        machine.dip('01', "(a b)")
        self.assertEqual(machine.run('LGM2'), '01')

        self.assertEqual(machine.run('niks'), 'Unkown or Invalid')

    
    def test_DIP_input_values(self):
        machine = m.LGM()
        machine.dip('10', "(a b)")
        self.assertEqual(machine.allPins, {'a': '1', 'b': '0'})
        machine.dip('01', "(a1 b)")
        self.assertEqual(machine.allPins, {'a': '1','a1': '0', 'b': '1'})

    def test_LED_output_vaules(self):
        machine = m.LGM()
        machine.dip('101', "(a b c)")
        self.assertEqual(machine.led("(a b)"), '10')
        self.assertEqual(machine.led("(c b)"), '10')


    def test_make_logic_from_schema(self):
        machine = m.LGM()

        schema1 = "(c AND a b) c"
        result1 = {'LGM1': [('c', 'AND', 'a', 'b'), ('c',)]}
        machine.logic('LGM1', schema1)
        self.assertEqual(machine.allLogic, result1)

        schema2 = "(c AND a b)(x NOT c) c"
        result2 = {'LGM1': [('c', 'AND', 'a', 'b'), ('x', 'NOT', 'c'), ('c',)]}
        machine.logic('LGM1', schema2)
        self.assertEqual(machine.allLogic, result2)

        machine.logic('LGM1', schema1)
        machine.logic('LGM2', schema2)
        result3 = {'LGM1': [('c', 'AND', 'a', 'b'), ('c',)], 'LGM2': [('c', 'AND', 'a', 'b'), ('x', 'NOT', 'c'), ('c',)]}
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




if __name__ == '__main__':
    unittest.main()