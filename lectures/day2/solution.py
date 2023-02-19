#/usr/bin/env python3
# Description: Day 2 Homework
# Solution 1

def solution1() -> int:
    '''Solution 1 shows how to use if-else and function'''
    def print_say_thanks(tutor, students):
        proposition=""
        if tutor == "이재원":
            proposition = "은"
        else:
            proposition = "는"
        print("강사인 저 " + tutor + proposition + " " + students + "님에게 감사하다는 말씀을 드리고 싶습니다")

    print("Solution 1")
    tutor="이재원"
    students="박주혜, 박영진, 진은총, 노수림, 장진용"
    print_say_thanks(tutor, students)
    tutor="홍두깨"
    students="김철수, 이영희, 박철수, 김영희, 이철수"
    print_say_thanks(tutor, students)


def main() -> int:
    solution1()
    return 0

if __name__ == "__main__":
    exit(main())
