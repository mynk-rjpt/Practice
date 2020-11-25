def find(str, ch, start=0, end = len(str)):
    index = start
    while index < len(str):
        if str[index] == ch:
            return index
        index = index + 1

a = find("Pomegranate", 'm')
print(a)