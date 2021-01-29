#creating a file
File = open("new.txt", "r")
#splitting  file to make a list
List = File.read().split('/n')
# iterating over list to print elements
for i in List:
     print(i)
File.close()
