class FourCal:
    def setData(self, _first, _second):
        self.first = _first
        self.second = _second

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second

#########################################


class FourCalChild(FourCal):
    def pow(self):
        return self.first ** self.second


def chap1():
    a = FourCal()
    print(type(a))


def chap2():
    a = FourCal()
    a.setData(4, 2)
    print(a)
    print(a.first, a.second)


def chap3():
    a = FourCal()
    b = FourCal()
    a.setData(4, 2)
    b.setData(3, 8)
    print(a.add(), a.sub(), a.mul(), a.div())
    print(b.add(), b.sub(), b.mul(), b.div())


def chap4():
    a = FourCalChild()
    a.setData(4, 2)
    print(a.pow())


def main():
    chap4()

main()
