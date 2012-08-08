
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

    def num_of_bits():
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


