text = input("Enter a string: ")
textlen = len(text)

for char in text:
    ascii = ord(char)
    print(f"{char} = {ascii} ")