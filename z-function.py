def zfun(s):
     out = []
     if not s: 
         return out
     i, slen = 1, len(s)
     out.append(0)
     while i < slen:
         left, right = 0, i
         while right < slen and s[left] == s[right]:
             left += 1
             right += 1
         out.append(left)
         i += 1
     return out

result = zfun(input())
print(*result)
