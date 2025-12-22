#python class

my_list = [3,4,1,9,7,5,6,10,12,14,20,25]

def number(a):
    if a > 10:
        return True
    else:
        return False

num = list(filter(number,my_list))

print(num)
