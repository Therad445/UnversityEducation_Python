import os

masEnds = ["txt", "csv", "text", "doc", "docx", "word", "pdf", "list" , "vgs", "cas"]
if os.path.exists("example"):
    print("Указанная папка существует")
else:
    print("Папка не существует")
    print("Папка создана")
    os.mkdir("example")
for end in range(len(masEnds)):
    for i in range(10):
        name = "example/" + "file" + str(i) + "." + masEnds[end]
        with open(name, "w") as file:
            file.write("Your text goes here")
print("Файлы созданы")