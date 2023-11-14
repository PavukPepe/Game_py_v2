import os
import json
class Save:
    def Body(self):
        filesname = map(lambda path: os.path.splitext(os.path.basename(path))[0],
                        list(filter(lambda file: os.path.isfile(os.path.abspath(os.path.join('Saves', file))),
                                    os.listdir('Saves'))))
        print(*list(filesname), sep='\n')
        # Вывод сохранений

        # for file in os.listdir('Saves'):
        #     # if os.path.isfile(file):
        #         print(os.path.basename(file))

        name = input("Введите имя сохранения: ")
        if len(name) == 0:
            name = 'Quiksave'
        for file in os.listdir('Saves'):
            if os.path.basename(file) == f"{name}.json":
                with open(f"Saves\\{name}.json") as f:
                    data = dict(json.load(f))
