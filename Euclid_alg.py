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

def main():
  print(eucli(3,-7))
if __name__ == "__main__":
  main()