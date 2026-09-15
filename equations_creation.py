import interpolation as intp

def matrixcreate(conductivity):
    Q=float(input("Enter thermal load : "))
    
    Tfluid=float(input("Enter fluid temp: "))
    
    Tambient=float(input("Enter ambient  temp : "))
    
    Rleft=float(input("Enter R left: "))
    
    Rright=float(input("Enter R ight: "))
    
    Rcol=1/(436*conductivity*0.0016)
    
    Rx=1.72413
    
    Rtim=0.44642
    
    RA=0.056818
    
    n =15
    
    coeffes= [[0]*n for _ in range(n)]
    
    b=[0]*15
    
    c1 =1/Rx
    c2 = -(2*c1 + 1/(Rtim+RA+Rcol))
    
    b=[-Q - Tfluid/(Rtim+RA+Rcol)]*n
    
    coeffes[n-1][n-1] = -(c1+(1/Rright) + 1/(Rtim + RA + Rcol))
    coeffes[0][0] = c2
    coeffes[0][1] = c1
    
    b[0] = -Q - Tfluid/(Rtim+RA+Rcol) - Tambient/Rleft
    for i in range(1,n-1):
    
        coeffes[i][i-1]=c1
        coeffes[i][i+1]=c1
        coeffes[i][i]=c2
    
    coeffes[n-1][n-2] = c1
    coeffes[n-1][n-1] = -(c1 +(1/Rleft)+ 1/(Rtim + RA + Rcol))
    b[n-1] = -Q - Tfluid/(Rtim+RA+Rcol) - Tambient/Rright    
    return b,coeffes,Tfluid


def maxinmatrix(a):
    x = len(a)
    s = [0]*x
    
    for i in range(x):
        row_max = 0
        for val in a[i]:
            if abs(val) > row_max:
                row_max = abs(val)
        s[i] = row_max     
    return s

def thomasmatrix(b, coeffes):

    n=len(coeffes)
  

    f=[0]*n
    g=[0]*(n - 1)
    e=[0]*(n - 1)

    for i in range(n):
        f[i]=coeffes[i][i]
        if i< (n - 1):
            e[i]=coeffes[i][i + 1]
        if i > 0:
            g[i - 1] = coeffes[i][i - 1]

    return b, g, f, e
