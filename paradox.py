import matplotlib.pyplot as plt

prob_n = 365/365
j = 1
y = []

for i in range(99):
    prob_n = 1
    j = 1
    while j <= i:
        prob_n = prob_n * ((365 - j) / 365.0)
        j += 1
    y.append(1-prob_n)

x = []
for i in range(99):
    x.append(i+1)

print(len(x))
print(len(y))

plt.scatter(x, y)
plt.xlabel("Number of People")
plt.ylabel("P(Same Birthday")
plt.axvline(22, color = "red")
plt.show()