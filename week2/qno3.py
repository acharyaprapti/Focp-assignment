stud = int(input("How many students? "))
group_size = int(input("Required group size? "))
groups = stud // group_size
left = stud % group_size
print ("There will be", groups, "groups with", left, "students left over. ")