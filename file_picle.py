import pickle

def names():
    nam_list=[]
    while True:
        print("1)add names in list")
        print("2)stop")
        option=input("enter the option:")
        if option=="1":
            a=input("enter the names")
            nam_list.append(a)
        elif option=="2":
            break
    with open("nam_list.txt","wb") as file:
        pickle.dump(nam_list,file)

def readfile():
    with open("nam_list.txt","rb") as file:
        print(pickle.load(file))

names()
readfile()




