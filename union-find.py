N, M = map(int, input().split())

par = [i for i in range(N+1)]
rank = [0 for _ in range(N+1)]

def _find(A):
    if par[A] == A: # 스스로를 부모로 칭하고 있다면!
        return A
    else:
        par[A] = _find(par[A])
        return _find(par[A])

def _union(A, B): # 최대 높이를 확인해서 합쳐준다. 효과적으로!
    A = _find(A)
    B = _find(B)

    if A == B:
        return

    if rank[A] < rank[B]:
        par[A] = B
    elif rank[B] < rank[A]:
        par[B] = A
    else:
        par[A] = B
        rank[B] += 1


for _ in range(M):
    X,A,B = map(int, input().split())
    if X == 0:
        _union(A, B)
    else:
        if _find(A) == _find(B):
            print('YES')
        else:
            print('NO')
