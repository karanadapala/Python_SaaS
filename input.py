import requests
import time

x = [1,4,15,10,7,90,50]
y = [11,14,5,]
#y = input("Give the length of the list of number?")
#for i in range(0,int(y)):
    #x[str(i)] = str(input("give the number " + str(i+1))) 

print('x')
res = requests.post('http://172.17.0.1/127.0.0.1:5000/', json={"x":"{}".format(x), "y":"{}".format(y)})
print('y')
#x ={}
if res.ok:
    print('z')
    print(res.json())
#if type(str([1,2,3]))== str : 
#    print("x") 