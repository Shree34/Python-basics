a= 'shrinath is a good boy \n but not a bad boy'
print(a)
print("This is a backslash: \\")
print("Hello\nWorld")
# Output:
# Hello
# World
print("Hello\tWorld")
# Output: Hello    World
print("Hello\rWorld")
# Output: World (overwrites "Hello")
print('It\'s a great day!')
print("He said, \"Hello!\"")
print("Hello\bWorld")
# Output: HellWorld (the 'o' is removed)
print("Hello\fWorld")
print("Hello\vWorld")
print("\a")  # Might produce a sound on some systems
print("\u0048\u0065\u006C\u006C\u006F")  # Output: Hello (Unicode for 'Hello')
print("\x48\x65\x6C\x6C\x6F")  # Output: Hello (Hexadecimal for 'Hello')
