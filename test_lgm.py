import unittest
import lgm as m


class TestGateLogic(unittest.TestCase):

    def test_burn_chip_from_schema(self):
        machine = m.LGM()
        schema1 = "(a1 a2)(b1 b2)(chip chip)(o1 o2)"
        result1 = {'burn1': ['(a1 a2)', '(b1 b2)', '(chip chip)', '(o1 o2)']}
        machine.burn('burn1', schema1)
        self.assertEqual(machine.allBurnt, result1)

    def test_burn_chip_from_schema_xtra(self):
        import lgm as m
        machine = m.LGM()
#test for logic
        and3 = "(z AND A B)(D AND z C) D"
        machine.logic('and3', and3)

        machine.dip('111', "(A B C)")
        self.assertEqual(machine.run('and3'), "1")

        machine.dip('101', "(A B C)")
        self.assertEqual(machine.run('and3'), "0")
#test for chip
        chip = "[(1 2 3), (A B C), and3, (4)]"
        machine.chip('chip1', chip)

        machine.dip('111', "(1 2 3)")
        print(machine.run('chip1'))
        self.assertEqual(machine.led('(4)'), "1")

        machine.dip('101', "(1 2 3)")
        print(machine.run('chip1'))
        self.assertEqual(machine.led('(4)'), "0")
#test for burned chip

        schema1 = "(1 2 3)(chip)(4)"
        result1 = {'burn1': ['(1 2 3)', '(chip)', '(4)']}
        machine.burn('burn1', schema1)
        self.assertEqual(machine.allBurnt, result1)

        self.assertEqual(machine.run("burn1", ('111')), '1')
        self.assertEqual(machine.run("burn1", ('101')), '0')

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

    def test_run_chip_from_allburnt2(self):
            machine = m.LGM()
            bit0 = "(x XOR A B)(z AND A B)(S XOR x Cx)(y AND x Cx)(Co OR z y) Co S"
            machine.logic('bit0', bit0)
            chip = "[(A0 B0 Co), (A B Cx), bit0, (Co S0)], [(A1 B1 Co), (A B Cx), bit0, (Co S1)], [(A2 B2 Co), (A B Cx), bit0, (Co S2)], [(A3 B3 Co), (A B Cx), bit0, (Co S3)]"
            machine.chip('chip1', chip)
            burn = "(A3 A2 A1 A0)(B3 B2 B1 B0)(Co)(chip1)(Co S3 S2 S1 S0)"
            machine.burn("burn", burn)

            self.assertEqual(machine.run("burn", ("0101",'1010','0')), '01111')
            self.assertEqual(machine.run("burn", ("0000",'0011','0')), '00011')
            self.assertEqual(machine.run("burn", ("1111",'0001','0')), '10000')

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