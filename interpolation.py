import numpy as np

def select_points(fncpt, xi, n):
    total = len(fncpt)
    xs = fncpt[:, 0]

    nearest = 0
    best_dist = abs(xs[0] - xi)
    for i in range(1, total):
        dist = abs(xs[i] - xi)
        if dist < best_dist:
            best_dist = dist
            nearest = i

    start = nearest - n // 2
    if start < 0:                   
        start = 0
    if start > total - n:          
        start = total - n

    return fncpt[start:start + n]


def interpolation(fncpt, n, xi):
    diffrencedivided = [[0] * n for _ in range(n)]
    pts = select_points(fncpt, xi, n)

    for i in range(0, n):
        diffrencedivided[i][0] = pts[i][1]
    for j in range(1, n):
        for i in range(0, n - j):
            diffrencedivided[i][j] = (diffrencedivided[i + 1][j - 1] - diffrencedivided[i][j - 1]) / (pts[i + j][0] - pts[i][0])

    xproduct = 1
    result = diffrencedivided[0][0]
    for i in range(1, n):
        xproduct = xproduct * (xi - pts[i - 1][0])
        result = result + diffrencedivided[0][i] * xproduct

    return result


def user_interpolation(data):
    userinput = float(input("Enter fluid temperature: "))
    result = interpolation(data, 3, userinput)
    print(f"Estimated thermal conductivity at {userinput}: {result}")
    return result