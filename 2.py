class Title():
    def __init__(self,x,y,title):
        self.x = x
        self.y = y
        self.title = title
        self.appearance = True
    def higth(self):
        self.appearance = False
    def shov(self):
        self.appearance = True
    def prent(self):
        print('Кнопка:',self.title)
        print('Розташування:',self.x,self.y)
        if self.appearance:
            print('Видимість:',self.appearance)
        elif self.appearance == False:
            print('Видимість:',self.appearance)
            print(self.title,'- приховано')
a = Title(150,50,'Дізнайтесь переможця прямо зараз!')
a.prent()
b = Title(150,-100,'Переможець може бути тільки один')
b.higth()
b.prent()