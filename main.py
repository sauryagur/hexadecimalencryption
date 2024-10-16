def decrypthex(hexv):
    cursor = 0
    hexdict = {
        "X": 0,
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15
    }
    intlist = []
    while cursor < len(hexv):
        left = hexv[cursor]
        right = hexv[cursor + 1]
        element = hexdict[left.upper()] * 16 + hexdict[right.upper()]
        intlist.append(element)
        cursor += 2

    print(intlist)
    normstr = ""
    for thing in intlist:
        normstr += str(chr(thing))
    return normstr

def encrypthex(strv):
    hexstr = ""
    for cha in strv:
        hexstr += str(hex(ord(cha)))[-2:]
    return hexstr


print("HEXENCRYPT")
while True:
    print("Operations:\n1.Encrypt\n2.Decrypt\n3.Exit")
    a = int(input("Enter your choice: "))
    if a == 1:
        op = encrypthex(str(input("Enter the text: ")))
        print("Encrypted text: ", op)
    elif a == 2:
        op = decrypthex(str(input("Enter the hex code: ")))
        print("Decrypted text: ", op)
    else:
        break
    a = str(input("Do you want to continue? (Y/N): "))
    if a.lower() != "y":
        break
