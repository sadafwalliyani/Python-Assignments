
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