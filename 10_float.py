x : float = 3.3
print(x)
y = 1.1 + 2.2
print(y)

y_str = format(y, '.2g')
print("str ->",y_str)
print(y_str == str(x))

print("-" * 80)

print (y, x)

tolerance = 0.0001
print(abs(x - y) < tolerance)