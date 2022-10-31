with open('books.txt','r') as books, open('catalogue.txt','a') as catalogue:
  for line in books:
    if line.endswith("\n"):
      catalogue.writelines(line[0] + str(len(line) - 1) + "\n")
    else:
      catalogue.writelines(line[0] + str(len(line)))
catalogue = open("catalogue.txt", "r")
print(catalogue.read())