from products import Products

t = Products()

class Task:
    def __init__(self):
        self.coins = 0
        self.cost_latte = 3000
        self.cost_esperasso = 5000
        self.cost_capuccino = 7000
        self.menu = ['latte', 'esperasso', 'capuccino']

    def Menuni_chiqar(self):
        print(f"latte : {self.cost_latte} so'm \nesperasso : {self.cost_esperasso} so'm \ncapuccino {self.cost_capuccino} so'm")

    def enter_coins(self):
        try:
            a = int(input('pulni kiriting (somda) :  '))
            self.coins+=a
        except:
            pass

    def tanlang(self):
        global sora, bool
        bool =False
        sora = input('qaysi ichimlikni hohlaysiz? birini kiriting (latte / esperasso / capuccino ) : ').lower()
        if sora not in self.menu:
            while bool == False:
                print('hato malumot kiritdingiz. Qayyta urunib koring! ')
                sora = input('qaysi ichimlikni hohlaysiz? birini kiriting (latte / esperasso / capuccino ) : ').lower()
                if sora in self.menu:
                    bool = True

    def give_drinking(self):

        if sora == 'latte':
            if self.coins >= self.cost_latte:
                self.coins -=self.cost_latte
                t.make_latte()
                print('Marhamat sizning latte ingiz iching va zavq oling ☺️☻')
            else:
                print(f'Pulingiz latte ga {self.cost_esperasso - self.coins } miqdorda puliz yetmaydi!!')
        elif sora == 'esperasso':
            if self.coins >= self.cost_esperasso:
                self.coins -=self.cost_esperasso
                t.make_esperasso()
                print('Marhamat sizning espersso ingiz iching va zavq oling ☺️☻')
            else:
                print(f'esperasso ga {self.cost_esperasso - self.coins } miqdorda pulliz yetmaydi! ')

        elif sora == 'capuccino':
            if  self.coins >= self.cost_capuccino:
                self.coins -= self.cost_capuccino
                t.make_capucino()
                print('Marhamat sizning capuccino ingiz iching va zavq oling ☺️☻')
            else:
                print(f'capuccino ga {self.cost_capuccino - self.coins} miqdorda pulliz yetmaydi! ')



    def give_information(self):
        print(f"sizda mavud mablag' miqdori = {self.coins}")
        print(f"suvimiz {t.suv} gram \nCoffeimiz {t.coffe} gram \nSutimiz {t.sut} gram")
