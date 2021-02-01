def encryption(s):
    ls = len(s)
    column = (math.ceil(math.sqrt(ls)))
    row = (column)-1
    mat=s[:]
    
    
    if column*row<ls:
        row=column
    
    
    matrix=[]
    for i in range(row):
        matrix.append(mat[:column])
        mat = mat[column:]
    
    
    ciphertext='' 
    for i in range(column):
        for j in range(row):
            if i<len(matrix[j]):
                ciphertext+=matrix[j][i]
        ciphertext+=' '
   
    return ciphertext
