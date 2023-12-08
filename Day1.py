#First task

text = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
values = []
j = 0

#Finds if character is digit and adds it to list
for item in text:
    adding = ""
    for char in item:
        if char.isdigit():
            adding += char
    values.append(adding)

#Adds the first and last char in list to count and changes it to int and counts the values
for item in values:
    count = ""
    count = item[0] + item[-1]
    j += int(count)

print(j)

