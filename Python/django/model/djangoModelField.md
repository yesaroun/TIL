# Field Type

## AutoField
IntegerField이며 자동으로 증가한다. 이 코드를 명시하지 않으면 자동으로 아래 코드가 생성된다.
```python
id = model.AutoField(primary_key=True)
```

### BigAutoField
AutoField와 같지만 숫자 범위가 64bit이다.(양수만)  
1 ~ 9223372036854775807

### BigIntegerField
BigAutoField와 같아서 숫자 범위가 64bit이고, 양수, 음수 둘다 포함한다.  
-9223372036854775808 ~ 9223372036854775807

### BinaryField
이진 데이터를 저장하는 필드이다. bytes, bytearray, memoryview와 같은 데이터를 저장한다.  
기본으로 editable=False로 설정되고, max_length로 최대 길이를 제한할 수 있다.

## BooleanField
참, 거짓을 저장하는 필드이다. default값을 설정하지 않으면 None이 저장된다.

