# HW-#2

[HW-#1](https://github.com/jayleekr/spc_code_space/blob/main/homework/day1/HW.md)

## Preface

위 문제와 이어지는 내용입니다. **HW-#1**을 풀고 오세요~

## Problem

위 문제를 제대로 해결했다면 출력창에 “**강사인 저 이재원은 박주혜, 박영진, 진은총, 노수림, 장진용 님에게 감사하다는 말씀을 드리고 싶습니다!!**” 라는 문장이 출력될 것입니다.

이재원 강사에게 일이 생겨 일일 강사를 **홍두깨** 선생님에게 맡기고 싶은데요.

결론적으로 출력창에 “이재원” 대신 “홍두깨” 가 출력되면 되는 되는 것이지요.

그런데 선생님 이름뒤에오는 조사 “은”과 “는”은 선생님의 이름에 따라 다르게 붙어야 할텐데 이를 해결 하기 위해서는 어떻게 해야할까요?
<center>
    <img src="./meme_day2.png" width="50%" height="50%" title="meme_day2"/>
</center>
아 물론 아래의 **조건**을 만족해야합니다.

## Condition(s)

tutor변수에 따라 올바른 조사(proposition)이 사용되어야함

tutor라는 변수에 처음에는 **이재원** 두번째에는 **홍두깨**를 대입하여 print 를 두번 사용함

## Examples

1. **강사인 저 이재원은 박주혜, 박영진, 진은총, 노수림, 장진용 님에게 감사하다는 말씀을 드리고 싶습니다!! → Correct!**
2. **강사인 저 홍두깨은 박주혜, 박영진, 진은총, 노수림, 장진용 님에게 감사하다는 말씀을 드리고 싶습니다!! → Incorrect!**
3. **강사인 저 홍두깨는 박주혜, 박영진, 진은총, 노수림, 장진용 님에게 감사하다는 말씀을 드리고 싶습니다!! → Correct!**

## Hint

[https://datascienceschool.net/01 python/02.05 파이썬 조건문 기초.html](https://datascienceschool.net/01%20python/02.05%20%ED%8C%8C%EC%9D%B4%EC%8D%AC%20%EC%A1%B0%EA%B1%B4%EB%AC%B8%20%EA%B8%B0%EC%B4%88.html)