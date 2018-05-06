import unittest
import os
import filecmp

import hackassembler.assembler as assembler

class AssemblerTestCase(unittest.TestCase):
    def setUp(self):
        self.current_dir = os.path.dirname(__file__)
        self.tmp_dir = os.path.join(self.current_dir, "out_hack")

        if not os.path.isdir(self.tmp_dir):
            os.mkdir(self.tmp_dir)

    def test_assemble_Add_asm(self):
        infile = os.path.join(self.current_dir, "..", "add", "Add.asm")
        outfile = os.path.join(self.tmp_dir, "Add.hack")
        cmpfile = os.path.join(self.current_dir, "..", "add", "Add.hack")
        asmer = assembler.HackAssembler(infile, outfile)
        asmer.assemble()
        self.assertFileEqual(outfile, cmpfile, "Assemble Add.asm failed")

        os.remove(outfile)

    def test_assemble_MaxL_asm(self):
        infile = os.path.join(self.current_dir, "..", "max", "MaxL.asm")
        outfile = os.path.join(self.tmp_dir, "MaxL.hack")
        cmpfile = os.path.join(self.current_dir, "..", "max", "MaxL.hack")
        asmer = assembler.HackAssembler(infile, outfile)
        asmer.assemble()
        self.assertFileEqual(outfile, cmpfile, "Assemble MaxL.asm failed")

        os.remove(outfile)

    def test_assemble_RectL_asm(self):
        infile = os.path.join(self.current_dir, "..", "rect", "RectL.asm")
        outfile = os.path.join(self.tmp_dir, "RectL.hack")
        cmpfile = os.path.join(self.current_dir, "..", "rect", "RectL.hack")
        asmer = assembler.HackAssembler(infile, outfile)
        asmer.assemble()
        self.assertFileEqual(outfile, cmpfile, "Assemble RectL.asm failed")

        os.remove(outfile)

    def test_assemble_PongL_asm(self):
        infile = os.path.join(self.current_dir, "..", "pong", "PongL.asm")
        outfile = os.path.join(self.tmp_dir, "PongL.hack")
        cmpfile = os.path.join(self.current_dir, "..", "pong", "PongL.hack")
        asmer = assembler.HackAssembler(infile, outfile)
        asmer.assemble()
        self.assertFileEqual(outfile, cmpfile, "Assemble PongL.asm failed")

        os.remove(outfile)

    def tearDown(self):
        if not os.listdir(self.tmp_dir):
            os.rmdir(self.tmp_dir)

    def assertFileEqual(self, first, second, msg=None):
        """Assert that contents in two files are equal
        """
        self.assertTrue(isinstance(first, str),
                'First argument is not a string')
        self.assertTrue(isinstance(second, str),
                'Second argument is not a string')

        with open(first, 'r') as firstfile:
            with open(second, 'r') as secondfile:
                first_str = firstfile.read()
                second_str = secondfile.read()
                self.assertMultiLineEqual(first_str, second_str, msg)

if __name__ == '__main__':
    unittest.main()
