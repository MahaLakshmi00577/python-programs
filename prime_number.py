```python
# Check whether a number is prime

num = int(input("Enter a number: "))

if num <= 1:
    print("The number is not a prime number")
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("The number is a prime number")
    else:
        print("The number is not a prime number")
```
