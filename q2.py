students = ['ali','vahid','sara','hamid','reza','elham','mohsen','zahra','paniz','parmida']
scores = [20,17,9 , 13, 7 , 20 , 18 , 3 , 1 , 14]
new=dict(zip(students,scores))
for student,score in sorted(new.items()):
    if score >=10:
        print(student)
    