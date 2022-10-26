
import re

text = """
pakistan
"""
print(re.findall("a", text)) # extact character wise
print(text)

text = """
pakistan America adadki222ka
"""
print(re.findall("ki", text))
print(text)