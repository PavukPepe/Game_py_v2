import Character
char = Character.Character(input("Введите имя: "))


while True:
    char.location.getter()
    char.Setter(input("Ваше действие: "))

    if char.HP == 0:
        print("Работяга не смог выжить в этом жестоком мире")
        break
