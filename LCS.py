# Dynamic Programming implementation of LCS problem
 
def lcs(X , Y, m, n):     
 
    # Declaring the array for storing the dp values
    L = [[None]*(n+1) for i in range(m+1)]
 
    # Following steps build L[m+1][n+1] in bottom up fashion
    # Note: L[i][j] contains length of LCS of X[0..i-1]
    # and Y[0..j-1]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
 
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]
 
 

if __name__ == '__main__':
    S1 = "AGGTAB"
    S2 = "GXTXAYB"
    m = len(S1)
    n = len(S2)
    print ("Length of LCS is", lcs(S1, S2, m, n) )
