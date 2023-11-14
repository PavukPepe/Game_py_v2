import time
import json

class Location:

    cl_loc = 0
    name = ""
    dif_search = 0
    dif_draka = 0

    actions = []
    react_draka = []
    plot_l = []
    s = ""


    list_loc = []

    def __init__(self, name, dif_s, dif_d):
        self.name = name
        self.dif_search = dif_s
        self.dif_draka = dif_d

    def act(self, *actions):
        self.actions = actions
    def vzv(self, s):
        self.s = s
    def react(self, *actions):
        self.react_draka = actions
    def plot(self, *actions):
        self.plot_l = actions
    def list_l(self, *loc):
        self.list_loc = loc
    def getter(self):
        if self.cl_loc < 1:
            for i in self.plot_l:
                time.sleep(0.5)
                print(i)
                self.cl_loc += 1
            cl = 1
            for i in self.actions:
                print(f"{cl}. {i}")
                cl += 1
        elif self.cl_loc == 1:
            cl = 1
            for i in self.actions:
                print(f"{cl}. {i}")
                cl += 1
        elif self.cl_loc :
            print(self.s)
            cl = 1
            for i in self.actions:
                print(f"{cl}. {i}")
                cl += 1
            self.cl_loc = 1
    def Saver(self):
        return {"cl_loc": self.cl_loc,
        "name":self.name,
        "dif_search":self.dif_search,
        "dif_draka":self.dif_draka,
        "actions":self.actions,
        "react_draka":self.react_draka,
        "plot_l":self.plot_l,
        "s":self.s,
        "list_loc":self.list_loc}


n1 = Location("Завод", 2, 2)
n1.plot("Резкий звук гудка будит тебя.",
        "Подсознание: -Ты свободен!",
        "Именно с этой мыслью ты открываешь свои глаза")
n1.act("Выйти во двор")
n1.react("Тебя отымели твои товарици по цеху, во все, как говорится щели",
         "Ты показал всем кто тут альфа")
n1.vzv("Вы вернулись на завод")

n2 = Location("Двор завода", 1, 1)
n2.plot("Ты вышел во двор завода. Ветер обдувает твои грязные патлы",
        "Подсознание: -Нужно похмелиться!",
        "Справа от себя ты видишь старую вахтерку. Рядом с ней распахнутые настеж ворота, в далеке виднеются жилиые дома")
n2.act("Вернуться на завод",
       "Подойти к вахтерке",
       "Пройти к жилым домам")
n2.react("Твоей головой настойчиво постучали об землю",
         "(*Звук фанфар*), Ты пафосно отпинал тех, кто на тебя напал")

n3 = Location("Вахтерка_А", 1, 1)
n3.plot("Подойдя к вахтерке ты видишь зажженный внутри свет",
        "Присмотревшись ты замечаешь тушу вахтера, который по видимости задремал")
n3.act("Зайти в вахтерку",
       "Вернуться во двор завода")
n3.react("Вахтер проснулся и налюлял тебе", "На удивление ты смог ударить вахтера")

n4 = Location("Вахтерка_Б", 3, 12)
n4.plot("Пройдя в сторожку ты окончательно убеждаешься что вахтер спит",
        "Окинув помещение взглядом ты замечаешь множество ценностей",
        "Вахтерку можно обысать, но предельно осторожно",
        "Взглянув в окно ты замечаешь одниноко стоящий магазин")
n4.act("Вернуться ко входу в вахтерку",
       "Пойти в сторону магазина")
n4.react("Вахтер проснулся и налюлял тебе", "На удивление ты смог ударить вахтера")

n5 = Location("Магазин", 5, 2)
n5.plot("Пока шел упал в говно(((",
        "Подходя к магазину появилась бредовая идея купить поесть",
        "Благо критическому мышления ты понял, что все на что у тебя хватит духа, это купить пива")
n5.act("Выйти во двор")
n5.react("Тебя отымели твои товарици по цеху, во все, как говорится щели", "Ты показал всем кто тут альфа")

n6 = Location("Жилые дома", 2, 2)
n6.plot("Дома становились все ближе",
        "Подходя все ближе ты стал слышать музыку, которая играла во дворе одного из домов")
n6.act("Вернуться в магазин")
n6.react("Тебя отымели твои товарици по цеху, во все, как говорится щели", "Ты показал всем кто тут альфа")



n1.list_l(n2)
n2.list_l(n1, n3, n6)
n3.list_l(n4, n2)
n4.list_l(n3, n5)
n1.list_l(n2)

list_location = [n1, n2, n3, n4, n5, n6]


