def dec_test():
    hey()
    test()
    pass


def ruban(func):
    print("ruban")
    func()

    def hello():
        print("hello")

    return hello

def multiplicateur(nb):
    def decorateur(func):
        def new_func():
            for i in range(nb):
                func()
            return
        return new_func
    return decorateur



@ruban
def hey():
    print("hey")

@multiplicateur(5)
def test():
    print("test")

