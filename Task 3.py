Li_num = int(input("enter the number of elements in the list "))
list = []
for i in range(Li_num):
    list.append(0)
for i in range(Li_num):
    list[i] = int(input("enter a number "))
Li_div = []
def div (list,N):
    for i in range(Li_num):
        if list[i]%N == 0:
            print(list[i]," is divisible by ", N)
            Li_div.append(list[i])
print (list)
n = int(input("enter a number to divide "))
div(list,n)
print ("the numbers in ", list, " that are divisble by ", n, " are ", Li_div)