class Products:
    def __init__(self):
        self.suv = 10000
        self.coffe = 1000 # kg
        self.sut = 10000


    def make_latte(self):
        if self.sut >=30 and self.suv >= 100 and self.coffe >= 20:
            self.suv-= 100
            self.coffe -= 20
            self.sut -=30
        else:
            print('Mahsulotlarimiz yetarli emas')

    def make_capucino(self):
        if self.sut >= 100 and self.coffe >= 40 and self.sut >= 50:
            self.suv -= 100
            self.coffe -= 40
            self.sut  -= 50
        else:
            print('capucino uchun mahsulotimiz yetarli emas! ')

    def make_esperasso(self):
        if self.sut >= 40 and self.suv >= 100 and self.coffe >= 50:
            self.suv -=100
            self.sut -= 40
            self.coffe -= 50
        else:
            print('esperasso uchun mahsulotimiz yetarli emas: ')