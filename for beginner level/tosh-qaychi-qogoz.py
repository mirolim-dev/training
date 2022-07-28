# Tosh qaychi qogg'oz o'yonini yaratish
a=input("Kompyutter bilan o'ynamoqchimisiz?  (ha/yoq):  ")
tanlov=['tosh', 'qaychi', 'qogoz']
if a=='ha':
    t=1
    from random import randint
    b=randint(0,2)
    c=input('birini tanlang: ( tosh,  qaychi,  qogoz ): ')
    g='Men'
    f='Tanladim'
elif a=='yoq' :  
    t=2
    c=input('birini tanlang: ( tosh,  qaychi,  qogoz ): ')
    x=input('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n 2-ishtirokchi tanlasin  ( tosh,  qaychi,  qogoz ): ')
    g='2-ishtirokchi'
    f='tanladi'
    if x=='tosh':
        b=0
    elif x=='qaychi':
        b=1
    elif x=='qogoz':
        b=2
    else:
        print('notogri malumot kiritdiz \n ( tosh,  qaychi,  qogoz )  shulardan birini kiritishiz kerak ')
else:
    t=0
    print('ha/yoq  dan birini tanlang')
if t==1 or t==2:
    if c == 'tosh':
        if b==0:
            print('durrang')
        elif b==1:
            print(f"Siz yutdiz ☻☻ \n  {g}  {tanlov[b].title()} ni {f}  siz esa {c.title()} ni ")    
        else:
            print(f"Siz yutqazdiz ☻☻ \n  {g}  {tanlov[b].title()} ni {f}  siz esa {c.title()} ni ")
    elif c == 'qaychi':
        if b==0:
            print(f"Siz yutqazdiz ☻☻ \n  {g}  {tanlov[b].title()} ni {f}  siz esa {c.title()} ni ")
        elif b==1:
            print('durrang')    
        else:
            print(f"Siz yutdiz ☻☻ \n  {g}  {tanlov[b].title()} ni {f}  siz esa {c.title()} ni ")
    elif c == 'qogoz':
        if b==0:
            print(f"Siz yutdiz ☻☻ \n  {g}  {tanlov[b].title()} ni {f}  siz esa {c.title()} ni ")
        elif b==1:
            print(f"Siz yutqazdiz ☻☻ \n  {g}  {tanlov[b].title()} ni {f}  siz esa {c.title()} ni ")
        else:
            print('durrang')
    else:
        print('hato malumot kiritdiz  ( tosh,  qaychi,  qogoz )  shulardan birini kiritishiz kerak edi ')