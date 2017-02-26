# Error increases with input value
a = 1000000000
for i in range(1000000):
    a = a + 1e-6
print(a - 1000000000) # => 0.953674316406
