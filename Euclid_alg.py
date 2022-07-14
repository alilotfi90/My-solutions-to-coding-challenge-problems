def eucli(a,b):
  if a==0 or b==0:
    return 0
  a , b =max(abs(a),abs(b)) , min(abs(a),abs(b))
  r=a%b
  while r!=0:
    a , b =max(abs(a),abs(b)) , min(abs(a),abs(b))
    a , b = b , a%b
    r=a%b
  return b
def isprime(n):
  count=0
  for i in range(1,n):
    if n%i==0:
      count+=1
  if count==1:
    return 1
  else:
    return 0
def euler_phi(n):
  count=0
  for i in range(1,n):
    if i==1:
      count+=1
    elif i !=1 and n%i==1:
      print('i is',i)
      count+=1
    else:
      continue
  return count

def main():
  print(eucli(54,30))
  print(isprime(1))
  print(euler_phi(4))
if __name__ == "__main__":
  main()