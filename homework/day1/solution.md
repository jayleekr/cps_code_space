# HW-#1 Solutions

## Soltuion 1

```python
tutor="이재원"
students="박주혜, 박영진, 진은총, 노수림, 장진용"

print("강사인 저 " + tutor + "은 " + students + "님에게 감사하다는 말씀을 드리고 싶습니다")
```

## Solution 2

```python
tutor="이재원"
students=[ "박주혜", "박영진", "진은총", "노수림", "장진용" ]
str_from_students=""
for i,student in enumerate(students):
    if i == len(students)-1:
        str_from_students += student
    else:
        str_from_students += student + ", "

print("강사인 저 " + tutor + "은 " + str_from_students + "님에게 감사하다는 말씀을 드리고 싶습니다")
```

## Solution 3

```python
def print_say_thanks(tutor, students):
        _tutor = tutor
        _students = students
        str_from_students=""
        for i,student in enumerate(_students):
            if i == len(_students)-1:
                str_from_students += student
            else:
                str_from_students += student + ", "
        print("강사인 저 " + _tutor + "은 " + str_from_students + "님에게 감사하다는 말씀을 드리고 싶습니다")
    
print("Solution 3")
tutor="이재원"
students=[ "박주혜", "박영진", "진은총", "노수림", "장진용" ]
print_say_thanks(tutor, students)
```