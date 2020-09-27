X = 33
Y = 101
Z = 3

if X < Y and X < Z:
    x = X
    if Y < Z:
        y = Y
        z = Z
    else:
        y = Z
        z = Y
else:
    if Y < X and Y < Z:
        x = Y
        if X < Z:
            y = X
            z = Z
        else:
            y = Z
            z = X
    else:
        x = Z
        if X < Y:
            y = X
            z = Y
        else:
            y = Y
            z = X

print(x, y, z)
