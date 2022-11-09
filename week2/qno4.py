total_sweets = int(input("Enter the number of sweets: "))
stud = int(input("Enter the number of students: "))
sweets = total_sweets//stud
left = total_sweets % stud
print("you should give %d sweets to each students and %d will be left." %(sweets, left))