
F = [-5, -2, -5, -1, -2, -10, -34, -9]
found = F[0]

for item in F:
    if found < item:
        found = item
print(found)
