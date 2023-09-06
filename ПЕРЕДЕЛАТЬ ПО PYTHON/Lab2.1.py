with open("mask.log", "w") as file:
    for x in range(256):
        for y in range(256):
            for w in range(256):
                for z in range(256):
                    a = str(255 - x) + "." + str(255 - y) + "." + str(255 - w) + "." + str(255 - z)
                    file.write(a + "\n")
                    print(a)
print("Задача выполнена")

ПЕРЕДЕЛАТЬ!