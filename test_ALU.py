import unittest
import lgm as m


class TestGateLogic(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.machine = m.LGM()
        ## All needed logic
        plexer21 = "(z NOT X)(y AND D1 X)(x AND D0 z)(O OR x y) O"
        cls.machine.logic('plexer21', plexer21)
        plexer31 = "(z NOT X1)(y AND D1 X1)(x AND D0 z)(r OR x y)(z1 NOT X2)(y1 AND D2 X2)(x1 AND r z1)(O OR x1 y1) O"
        cls.machine.logic('plexer31', plexer31)
        adder = "(x XOR A B)(z AND A B)(S XOR x Cx)(y AND x Cx)(Co OR z y) Co S"
        cls.machine.logic('adder', adder)
        and2 = "(c AND a b) c"
        cls.machine.logic('and2', and2)
        or2 = "(c OR a b) c"
        cls.machine.logic('or2', or2)
        not1 = "(b NOT a) b"
        cls.machine.logic('not1', not1)

        ## Glue the logic to on bit ALU
        ALU = "[(A0), (a), not1, (An)], [(B0), (a), not1, (Bn)], [(A0 An Anot), (D0 D1 X), plexer21, (Ain)], [(B0 Bn Bnot), (D0 D1 X), plexer21, (Bin)], [(Ain Bin Cin), (A B Cx), adder, (Cout r2)], [(Ain Bin), (a b), or2, (r1)], [(Ain Bin), (a b), and2, (r0)], [(r0 r1 r2 S1 S2), (D0 D1 D2 X1 X2), plexer31, (O0)]"
        cls.machine.chip('ALU', ALU)


    def test_AND_gate(self):
        self.machine.dip('000', "(Anot Bnot Cin)")
        self.machine.dip('00', "(S2 S1)")


        self.machine.dip('00', "(A0 B0)")
        self.machine.run('ALU')
        self.assertEqual(self.machine.led('(O0)'), "0")

        self.machine.dip('01', "(A0 B0)")
        self.machine.run('ALU')
        self.assertEqual(self.machine.led('(O0)'), "0")

        self.machine.dip('10', "(A0 B0)")
        self.machine.run('ALU')
        self.assertEqual(self.machine.led('(O0)'), "0")

        self.machine.dip('11', "(A0 B0)")
        self.machine.run('ALU')
        self.assertEqual(self.machine.led('(O0)'), "1")

    def test_NAND_gate(self):
        self.machine.dip('110', "(Anot Bnot Cin)")
        self.machine.dip('01', "(S2 S1)")


        self.machine.dip('00', "(A0 B0)")
        self.machine.run('ALU')
        self.assertEqual(self.machine.led('(O0)'), "1")

        self.machine.dip('01', "(A0 B0)")
        self.machine.run('ALU')
        self.assertEqual(self.machine.led('(O0)'), "1")

        self.machine.dip('10', "(A0 B0)")
        self.machine.run('ALU')
        self.assertEqual(self.machine.led('(O0)'), "1")

        self.machine.dip('11', "(A0 B0)")
        self.machine.run('ALU')
        self.assertEqual(self.machine.led('(O0)'), "0")

    def test_OR_gate(self):
        self.machine.dip('000', "(Anot Bnot Cin)")
        self.machine.dip('01', "(S2 S1)")


        self.machine.dip('00', "(A0 B0)")
        self.machine.run('ALU')
        self.assertEqual(self.machine.led('(O0)'), "0")

        self.machine.dip('01', "(A0 B0)")
        self.machine.run('ALU')
        self.assertEqual(self.machine.led('(O0)'), "1")

        self.machine.dip('10', "(A0 B0)")
        self.machine.run('ALU')
        self.assertEqual(self.machine.led('(O0)'), "1")

        self.machine.dip('11', "(A0 B0)")
        self.machine.run('ALU')
        self.assertEqual(self.machine.led('(O0)'), "1")

    def test_NOR_gate(self):
        self.machine.dip('110', "(Anot Bnot Cin)")
        self.machine.dip('00', "(S2 S1)")


        self.machine.dip('00', "(A0 B0)")
        self.machine.run('ALU')
        self.assertEqual(self.machine.led('(O0)'), "1")

        self.machine.dip('01', "(A0 B0)")
        self.machine.run('ALU')
        self.assertEqual(self.machine.led('(O0)'), "0")

        self.machine.dip('10', "(A0 B0)")
        self.machine.run('ALU')
        self.assertEqual(self.machine.led('(O0)'), "0")

        self.machine.dip('11', "(A0 B0)")
        self.machine.run('ALU')
        self.assertEqual(self.machine.led('(O0)'), "0")


    def test_ADDER_gate(self):
        self.machine.dip('000', "(Anot Bnot Cin)")
        self.machine.dip('11', "(S2 S1)")


        self.machine.dip('000', "(A0 B0 Cin)")
        self.machine.run('ALU')
        self.assertEqual(self.machine.led('(O0 Cout)'), "00")

        self.machine.dip('001', "(A0 B0 Cin)")
        self.machine.run('ALU')
        self.assertEqual(self.machine.led('(O0 Cout)'), "10")

        self.machine.dip('010', "(A0 B0 Cin)")
        self.machine.run('ALU')
        self.assertEqual(self.machine.led('(O0 Cout)'), "10")

        self.machine.dip('011', "(A0 B0 Cin)")
        self.machine.run('ALU')
        self.assertEqual(self.machine.led('(O0 Cout)'), "01")

        self.machine.dip('100', "(A0 B0 Cin)")
        self.machine.run('ALU')
        self.assertEqual(self.machine.led('(O0 Cout)'), "10")

        self.machine.dip('101', "(A0 B0 Cin)")
        self.machine.run('ALU')
        self.assertEqual(self.machine.led('(O0 Cout)'), "01")

        self.machine.dip('110', "(A0 B0 Cin)")
        self.machine.run('ALU')
        self.assertEqual(self.machine.led('(O0 Cout)'), "01")

        self.machine.dip('111', "(A0 B0 Cin)")
        self.machine.run('ALU')
        self.assertEqual(self.machine.led('(O0 Cout)'), "11")




if __name__ == '__main__':
    unittest.main()
