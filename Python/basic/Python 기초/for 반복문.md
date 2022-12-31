# for 반복문

복습: No
블로그: No

# For 반복문

```python
my_list = [2, 3, 5, 7, 11]

for number in my_list:      # number는 변수 이름
    print(number)           # 리스트의 마지막까지 반복

# while문
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
```

# range 함수

```python
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(i)
# 이렇게 1 부터 100까지 출력하는 경우는 힘들다
# 이걸 보완하기 위한 함수가 range함수이다.

# 파라미터 2개 버전
# for i in range(start, stop):
#   print(i)
for i in range(3, 11):      # 3부터 10까지 출력
    print(i)

# 파라미터 1개 버전
# for i in range(stop):
#   print(i)
for i in range(10):         # 0부터 9까지 출력
    print(i)

# 파라미터 3개 버전
# for i in range(start, stop, step):    step은 간격
#   print(i)
for i in range(3, 17, 3):
    print(i)
# range 함수 장점 : 간편함 / 깔끔함 / 메모리 효율성
```

## 문 1

numbers라는 리스트가 주어졌습니다.

for문과 range 함수를 사용하여, numbers의 인덱스와 원소를 출력해 보세요.

```python
numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
```

아래와 같이 출력

```python
0 2
1 3
2 5
3 7
4 11
5 13
6 17
7 19
8 23
9 29
10 31
```

## 답

```python
numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

for i in range(len(numbers)):
    print("{} {}".format(i, numbers[i]))
```

## 문 2

"2의 n제곱"을 출력하는 프로그램을 만들려고 합니다.

코드를 실행하면 아래와 같이 2^0 = 1부터 2^10 = 1024까지 출력되어야 합니다.

```python
2^0 = 1
2^1 = 2
2^2 = 4
.
.
.
2^10 = 1024
```

## 답

```python
for i in range(11):
    print("2^{} = {}".format(i, 2 ** i))
```

## 문 3

구구단 프로그램을 while문이 아닌 for문을 사용해서 만들어 보세요.

코드를 실행하면, 아래와 같이 출력되어야 합니다.

```python
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
.
.
.
9 * 7 = 63
9 * 8 = 72
9 * 9 = 81
```

### 답

```python
for i in range(1, 10):
		for ii in range(1, 10):
				print("{} * {} = {}".format(i, ii, i * ii))
```

## 문 4

'피타고라스 정리'라고 들어 보셨나요? 직각삼각형에서, 빗변의 제곱이 두 직각변의 제곱의 합과 같다는 정리입니다.

거기서 나온 '피타고라스 삼조'라는 개념이 있는데요. 피타고라스 삼조란, 피타고라스 정리(a^2 + b^2 = c^2 )를 만족하는 세 자연수 쌍 (a, b, c)입니다.

예를 들어, 3^2 + 4^2 = 5^2 이기 때문에 (3, 4, 5)는 피타고라스 삼조입니다.

a < b < c라고 가정할 때, a+b+c=400을 만족하는 피타고라스 삼조 (a, b, c)는 단 하나인데요. 이 경우, a * b * c는 얼마인가요?

2040000

답

```python
for a in range(1, 398):
    for b in range(1, 398):
        for c in range(1, 398):
            if a + b + c == 400 and a < b < c and a * a + b * b == c * c:
                print(a * b * c)
```

단, 이거는 오래걸림

```python
for a in range(1, 398):
    for b in range(1, 398):
        c = 400 - a - b
        if a < b < c and a * a + b * b == c * c:
            print(a * b * c)
```

이게 더 좋음

## 문제 5 *****

리스트 원소들의 순서를 거꾸로 뒤집으려고 합니다.

**numbers**라는 리스트가 주어졌을 때, **for**문을 사용하여 리스트를 거꾸로 뒤집어 보세요!

```python
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
# 코드를 입력하세요.

print("뒤집어진 리스트: " + str(numbers))
#--==>> 뒤집어진 리스트: [19, 17, 13, 11, 7, 5, 3, 2]
```

## 답

