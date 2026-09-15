def thomas(g, f, e, b):
    n = len(f)
    g = g.copy()
    f = f.copy()
    e = e.copy()
    b = b.copy()

    for i in range(1, n):
        factor = g[i - 1] / f[i - 1]
        f[i] = f[i] - factor * e[i - 1]
        b[i] = b[i] - factor * b[i - 1]

    x = [0] * n
    x[n - 1] = b[n - 1] / f[n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = (b[i] - e[i] * x[i + 1]) / f[i]
    return x