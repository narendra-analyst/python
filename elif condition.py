#check the total and excute the grade
#99 - 100 - S
#89 - 80 - A
#79 - 70 - B
#69 - 60 - C
#59 - 50 - D
#49 - 40 - E
#39 - 30 - F

mark = int(input('enter your mark:'))
if mark>=90 :
   print('your grade is S')
elif mark>=80 :
   print('your grade is A')
elif mark>=70 :
    print('your grade is B')
elif mark>=60 :
    print('your grade is C')
elif mark>=50 :
    print('your grade is D')
elif mark>=40 :
    print('your grade is E')
else :
    print('your grade is F')
