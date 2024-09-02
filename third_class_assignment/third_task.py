file = open("words.txt", "a")
file.write('\n' + "שלום עולם!")
file.close()

file = open("words.txt", "r")
print(file.read())