### **접근법 #1**

리스트를 뒤집기 위해서는, 서로 대칭인 원소들의 위치를 바꿔야(swap) 합니다.

### **대칭 관계 이해하기**

대칭인 원소들을 어떻게 찾을 수 있을까요? 서로 대칭이 되는 인덱스를 찾아야겠죠.

인덱스 **0**과 대칭되는 위치는 인덱스 **len(numbers) - 1**입니다.

인덱스 **1**과 대칭되는 위치는 인덱스 **len(numbers) - 2**입니다.

인덱스 **2**와 대칭되는 위치는 인덱스 **len(numbers) - 3**입니다.

대칭되는 두 인덱스를 **left**와 **right**라고 합시다.

**right = len(numbers) - left - 1**로 관계를 표현할 수 있습니다.

### **반복문 돌기**

반복문을 돌면서 **left** 요소와 **right** 요소의 위치를 바꿔 줘야 합니다.

그러기 위해서는 이렇게 할 수 있는데요.

```python
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
for left in range(len(numbers)):
    # 인덱스 left와 대칭인 인덱스 right 계산
    right = len(numbers) - left - 1

    # 위치 바꾸기
    temp = numbers[left]
    numbers[left] = numbers[right]
    numbers[right] = temp

print("뒤집어진 리스트: " + str(numbers))
#--==>> 뒤집어진 리스트: [2, 3, 5, 7, 11, 13, 17, 19]
```

이렇게 하면 리스트가 뒤집히지 않은 상태로 출력됩니다. 왜 그런 걸까요?

우리는 **for**문을 **left**가 **0**일 때부터 **left**가 **len(numbers) - 1**일 때까지 반복하는데요. 사실 **left**가 그렇게 끝까지 돌 필요가 없습니다. 그냥 리스트 길이의 반만 돌아도 리스트를 뒤집을 수 있기 때문이죠!

오히려 리스트 길이의 반을 넘게 돌면, 잘 바꿔 놨던 위치를 다시 원상 복구하는 셈입니다.

### **접근법 #2**

위치 바꾸기를 쉽게 할 수 있는 방법도 있습니다. **피보나치 수열** 과제에서 언급한 방법 기억나시나요? 강의에서 배우지는 않지만, **튜플(tuple)**이라는 자료형을 이용해서 할당하는 겁니다. 튜플은 아래와 같이 표현합니다.

```python
korean_names = ('효선', '유신')
english_names = 'hyoseon', 'yusin'

print(type(korean_names))
print(type(english_names))
#--==>>
'''
<class 'tuple'>
<class 'tuple'>
'''
```

위처럼 괄호를 통해 표현할 수도 있지만 **,** 로만 각 요소를 구분해도 튜플로 인식이 됩니다.

그럼 어떻게 위치를 쉽게 바꿀 수 있는지 코드를 보겠습니다.

```python
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
for left in range(len(numbers)):
    # 인덱스 left와 대칭인 인덱스 right 계산
    right = len(numbers) - left - 1

    # 위치 바꾸기
    numbers[right], numbers[left] = numbers[left], numbers[right]

print("뒤집어진 리스트: " + str(numbers))
```

위와 같이 쓰게 되면 지정 연산자(=) 의 오른쪽에 있는 튜플이 위치가 바뀌기 전의 **numbers[left]**, **numbers[right]** 의 값을 보관하게 됩니다. 그리고 **numbers[right]**, **numbers[left]** 에 해당하는 요소에 값을 각각 할당하게 되면서 이전 코드처럼 임시 변수를 만들지 않고도 값을 교환할 수 있는 것입니다.

### **모범 답안**

```python
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
for left in range(len(numbers) // 2):
    # 인덱스 left와 대칭인 인덱스 right 계산
    right = len(numbers) - left - 1

    # 위치 바꾸기
    numbers[right], numbers[left] = numbers[left], numbers[right]

print("뒤집어진 리스트: " + str(numbers))
#--==>> 뒤집어진 리스트: [19, 17, 13, 11, 7, 5, 3, 2]
```