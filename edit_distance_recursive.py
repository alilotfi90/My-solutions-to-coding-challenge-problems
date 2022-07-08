def editdisthelper(str1,str2,i,j):
  if i==len(str1):
    # insert j-len(str1) at the end of str1
    return len(str2)-j
  if j==len(str2):
    return len(str1)-i
  if str1[i]==str2[j]:
    return editdisthelper(str1,str2,i+1,j+1)
  return 1+min(editdisthelper(str1,str2,i+1,j+1),editdisthelper(str1,str2,i,j+1),editdisthelper(str1,str2,i+1,j))
#case1: change str1[i]===> editdisthelper(str1,str2,i+1,j+1)
#case2: add a letter in i position virtually, not changing the string though, meaning we add str2[j] in ith position of str1
#editdisthelper(str1,str2,i,j+1)
#case3: delete i th letter of str1, good to move i to i+1, do not change j
#editdisthelper(str1,str2,i+1,j)
def editdist(str1,str2):
  return editdisthelper(str1,str2,0,0)

def main():
    str1="the"
    str2="atgh"
    print(editdist(str1,str2))
if __name__ == "__main__":
  main()