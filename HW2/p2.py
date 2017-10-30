############################## ALGORITHMS HW2-p2 ###############################
# Global Variable
record = {}

# Functions related to Matrix Inversion
# ref : https://stackoverflow.com/questions/32114054/matrix-inversion-without-numpy
def getMinor(m,i,j):
    # remove ith row and jth column
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getDeterminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return float(m[0][0]*m[1][1]-m[0][1]*m[1][0])

    determinant = 0.0
    for c in range(len(m)):
        determinant += float(((-1)**c)*m[0][c]*getDeterminant(getMinor(m,0,c)))
    return determinant

def getInverse(m):
    determinant = float(getDeterminant(m))
    # determinant = 0, means cannot inverse
    if determinant == 0:
        return None
    # special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    # find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getDeterminant(minor))
        cofactors.append(cofactorRow)
    cofactors = getTranspose(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors

# functions related to matrix computation by my own
def getTranspose(m):
    # m is axb matrix
    a = len(m)
    b = len(m[0])
    m_t = []
    for y in range(b):
        tmp = [ m[x][y] for x in range(a)]
        m_t.append(tmp)
    return m_t

def getMultiply(X,Y):
    # X is axb matrix; Y is bxc matrix
    a = len(X)
    b = len(X[0])
    c = len(Y[0])
    Z = [] # Z = X * Y is axc matrix
    for i in range(a):
        tmp = [sum([ X[i][j]*Y[j][k] for j in range(b)]) for k in range(c)]
        Z.append(tmp)
    return Z

def getPseudoInverse(M):
    M_t = getTranspose(M)
    tmp = getInverse(getMultiply(M_t,M))
    if tmp == None:
        return None
    return getMultiply(tmp,M_t)

def getCoefficient(M,y):
    M_ps = getPseudoInverse(M)
    # if M_ps == None, indicating that y can be perfectly approximated by A
    if M_ps == None:
        return None
    return getMultiply(M_ps,y)

# functions related to dynamic programming by my own
def evaluation(start,end,y,m,c):
    # start=[0,n-2]; end=[1,n-1]
    n = len(y)
    pair = (start,end)
    # Initialize Record
    if pair == (0,n-1):
        for i in range(1,m+1):
            # if m+1 > i, we can arbitrary choosing i points and perfectly approximated
            for j in range(n-i+1):
                record[(j,j+i-1)] = 0
        #print(record)
    if pair in record.keys():
        return record[pair]
    else:
        localmin = MSE(start,end,y,m)
        #print(localmin)
        for i in range(start+1,end):
            temp = c + evaluation(start,i,y,m,c) + evaluation(i+1,end,y,m,c)
            localmin = min(localmin,temp)
        record[pair] = localmin
        return record[pair]

def MSE(start,end,y,m):
    x = [i for i in range(start+1,end+2)]
    y_pcs = [[y[i][0]] for i in range(start,end+1)]
    M = []
    for entry in x:
        M.append([entry**i for i in range(m+1)])
    A = getCoefficient(M,y_pcs)
    y_pred = getMultiply(M,A)
    y_err = sum([(y_pred[i][0] - y_pcs[i][0])**2 for i in range(len(y_pcs))])
    return y_err

def main():
    (n,m,c) = tuple(input().split(' '))
    n = int(n)
    m = int(m)
    c = int(c)

    y = input().split(' ')
    y = [[float(i) for i in y]]
    y = getTranspose(y)
    error = evaluation(0,n-1,y,m,c)
    print(int(round(error,0)))

if __name__=='__main__':
    main()
