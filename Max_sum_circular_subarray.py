def maxsum(array):
  n=len(array)
  dp=[0]*n
  dp[0]=array[0]
  for i in range(1,n):
    dp[i]=array[i]+max(0,dp[i-1])
  return max(dp)
def minsum(array):
  n=len(array)
  dp=[0]*n
  dp[0]=array[0]
  for i in range(1,n):
    dp[i]=array[i]+min(0,dp[i-1])
  return min(dp)
def max_cycle(array):
  return max(maxsum(array),sum(array)-min(minsum(array[1:]),minsum(array[:-1])))
def main():
    array1=[5,-3,5]
    print(max_cycle(array1))
    

if __name__ == "__main__":
  main()