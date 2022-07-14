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
    elif i !=1 and eucli(n,i)==1:
      count+=1
  return count
def calc_inv(a,m):
  if eucli(a,m)!=1:
    return False
  for i in range(1,m):
    if (a*i)%m==1:
      return i
def main():
  m="3210"
  print(int(m[0]))
  print(calc_inv(3,280))
  print(280%3)
  print(280//(-3))
  print(-94+280)
  print((3*187)%280)
  print(-93+280)
  print(10**(6)%(11*29))
  print(254**(187)%319)
  
if __name__ == "__main__":
  main()