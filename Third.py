#creating a new file
New_file = open("new.txt", "w")
Names = [
    "rakesh", "ravi", "vineesh", "raghu", "lalith"
]
#iterating over names to write each element into file
for i in Names:
    New_file.write(i+'\n')
New_file.close()