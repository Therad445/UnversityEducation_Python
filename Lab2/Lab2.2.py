ip = input("Введите IPv4 адрес: ")
ip = ip.split(".")
with open("mask.log", "r") as fileIn:
    with open("ip_solve.log", "w") as fileOut:
        for string in fileIn:
            string = string.replace('\n', '')
            string = string[:15]
            mac = string.split(".")
            ip[2] = str(int(str(bin(int(ip[2]))[:-1]) + str(bin(int(mac[2]))[-1]), base=2))
            ip[3] = mac[3]
            strOut = str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + "." + str(ip[3])
            fileOut.write(strOut + "\n")

# ip = input("Введите IPv4 адрес: ")
# ip = ip.split(".")
# with open("mask.log", "r") as fileIn:
#     with open("ip_solve.log", "w") as fileOut:
#         for string in fileIn:
#             string = string.replace('\n', '')
#             string = string[:15]
#             mac = string.split(".")
#             print(ip)
#             print(bin(int(ip[2])))
#             print(bin(int(ip[3])))
#             print(mac)
#             print(bin(int(mac[2])))
#             print(bin(int(mac[3])))
#             ip[2] = str(int(str(bin(int(ip[2]))[:-1]) + str(bin(int(mac[2]))[-1]), base=2))
#             print()
#             ip[3] = mac[3]
#             print(ip)
#             print(bin(int(ip[2])))
#             print(bin(int(ip[3])))
