def queensAttack(n, k, r_q, c_q, obstacles):
    count=0
    nonset = [tuple(item)for item in obstacles]
    nonset = set(nonset)
    possible_moves = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
    for i,j in possible_moves:
        cr = (r_q+i,c_q+j)
        while 0<cr[0]<=n and 0<cr[1]<=n and cr not in nonset:
            cr = (cr[0]+i,cr[1]+j)
            count+=1
    return count
