import types

class str_example:
    def __init__(self,func=None):
        self.name = 'str Ex 0'
        if func is not None:
            self.execute = types.MethodType(func,self)

    def execute(self):
        print(self.name)


def execute_replacement1(self):
    print(self.name+ " replacememt 1")


def execute_replacement2(self):
    print(self.name+ " replacememt 2")

if __name__=='__main__':
    st0=str_example()


    st1=str_example()

    st1=str_example(execute_replacement1)
    st1.name = "str Ex 1"

    st2=str_example(execute_replacement2)
    st2.name = "str Ex 2"

    st0.execute
    st1.execute
    st2.execute