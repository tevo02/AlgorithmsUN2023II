a = int(input())
 
for i in range(a):
  bandera = True
  b = [input()]
  if len(b) %2 != 0:
    bandera = False
    continue
  
  for i in range(len(b)):
    if b[i] != b[-(i+1)]:
      bandera = False
      break
  if bandera:
    print("YES")
  else:
    print("NO")

