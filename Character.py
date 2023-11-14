import codecs
import random
import Location
import json
import csv
import os.path

n1 = Location.n1
SAVES_DIRECTORY = 'Saves'
class Character():
    HP = 3
    inv = {"Баклашка пива": 1, "Чирик": 2}
    location = n1
    def __init__(self, getname):
        self.name = getname
    def Draka(self, dif):
        n1 = random.randint(0, 20)
        n2 = random.randint(0, 5*dif)
        if n1 > n2:
            print(self.location.react_draka[1])
            print(f"Оставеееся ХП: {self.HP}")
        else:
            self.HP = self.HP - 1
            print(self.location.react_draka[0])
            print(f"Оставеееся ХП: {self.HP}")

    def Change(self):
        if self.inv["Чирик"] > 1:
            self.inv["Чирик"] = self.inv["Чирик"] - 2
            self.inv["Баклашка пива"] = self.inv["Баклашка пива"] + 1
            print("Вес ваших карманов уменьшился, зато теперь у вас есть пиво ")
            print(f"Оставшееся пиво {self.inv['Баклашка пива']}. Оставшиеся чирики {self.inv['Чирик']}")
        else:
            print("Денег нада? Играй в авокадо!")
            print(f"Оставшиеся чирики {self.inv['Чирик']}")

    def Hilling(self):
        if self.inv["Баклашка пива"] > 0:
            self.inv["Баклашка пива"] = self.inv["Баклашка пива"] - 1
            self.HP = self.HP + 1
            print("Вы выпили пиво и чувствуете как энергия и жизненные силы возвращаются к вам")
            print(f"Оставшееся пиво {self.inv['Баклашка пива']}")
            print(f"Оставеееся ХП: {self.HP}")
        else:
            print("У вас нет пива(((")

    def Searching(self, dif):
        n1 = random.randint(0, 5*dif)
        if n1 > 15:
            k = random.randint(2, 10)
            self.inv["Чирик"] += k
            print(f"Вы нашли заначку {k} чирик(-ов)")
            print(f"Количество чириков в карманах: {self.inv['Чирик']}")
        elif n1 < 15 and n1 > 5:
            self.inv["Баклашка пива"] += 1
            print("Вам посчастливилось найти припрятанную кормушку, этикетка гласит импортое, но вы то знаете правду")
            print(f"Оставшееся пиво {self.inv['Баклашка пива']}")
        elif n1 < 5:
            print("На вас напали!")
            self.Draka(self.location.dif_draka)

    def Inventar(self):
        for i in self.inv:
            print(f"{i}: {self.inv[i]}")

    def Saver(self, name="Quiksave"):
        data = {
            "HP": self.HP,
            "inv": self.inv,
            "location": self.location.name
        }

        data_csv = [[self.name, self.HP, self.inv]]
        print(data)
        with open(f'Saves/{name}.json', 'w', encoding="utf-8") as file:
            file.write(json.dumps(data, ensure_ascii=False, indent=4))
        with open(f'Saves/saves.csv', 'a+', encoding="utf-8") as file:
            writer = csv.writer(file)
            for row in data_csv:
                writer.writerow(row)
    def getSaver(self):
        # Вывод сохранений
        filesname = map(lambda path:os.path.splitext(os.path.basename(path))[0],
                        list(filter(lambda file: os.path.isfile(os.path.abspath(os.path.join('Saves',file))), os.listdir('Saves'))))
        print(*list(filesname),sep='\n')
        
        name = input("Введите имя сохранения, для удаленения напишете delete. перед его именем: ")
        if name.split('.')[0] == "delete":
            try:
                os.remove(f'Saves\\{name.split(".")[1]}.json')
                return
            except:
                print("Сохранение не найдено")
        if len(name) == 0:
            name='Quiksave'
        for file in os.listdir('Saves'):
            if os.path.basename(file) == f"{name}.json":
                with open(f"Saves\\{name}.json") as f:
                    data = dict(json.load(f))
                    self.HP = data["HP"]
                    self.inv = data['inv']
                    for i in Location.list_location:
                        if i.name == data['location']:
                            self.location = i
                    print("Сохранение успешно загружено")

    def Setter(self, cl):
        if cl == "h":
            self.Hilling()
        elif cl == "c":
            self.Change()
        elif cl == "i":
            self.Inventar()
        elif cl == "s":
            self.Searching(self.location.dif_search)
        elif cl == "F5":
            self.Saver(input("Введите имя сохранения"))
        elif cl == "F9":
            self.getSaver()
        else:
            try:
                self.location.cl_loc += 1
                self.location = self.location.list_loc[int(cl)-1]
            except:
                print("Вы ввeли некорректное заначение")