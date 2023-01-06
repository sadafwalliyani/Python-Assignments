
import re

text = """
pakistan
"""
print(re.findall("a", text)) # extact character wise

text = """
pakistan America adadki222ka
"""
print(re.findall("ki", text))

text = """
pakistan America adadki222ka
"""
print(re.findall("pak", text))

text="""
pakistan\n America pakistan  adadki222ka
"""
print(re.findall(r"pakistan\n",text))

text = """
pakistan\n America pakistan adadki222ka pakistana23232
"""
print(re.findall("pakistan", text))

text = """
pakistan\n America pakistan adadki222ka pakistana23232
"""
print(re.findall(r"\bpakistan\b", text))# \b = boudary \  , b

text = """
pakistan + USA + ABC
"""
print(re.findall("\+", text))# \b = boudary 

text="""
Paksitan USA \ ABC
"""
print(re.findall(r"\\",text)) # special character convert normal character, we apply "\" before special character

x = """
pakistan zind bad
pakistan is my country
pakistan always best country for me
We love our country
everyone can live in pakistan
"""
print(re.findall(r"^pakistan",x))# whole variable consider signle value

# ^ and $
y="""
Pakistan zinda abad
Pakistan is my country
We love pakistan
Pakistan zinda abad
Pakistan is my country
We love pakistanPakistan zinda abad
Pakistan is my country
We love pakistan
name: Muhammad Qasim
father's Name: Muhammad Aslam
education: MSDS
age : 30
"""
res=re.findall(r'age : (30)',y)# want to extract 30 -> ()
print(res)
# ^ means  starting line character
# * repeat sequence 
# . means any character except \n

# n=re.findall(".",x)
m=re.findall(r"^Pakistan.*",x,re.MULTILINE)
# print(n)
print(m)

# * means 0 or no/null and + lazmi repeat 
#vl means variables
vl= "abc aaa abd jfnrejfb xyz dnsdn aaaaa"
vl1=re.findall("a+", vl)
vl2=re.findall("a*", vl)
print(vl1)
print(vl2)

data1="""
name: Muhammad Qasim
father's Name: Muhammad Aslam
education: MSDS
age : 115
age : 2
cnic : 1234567891234
"""
resd1=re.findall(r'age : (\d+)',data1)# want to extract 30 -> ()
                           # \d = number + repeatation two people age
print(resd1)


