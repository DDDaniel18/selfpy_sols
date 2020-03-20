text = input("Please enter a string: ")
mid = len(text)//2
print(text[:mid].lower() + text[mid:].upper())
