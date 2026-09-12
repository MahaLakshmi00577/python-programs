```python
# Check whether a number is an Armstrong number

num = int(input("Enter a number: "))

original = num
sum = 0
digits = len(str(num))

while num > 0:
    digit = num % 10
    sum = sum + digit ** digits
    num = num // 10

if sum == original:
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")
```
