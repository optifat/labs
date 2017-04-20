def zfun(A, B):
     out = []
     if not A or not B: 
        return [-1]
     i, Blen = 0, len(B)
     while i < Blen:
        left, position = 0, i
        while left < len(A) and position < len(B) and A[left] == B[position]:
            left += 1
            position += 1
        if len(A) == left:
            out.append(i) 
        i+=1
     if len(out) == 0:
        return [-1]       
     return out

A = input()
B = input()
result = zfun(A, B)
print(*result)
