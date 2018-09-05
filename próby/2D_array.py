y_dim = 3
x_dim = 2
list2 = [0] * y_dim
for z in range(y_dim):
    list2[z] = [0] * x_dim

for y in range(x_dim):
    for x in range(y_dim):
        list2[x][y] = (x + 1) * (y + 1)
print(list2)