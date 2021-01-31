def organizingContainers(container):
    container_type = [0]*n
    ball_type = [0]*n
    for i in range(n):
         container_type[i]+=sum(container[i])
         for j in range(n):
            ball_type[i]+=container[j][i]
    if sorted(container_type)==sorted(ball_type):
        return'Possible'
    else:
        return'Impossible'
