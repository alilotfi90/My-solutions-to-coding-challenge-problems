def is_first_smaller(str1,str2):
    if str1.count(min(str1))<str2.count(min(str2)):
        return True
    return False
def compare_strings(lis1,lis2):
    m=len(lis1)
    n=len(lis2)
    retlis=[0 for i in range(n)]
    for i in range(n):
        for j in range(m):
            if is_first_smaller(lis1[j],lis2[i]):
                retlis[i]+=1
    return retlis
def main():
    lis1=['aaa','bcd']
    lis2=['avd','asfd','zzz']
    print(compare_strings(lis1,lis2))
if __name__ == "__main__":
  main()