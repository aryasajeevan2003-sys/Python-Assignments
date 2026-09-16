## List Creation
age_list = [24, 25, 26, 27, 28]
name_list = ["Arya", "Anu", "Riya", "Akshay", "Akhil"]
print("Age_List:", age_list)
print("Name_List:", name_list)

## List Operations/Modifications
name_list.append("Yazhini")
print("Name_List:", name_list)

age_list.insert(2,30)
print("Age_List:", age_list)

name_list.remove("Yazhini")
print("Name_List:", name_list)

age_list.pop()
print("Age_List:", age_list)

age_list.extend([29, 30, 26])
print("Age_List:", age_list)

age_list.sort(reverse=True)
print("Age_List:", age_list)

print("Maximun_Age:",max(age_list))
print("Minimum_Age:",min(age_list))
print("Sum_Of_Ages:",sum(age_list))

## Accessing List Elements
print(name_list[0])
print(name_list[-1])
print(name_list[2:5])
print(name_list[::-1])

## Dictionary
student_marks = {"Arya":85,"Anu":78,"Riya":92,"Akshay":67,"Akhil":88}
print("Student_Makrs:",student_marks)
print("Anu's mark:",student_marks["Anu"])
student_marks["Janani"]=80
print(student_marks)
student_marks["Anu"]=82
print(student_marks)
print("Keys:",student_marks.keys())
print("Values:",student_marks.values())
print("Items:",student_marks.items())

## Sets
my_set={'a','e','i','o','u','a','a','i'}
print("My_Set:",my_set)
my_set[4]='s'
##does not support indexing and does not have a fixed order

set1 = {1,3,5,7,9}
set2 = {2,3,5,8,10}
print("Union:",set1.union(set2))
print("Intersection:",set1.intersection(set2))

## Operators&Conditional Statement
score=int(input("Enter your score(0 to 10):"))
if score > 7:
    print("Above Average:Excellent Performance")
elif score >= 4:
    print("Average:Good effort! Keep practicing, there's room for improvement.")
else:
    print("Below Average:Need to improve your performance, consistent practice will lead to better results.")
    
