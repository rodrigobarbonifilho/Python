import clean_terminal


class A:
    vc = 123

    def __init__(self):
        pass

if __name__ == "__main__":
    a1 = A()
    a2 = A()

    A.vc = "Alterado"

    print(a1.vc)
    print(a2.vc)
    print(A.vc)
