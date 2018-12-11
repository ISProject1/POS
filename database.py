


file1= "db_breakfast_menu.txt"
file2= "db_lunch_menu.txt"
file3= "db_dinner_menu.txt"
file4 = "db_label_text.txt"

retail = []
title = []
label = []

with open(file1, "r") as f:
    data = f.readlines()


for line in data:
    w = line.split(":")
    title.append(w[1])


for line in data:
    w = line.split("$")
    price = w[1]
    price.rstrip('\n')
    conv = float(price)
    retail.append(conv)

f.close()

with open (file4, "r") as f:
    data = f.readlines()

for line in data:
    i = 1
    w = line.split(":")
    string1 = w[i]
    i+=1
    string2 = w[i]
    string = ("%s\n%s" %(string1,string2))
    label.append(string)


f.close()
