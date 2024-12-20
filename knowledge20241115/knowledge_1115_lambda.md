**`lambda` 함수**는 파이썬에서 **익명 함수**(anonymous function)를 정의할 때 사용하는 키워드이다. 일반적으로 **한 줄로 간단한 연산**을 수행하는 작은 함수를 만들 때 유용하다. 

### `lambda` 함수의 특징
1. **이름이 없는 함수**: `lambda` 함수는 일반적인 `def` 함수처럼 이름을 붙일 필요 없이 사용할 수 있다.
2. **간단한 표현식**: `lambda` 함수는 **단일 표현식**만을 가질 수 있으며, 여러 줄의 코드나 복잡한 로직을 포함할 수 없다.
3. **즉시 사용 가능**: `lambda` 함수는 다른 함수의 인수로 바로 전달하거나, 임시적으로 함수를 정의해야 할 때 유용하게 사용된다.

### `lambda` 함수 구문

```python
lambda arguments: expression
```

- `arguments`: 함수에 전달할 인수들이다.
- `expression`: 함수가 반환할 값이다. 이 표현식은 반드시 하나여야 하며, 반환값을 명시적으로 `return`하지 않아도 된다.

### 예시

#### 1. 간단한 덧셈 함수

```python
add = lambda x, y: x + y
print(add(2, 3))  # 5
```

여기서 `lambda x, y: x + y`는 두 숫자 `x`와 `y`를 받아서 그 합을 반환하는 익명 함수다.

#### 2. 리스트에서 짝수만 필터링

`lambda` 함수를 사용해 리스트에서 짝수만 필터링하는 예시다.

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6]
```

위의 코드에서 `lambda x: x % 2 == 0`은 `x`가 짝수인지 여부를 확인하는 익명 함수다. `filter` 함수는 이 조건을 만족하는 값만 리스트로 반환한다.

#### 3. `map` 함수와 `lambda` 사용

`map` 함수는 주어진 함수와 iterable을 결합하여, iterable의 각 항목에 주어진 함수를 적용한다.

```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # [1, 4, 9, 16, 25]
```

위 코드에서 `lambda x: x ** 2`는 각 숫자를 제곱하는 함수로, `map` 함수는 `numbers` 리스트의 각 요소에 이 함수를 적용하여 제곱값을 계산한다.

### `lambda` 함수 vs `def` 함수

`lambda` 함수는 주로 **짧고 간단한 함수**를 정의할 때 유용하지만, 복잡한 로직을 작성하거나 여러 줄의 코드를 작성해야 할 경우에는 `def`로 함수를 정의하는 것이 더 좋다.

#### `lambda` 예시 (간단한 연산)

```python
multiply = lambda x, y: x * y
print(multiply(3, 4))  # 12
```

#### `def` 예시 (복잡한 로직)

```python
def multiply(x, y):
    result = x * y
    return result

print(multiply(3, 4))  # 12
```

### `lambda` 함수의 활용

- **간단한 함수가 필요할 때**: 간단한 연산이나 조건문을 처리할 때 사용한다.
- **함수 인수로 전달**: `lambda` 함수는 다른 함수에 인수로 바로 전달할 수 있다. 예를 들어 `filter`, `map`, `sorted`, `reduce` 등에서 많이 사용된다.

### 예시: `sorted`와 `lambda`

`sorted` 함수는 리스트나 다른 iterable을 정렬하는 함수이다. `lambda`를 사용해 정렬 기준을 지정할 수 있다.

```python
# 튜플 리스트를 두 번째 항목을 기준으로 정렬
items = [(1, 'apple'), (3, 'banana'), (2, 'cherry')]
sorted_items = sorted(items, key=lambda x: x[1])
print(sorted_items)  # [(1, 'apple'), (3, 'banana'), (2, 'cherry')]
```

여기서 `lambda x: x[1]`은 각 튜플의 두 번째 요소를 기준으로 정렬하라는 의미이다.

### 결론

- **`lambda` 함수**는 간단한 연산을 수행하는 **익명 함수**를 정의할 때 사용된다.
- `lambda`는 **간단한 식만 포함**할 수 있으며, **여러 줄의 코드**나 복잡한 로직을 처리할 수는 없다.
- 주로 **함수 인자로 넘기거나** 짧은 연산을 할 때 유용하다.

좀 더 복잡한 함수나 여러 줄의 코드가 필요하면 `def`를 사용하여 일반적인 함수를 정의하는 것이 더 적합하다. 

