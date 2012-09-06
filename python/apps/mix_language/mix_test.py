import unittest
import mix

class TestFirstOrderMethods(unittest.TestCase):

    def test_bytes_setter_getter(self):
        byte_set = [mix.Byte(), mix.Byte()]
        mix.set_bytes_value(byte_set, 30)
        self.assertEqual(0, byte_set[0].value)
        self.assertEqual(30, byte_set[1].value)
        self.assertEqual(30, mix.get_bytes_value(byte_set))

        mix.set_bytes_value(byte_set, 1234)
        self.assertEqual(19, byte_set[0].value)
        self.assertEqual(18, byte_set[1].value)
        self.assertEqual(1234, mix.get_bytes_value(byte_set))

class TestByte(unittest.TestCase):

    def test_num_of_bits(self):
        b = mix.Byte()
        self.assertEqual(6, mix.Byte.num_of_bits())

class TestInstructions(unittest.TestCase):

    pass

if __name__ == '__main__':
    unittest.main()
