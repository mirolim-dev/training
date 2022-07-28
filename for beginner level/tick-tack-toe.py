# Tic - tac - toe  ni yaratish

# 1-ish doskani yaratish va uni chiqarish |done
# 2-ish foydalanuvchidan katak tanlashini so'rash |done
# 3-ish o'yinchini o'zgartir  |done
# 4- ish Natijani tekshir | done

doska = [
    '-', '-', '-', 
    '-', '-', '-', 
    '-', '-', '-'
    ]

game_over = True # o'yinni  yakunlash uchun ishlataman
z = 'O' # foydalanuvhini alishtirish uchun ishlataman
draw = True # Durrang holati uchun kerak
w=0 # Durrang holatini vujudga keltirish uchun ishlataman

def show_doska():
  """Doskani ko'rsatadi"""
  print(doska[0], doska[1], doska[2])
  print(doska[3], doska[4], doska[5])
  print(doska[6], doska[7], doska[8])

def ask_from_user():
  """Foydalanuvhidan katakni tanlashni so'raydi """
  global a 
  a=int(input("Bo'sh kataklardan birini tanlang (1 dan 9 gacha) :"))-1


def Oyinchini_alishtir():
  """O'yinchilarni alishtiradi"""
  global z 
  if z=='X':
    z='O'
  else:
    z='X'
  doska[a]=z


def satr_boyicha_tekshir():
  """Satr bo'yicha teksshiradi"""
  global game_over
  if doska[0] == doska[1] == doska[2] != '-':
    print(z, ' yutdi ')
    game_over=False
    draw = False
  elif doska[3] == doska[4] == doska[5] != '-':
    print(z, ' yutdi ')
    game_over=False
    draw = False
  elif doska[6] == doska[7] == doska[8] != '-':
    print(z, ' yutdi ')
    game_over=False
    draw = False


def tekshir_qator_boyicha():
  """ Qator bo'yicha tekshiradi"""
  global game_over
  if doska[0] == doska[3] == doska[6] != '-':
    print(z, ' yutdi ')
    game_over=False
    draw = False
  elif doska[1] == doska[4] == doska[7] != '-':
    print(z, ' yutdi ')
    game_over=False
    draw = False
  elif doska[2] == doska[5] == doska[8] != '-':
    print(z, ' yutdi ')
    game_over=False
    draw = False


def dioganal_boyicha_tekshir():
  """Dioganal bo'yicha tekshiradi"""
  global game_over
  if doska[0] == doska[4] == doska[8] != '-':
    print(z, ' yutdi ')
    game_over=False
    draw = False
  elif doska[2] == doska[4] == doska[6] != '-':
    print(z, ' yutdi ')
    game_over=False
    draw = False


def tekshir():
  """Umumiy holda natijani tekshiradi """
  satr_boyicha_tekshir()
  tekshir_qator_boyicha()
  dioganal_boyicha_tekshir()



while game_over==True:
  w+=1
  show_doska()
  ask_from_user()
  if a>=0 and a<=8:
    if doska[a] == '-':
      Oyinchini_alishtir()
      tekshir() 
    else:
      print('Bosh kataklardan birini tanlang!! ')
      w-=1
    if w==9 and draw == True:
      show_doska()
      print('Draw !! ')
      game_over = False

    if game_over == False:
      ask = (input('Davom etishni hohlaysizmi? ( ha/yoq ) :  ')).lower()
      if ask == 'ha':
        w=0
        game_over = True
        doska = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

      elif ask == 'yoq':
        print('Oyin tugadi')

      else:
        print('( ha/yoq ) dan birini javob sifatid kiriting')
  else:
    w-=1
    print('1 dan 9 gacha bolgan sonni kirting !! ')