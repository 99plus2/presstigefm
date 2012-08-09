
def set_bytes_value(byte_set, value):
    """ Sets the value to several bytes (e.g. when they are counted as one
        value). The value per byte is determined by the binary representation
        of the value. Bits are filled up from right to left.
        byte_set = list(Byte), the available bytes to set
        value = int, the value to store """
    full_byte = (2**Byte.MAX_VALUE) - 1
    for byte in byte_set[::-1]:
        byte.value = value & full_byte
        value = value >> Byte.num_of_bits()

def get_bytes_value(byte_set):
    """ Gets the value of bytes which belong together. The value is determined
        by concatenating the binary representation of each byte value.
        byte_set = list(Byte), the bytes to get the value from
        returns int """
    value = 0
    for byte in byte_set:
        value = value << Byte.num_of_bits()
        value = value | byte.value
    return value

class Byte:

    MAX_VALUE = 64

    @staticmethod
    def num_of_bits():
        """ returns int, the number of bits needed to store the specified
            MAX_VALUE """
        counter = 0
        val = Byte.MAX_VALUE
        while val > 1:
            val = int(val / 2)
            counter += 1
        return counter

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value % Byte.MAX_VALUE

    def __init__(self):
        self._value = 0

    def __repr__(self):
        return repr(self.value)

class Register:

    def __init__(self, name, num_of_bytes, sign=True):
        self.name = name
        self.sign = sign
        self.byte_set = []
        for i in range(1, num_of_bytes + 1):
            self.byte_set.append(Byte())

    def __repr__(self):
        repr_string = self.name + ' '
        repr_string += '|+' if self.sign else '|-'
        for byte in self.byte_set:
            repr_string += '|' + repr(byte)
        repr_string += '|'
        return repr_string

class Memory:

    def __init__(self, size=4000):
        self.registers = {}
        for i in range(size):
            self.registers[i] = Register(name=repr(i), num_of_bytes=5)

class Environment:

    def __init__(self):
        self.reg_a = Register('A', 5)
        self.reg_x = Register('X', 5)
        self.reg_i1 = Register('I1', 2)
        self.reg_i2 = Register('I2', 2)
        self.reg_i3 = Register('I3', 2)
        self.reg_i4 = Register('I4', 2)
        self.reg_i5 = Register('I5', 2)
        self.reg_i6 = Register('I6', 2)
        self.reg_j = Register('J', 2)
        self.overflow = False
        self.equal = False
        self.less = False
        self.greater = False

    def execute(mix_file):
        """ Executes a given file written in mix-language.
            mix_file = string, path to the file """
        pass
