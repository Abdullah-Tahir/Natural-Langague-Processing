def printing(D):
    for row in D:
        print(row)
def editDistance(source, target):
    slen = len(source)
    tlen = len(target)
    
    D = []
    for i in range(slen + 1):
        tmp = []
        for j in range(tlen + 1):
            tmp.append(0)
        D.append(tmp)
        
    for i in range(1, slen + 1):
        D[i][0] = D[i-1][0] + 1
    for j in range(1, tlen + 1):
        D[0][j] = D[0][j-1] + 1
        
    for i in range(1, slen + 1):
        for j in range(1, tlen + 1):
            if source[i-1] == target[j-1]:
                D[i][j] = D[i-1][j-1]
            else:
                D[i][j] = min(D[i-1][j] + 1,
                D[i][j-1] + 1,
                D[i-1][j-1] + 2)
    printing(D)


editDistance("play", "play")

def recursive(source, target, s_len, t_len):
  if s_len == 0:
      return t_len
  if t_len == 0:
      return s_len
  if source[s_len - 1] == target[t_len - 1]:
    return recursive(source, target, s_len - 1, t_len - 1)
  return min(recursive(source, target, s_len, t_len - 1) + 1,
              recursive(source, target, s_len - 1, t_len) + 1,
                recursive(source, target, s_len - 1, t_len - 1) + 2)

city=['pattoki','lahore','islamabad','karachi','multan','kohat','Chakwal','Chichawatni','Chiniot','Chishtian','Daska','Darya','Dera','Ghazi','Dhaular','Dina','Dinga','Dipalpur']
g=input("enter city:")
count=list()
dicts=dict()
for i in city:
  x=recursive(i, g, len(i), len(g))
  count.append(x)
  dicts[i]=x
print(min(dicts,key=dicts.get))

