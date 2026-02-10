#is (a and b) or (not (c or d) and (a ==b)) true?
#a=true,b=false,c=false,d=true
print(True and False)or(not(False or True) and (True == False))
# 1.ans=false
print((True or False) and (False == True)) or (not(True == False))
# 2.ans=false
print((True == False or False<True)and(True!=True or False>False))
# 3.ans=false
print(True and (False or False)) and not(True or (False and False))
# 4.ans=false
print((True and False and False) or (not (True and (True == False))))
# 5.ans=false
print(not (True or (True and False) or (True == True)) and (True or False))
# 6.ans=false
print(True == True) or (False and False) and (not (True != False)) or (False <= True)
# 7.ans=true
print((True and False) or (False > True)) and not(True == False) and (False != False)
# 8.ans=false
print((True and False) or (False == True)) and (True != True) and (False < False)
# 9.ans=false
print(True or (False and not False) or (True == True)) and not (True == False and False != True)
# 10.ans=true
print(not(True and False) or (False < True and (False == False or True == True)))
# 11.ans=true
print(not(True or False) and (False <=True or not(True == False)) and (False == False))
# 12.ans=false
print(True and (False or False)) or not (True == False) and (False != True)
# 13.ans=false
print(True == True and False == False) or not (False == True) and (True or True)
# 14.ans=true
print((True == False) or not (False <= True)) and ((False or False) and (True != True))
# 15.ans=false
print(True or (False and (False <=True))) or not ((False or False) and (True != True))
# 16.ans=true
print(not(True and (False or(False and True))) or (False == False (True == True)))
# 17.ans=true
print(True and (False == False or False == True)) and not(True and False)
# 18.ans=true
print(True or(False and (False or True))) and not (True == False or False != True)
# 19.ans=false
print((True and False) or (False and True)) and not (True == False and False != True) or (True == True)
# 20.ans=false
print(not(True and False) and (False != True) or (True == False and not (False != False)))
# 21.ans=true
print((True or False) and (False == True)) or (True == True and not(False == True))
# 22.ans=false
print((True and False) or not(False == True)) and (True == False or (False < True))
# 23.ans=true
print(True or (False and not(False == True))) and (True != True or not (False == False))
# 24.ans=true
print((True == True and not(False and False)) or (True != False and False == True)) and (False != True)
# 25.ans=true
print((True or(False and False)) and True == True) or not (True == False)
# 26.ans=true
print(True and not(False or False) and (True == True)) or not (True and False)
# 27.ans=true
print((True and False) or ((False == True) and (True != False))) and not (True == False)
# 28.ans=false
print(True == False and not (False and True)) or (True != True and False == False)
# 29.ans=false
print((True == False and False != True) or not (True and False) and (True or (False and True)))
# 30.ans=true
