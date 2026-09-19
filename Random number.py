import numpy as np
#np.random.randint(low, high, size)
#low → starting value included
#high → ending value included nahi
#size → kitne numbers / array ka shape

#np.random.rand(d0, d1, d2, ...)
a=np.random.randint(low=1, high=50, size=(3,2))
print(a)
print(np.random.random((3, 4)))

#randint()   → random integers
#rand()      → random decimals (0–1)
#random()    → random decimals (0–1)
#randn()     → normal distribution
#shuffle()   → array ko shuffle





# 1. randint()
a = np.random.randint(1, 10, 5)
print("randint:", a)


# 2. randint() — 2D array
b = np.random.randint(1, 100, (3, 4))
print("2D randint:")
print(b)


# 3. rand()
c = np.random.rand(5)
print("rand:", c)


# 4. rand() — 2D array
d = np.random.rand(3, 4)
print("2D rand:")
print(d)


# 5. random()
e = np.random.random(5)
print("random:", e)


# 6. random() — 2D array
f = np.random.random((3, 4))
print("2D random:")
print(f)


# 7. randn()
g = np.random.randn(5)
print("randn:", g)


# 8. randn() — 2D array
h = np.random.randn(3, 4)
print("2D randn:")
print(h)


# 9. shuffle()
i = np.array([10, 20, 30, 40, 50])

print("Before shuffle:", i)

np.random.shuffle(i)

print("After shuffle:", i)