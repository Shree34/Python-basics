name='Shrinath'
print(len(name))
print(name.endswith("ath"))
print(name.startswith("shr"))
print(name.capitalize())

a= "shrinath is a good  good boy"
print(a. replace("good ", "bad"))


# there are lot of str functions in python ask to chatgpt
b= "  hello  "
print(b.strip())  # Output: 'hello'
c= "hello world"
print(c.replace("world", "Python") ) # Output: 'hello Python'
d= "apple, banana,cherry"
print(d.split(",") ) # Output: ['apple', 'banana', 'cherry']
e = ["apple", "banana", "cherry"]
separator = ","  # Choose your separator
print(separator.join(e))  # Output: 'apple,banana,cherry'

f="hello world"
print(f.find("world"))  # Output: 6
g="hello"
print(g.startswith("he") ) # Output: True
h=("hello")
print(h.endswith("lo"))  # Output: True
i=("hello wrld")
print(i.count("o"))  # Output: 2
j=("hello")
print(j.isalpha())  # Output: True
k="12345"
print(k.isdigit())  # Output: True
l="12345"
print(l.isnumeric())  # Output: True
m=("hello")
print(m.capitalize())  # Output: 'Hello')
n="hello world"
print(n.title())  # Output: 'Hello World'
o="Hello, {}"
print(o.format("world"))  # Output: 'Hello, world'
p="42"
print(p.zfill(5))  # Output: '00042'
