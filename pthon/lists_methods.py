#List and Tuple

#List mutable - changeable []
#tuple imutable- Unchangeable ()

#List
from ast import Num
import imp
import numbers
from operator import index
from typing import List
from unicodedata import name

    #       0       1       2       3
names= ['sadaf','rustam', 'Ali','samra']
    #    -4        -3       -2     -1
print(names[2]) #list[index] extract value with positive index 
print(names[-1]) #List[Start:end] extarct value with negative index
print(names) #list[start:end:seq] 

print('before',names)
names[0] = 'Sadaf Mansoor'

print('after',names)

#extract multiple values from list or tuple (start enclude, end exclude one minus)

#esc->m-shift+enter

print(names[1:3]) # start enclude, end exclude index-1
print(names[1:4]) # start enclude, end exclude index-1

#while loop
i=0
while i<len(names):
    print(names[i])
    i+=1

# While Lopp

# s= int(input('start No:'))
# e= int(input('end No:'))
# i=s
# while i<e:
#     print(names[i])
#     i+=1

#list[start:end:seq] 
# Start =enclude
#end = Exclude
#sequence =steps

numbers= list(range(1,21))
print(numbers)

num=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(num)
#start:end:seq
print(num[8:])
print("step-1",numbers[::1])
print("step-2",numbers[::2])
print("step-3",numbers[::3])

print(numbers[0:10:-1]) #right to left
print(numbers[::-1]) #right to left
print(numbers[-11:-1])


# data=("""
# 11:07:16 From Sadaf(174657) = Name:Sadaf(174657)
# 11:08:16 From Hammad PIAIC(174650) =  Name: Hammad PIAIC(174650)
# """)

# for r in data.split("\n"):
#     if "=" in r:
#         d= r.split('=')
#         print(d[0].split(':')[-1])
# # print(d)

# data1=("""
# 11:07:16 From Sadaf(174657) = Name:Sadaf(174657)
# 11:08:16 From Hammad PIAIC(174650) =  Name: Hammad PIAIC(174650)
# """)

# for r in data.split("\n"):#split in line
#     if "=" in r:
#         d=r.split("=") #split after =
#         print(d)

data3=("""
09:02:45 From Muhammad Sadullah = PIAIC-178950 To Everyone : Assalam O Alikum
09:03:06 From PIAIC188523 - Subhan Ahmed To Everyone : waalikum assalam
09:03:24 From Kashif To Everyone : Kashif - PIAIC181638
09:03:36 From Syed Jawad [PIAIC185558] To Everyone : wa alikum assalam
09:03:52 From Muhammad Sadullah = PIAIC-178950 To Everyone : Muhammad Sadullah = PIAIC-178950
09:04:18 From Shahzaib To Everyone : sir assalam o alikum sir ya mari 3 class ha . jo class miss h gai ha wo kasa lo
09:04:32 From ABDUL BASIT To Everyone : ABDUL BASIT PIAIC 59115
09:04:38 From PIAIC183349 Muahhamd Waseem To Everyone : sir blockstructure sy start krna hy sir
09:05:02 From Mohammad Javed To Everyone : Mohammad Javed
PIAIC 185754
09:05:06 From Humera Naz To Everyone : PIAIC 173431
09:05:07 From Muhammad Saad To Everyone : Muhammad Saad - PIAIC172478
09:05:21 From Sabir Zafar To Everyone : Muhammad Sabir Zafar PIAIC182023
09:05:29 From Shahzaib To Everyone : Muhammad Shahzaib Iqbal
09:05:34 From Sabir Zafar To Everyone : PIAIC182023
09:05:37 From Mohammad Javed To Everyone : Assalamo Alykum to everyone
09:06:04 From Shahzaib To Everyone : sir ya ap kia para raha ha
09:06:10 From Usman Noor PIAIC-188401 To Everyone : Usman Noor PIAIC-188401
09:06:31 From Amir Rashid To Everyone : aoa sir jee
09:06:41 From Salman Nayyer To Everyone : PIAIC 180996
09:06:42 From Usman Noor PIAIC-188401 To Everyone : yes
09:06:44 From Moattar Khanum (PIAIC170982) To Everyone : Moattar Khanum - PIAIC170982
09:07:06 From MUHAMMAD USMAN MANZOOR To Everyone : Muhammad Usman Manzoor
128778
09:07:56 From Syed Jawad [PIAIC185558] To Everyone : distortion ari h voice me
09:08:03 From Zeeshan Asim : PIAIC55300 To Everyone : Zeeshan Asim Khan, PIAIC55300
09:08:15 From Syed Jawad [PIAIC185558] To Everyone : loop
09:08:32 From Kainat PIAIC182352 To Everyone : piaic 182352
09:09:07 From Syed Jawad [PIAIC185558] To Everyone : PIAIC185558
09:09:12 From Amir Rashid To Everyone : PIAIC107890
09:09:15 From Victor PIAIC 177535 To Everyone : PIAIC 177535
09:09:46 From Nasir Hussain (Faculty) To Everyone : 
""")
students_roll_no=[]
import re
for r in data3.split("\n"):#split in line
   a = re.findall("PIAIC\d{1,7}",r) #print PIACI and numbers
   b =re.findall("AIC-\d{1,7}",r)#print AIC and number
   result =a+b
   result=list(set([i.replace("-","") for i in result]))
# if len(result)>1 and result not in students_roll_no: students_roll_no.append(result)
print(len(result))