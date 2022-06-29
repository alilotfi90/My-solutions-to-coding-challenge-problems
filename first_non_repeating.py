def firstNonRepeatingCharacter(st):
    dic={}
    for i in range(len(st)):
        if st[i] in dic:
            dic[st[i]].append(i)
        else:
            dic[st[i]]=[i]
    lis=[dic[key] for key in dic if len(dic[key])==1]
    lis2=[a for b in lis for a in b]
    if len(lis2)!=0:
        return min(lis2)
    else:
        return -1
def main():
  st="strriinnggs"
  print(firstNonRepeatingCharacter(st))
if __name__ == "__main__":
  main()