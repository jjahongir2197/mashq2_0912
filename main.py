list comprehension

1 - misol

words = ["dog", "cat", "mouse"]
result = [w[0] for w in words]
print(result)

2 - misol

numbers = [-5, 3, -1, 0, 7, -2]
result = [x for x in numbers if x > 0]
print(result)

3 - misol

resault = ["juft" if x % 2== 0 else "toq" for x in range(1, 11)]
print(resault)

4 - misol

numbers = [4, 9, 16, 25]
result = [x ** 0.5 for x in numbers]
print(result)

5 - misol

result = [x for x in range(0, 51) if x % 5 == 0]
print(result)

6 - misol

words = ["hello", "world", "python"]
result = [w.upper() for w in words]
print(result)
