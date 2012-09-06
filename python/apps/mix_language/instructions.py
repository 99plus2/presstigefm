
class Instruction:

    def __init__(self, op_code=0, f=0, i=0, address=0, execution_time=0):
        self.op_code = op_code
        self.f = f
        self.i = i
        self.address = address
        self.execution_time = execution_time

    def __repr__(self):
        return 'address: {0}, i: {1}, f: {2}, op_code: {3} - time: {4}'.format(self.address, 
                self.i, self.f, self.op_code, self.execution_time)

    def execute(self, env):
        """ Executes this command.
            env = mix.Environment, the environment to execute on """
        raise NotImplementedError('Implement Instruction.execute(..)')

class NOP(Instruction):
    """ No operation. """

    def __init__(self, *args):
        super().__init__(op_code=0, execution_time=1, *args)

    def execute(self, env):
        pass

class ADD(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=1, execution_time=2, *args)

class SUB(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=2, execution_time=2, *args)

class MUL(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=3, execution_time=10, *args)

class DIV(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=4, execution_time=12, *args)

class NUM(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=5, execution_time=10, *args)

class SLA(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=6, execution_time=2, *args)

class MOVE(Instruction):

    def __init__(self, *args):
        # XXX: execution_time depends on f
        super().__init__(op_code=7, execution_time=1, *args)

class LDA(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=8, execution_time=2, *args)

class LD1(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=9, execution_time=2, *args)

class LD2(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=10, execution_time=2, *args)

class LD3(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=11, execution_time=2, *args)

class LD4(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=12, execution_time=2, *args)

class LD5(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=13, execution_time=2, *args)

class LD6(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=14, execution_time=2, *args)

class LDX(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=15, execution_time=2, *args)

class LDAN(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=16, execution_time=2, *args)

class LD1N(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=17, execution_time=2, *args)

class LD2N(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=18, execution_time=2, *args)

class LD3N(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=19, execution_time=2, *args)

class LD4N(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=20, execution_time=2, *args)

class LD5N(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=21, execution_time=2, *args)

class LD6N(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=22, execution_time=2, *args)

class LDXN(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=23, execution_time=2, *args)

class STA(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=24, execution_time=2, *args)

class ST1(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=25, execution_time=2, *args)

class ST2(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=26, execution_time=2, *args)

class ST3(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=27, execution_time=2, *args)

class ST4(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=28, execution_time=2, *args)

class ST5(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=29, execution_time=2, *args)

class ST6(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=30, execution_time=2, *args)

class STX(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=31, execution_time=2, *args)

class STJ(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=32, execution_time=2, *args)

class STZ(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=33, execution_time=2, *args)

class JBUS(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=34, execution_time=1, *args)

class IOC(Instruction):

    def __init__(self, *args):
        # XXX: execution_time depends on T
        super().__init__(op_code=35, execution_time=1, *args)

class IN(Instruction):

    def __init__(self, *args):
        # XXX: execution_time depends on T
        super().__init__(op_code=36, execution_time=1, *args)

class OUT(Instruction):

    def __init__(self, *args):
        # XXX: execution_time depends on T
        super().__init__(op_code=37, execution_time=1, *args)

class JRED(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=38, execution_time=1, *args)

class JMP(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=39, execution_time=1, *args)

class JA(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=40, execution_time=1, *args)

class J1(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=41, execution_time=1, *args)

class J2(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=42, execution_time=1, *args)

class J3(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=43, execution_time=1, *args)

class J4(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=44, execution_time=1, *args)

class J5(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=45, execution_time=1, *args)

class J6(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=46, execution_time=1, *args)

class JX(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=47, execution_time=1, *args)

class INCA(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=48, execution_time=1, *args)

class INC1(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=49, execution_time=1, *args)

class INC2(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=50, execution_time=1, *args)

class INC3(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=51, execution_time=1, *args)

class INC4(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=52, execution_time=1, *args)

class INC5(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=53, execution_time=1, *args)

class INC6(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=54, execution_time=1, *args)

class INCX(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=55, execution_time=1, *args)

class CMPA(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=56, execution_time=2, *args)

class CMP1(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=57, execution_time=2, *args)

class CMP2(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=58, execution_time=2, *args)

class CMP3(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=59, execution_time=2, *args)

class CMP4(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=60, execution_time=2, *args)

class CMP5(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=61, execution_time=2, *args)

class CMP6(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=62, execution_time=2, *args)

class CMPX(Instruction):

    def __init__(self, *args):
        super().__init__(op_code=63, execution_time=2, *args)


i = NOP()
print(i)
