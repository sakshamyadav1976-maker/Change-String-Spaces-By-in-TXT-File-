def write():
    f = open("text5.txt","w")
    t = input("Enter the Message :")
    f.write(t)
    print("Message is added to file")
    f.close()

def count():
    f = open("text5.txt","r")
    r = f.read()
    print("This message is in file :",r)
    print(r.strip().replace(" ","#"))
    f.close()
    
def menu():
    print("press 1 to write in file")
    print("press 2 to read file")
    n = int(input("Enter the No. To procced :"))
    if n == 1:
        write()
    elif n== 2:
        count()
    else:
        print("Invalid option")

menu()

