with open("store.csv", "r") as fileIn:
    with open("categories.csv", "w") as fileOut:
        for string in fileIn:
            string = string.split(";")
            strOut = string[1] + ";" + string[2]
            fileOut.write(strOut)
