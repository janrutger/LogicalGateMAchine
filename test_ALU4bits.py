import unittest
import sample_ALU4bits

class TestMyScript(unittest.TestCase):
    def test_ALU_4bits(self):
        self.assertEqual(sample_ALU4bits.machine.run("ALU", ("1010",'0101','0000')), '00000')   # AND  function Cout R3 R2 R1 R0
        self.assertEqual(sample_ALU4bits.machine.run("ALU", ("1010",'0101','1000')), '01111')   # OR   function
        self.assertEqual(sample_ALU4bits.machine.run("ALU", ("1010",'0101','1011')), '11111')   # NAND function
        self.assertEqual(sample_ALU4bits.machine.run("ALU", ("1010",'0101','0011')), '10000')   # NOR  function
        self.assertEqual(sample_ALU4bits.machine.run("ALU", ("1010",'0101','0100')), '01111')   # ADD  function (10 + 5)
        self.assertEqual(sample_ALU4bits.machine.run("ALU", ("1011",'0101','0100')), '10000')   # ADD  function and Carry (11 + 5)
        self.assertEqual(sample_ALU4bits.machine.run("ALU", ("1010",'0101','0101')), '10101')   # SUB  function (10 -  5)
        self.assertEqual(sample_ALU4bits.machine.run("ALU", ("0101",'1010','0101')), '01011')   # SUB  function ( 5 - 10)
        self.assertEqual(sample_ALU4bits.machine.run("ALU", ("0101",'0101','0101')), '10000')   # SUB  function ( 5 -  5)


        self.assertEqual(sample_ALU4bits.machine.run("ALU", ("1101",'0110','0000')), '10100')   # AND  function Cout R3 R2 R1 R0
        self.assertEqual(sample_ALU4bits.machine.run("ALU", ("1101",'0110','1000')), '11111')   # OR   function
        self.assertEqual(sample_ALU4bits.machine.run("ALU", ("1101",'0110','1011')), '01011')   # NAND function
        self.assertEqual(sample_ALU4bits.machine.run("ALU", ("1101",'0110','0011')), '00000')   # NOR  function


if __name__ == '__main__':
    unittest.main()


# Truth table
# ---------------------
# | S1 | S2 | An | Bn |
# ---------------------
# |  0 |  0 |  0 |  0 |   AND
# |  1 |  0 |  0 |  0 |   OR
# |  1 |  0 |  1 |  1 |   NAND
# |  0 |  0 |  1 |  1 |   NOR 
# |  x |  1 |  0 |  0 |   ADD 
# |  x |  1 |  0 |  1 |   SUB
# ---------------------