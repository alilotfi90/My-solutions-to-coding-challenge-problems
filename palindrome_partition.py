def is_pali(string):
    if string==string[::-1]:
        return True
    return False
def palindrome_partition(string):
    res=[]
    n=len(string)
    def dfs(s,index,path):
        if index==n:
            res.append(path)
            return
        for i in range(index+1,n+1):
            if not is_pali(s[index:i]):
                continue
            dfs(s,i,path+[s[index:i]])
    dfs(string,0,[])
    return res
def main(args):
    # use dfs, with inputs: 1- input string 2- start index of last partition, 3- path
    string="strinabab"
    print(palindrome_partition(string))
    # stopping criteria could be index==n, that is when string[index:] is empty
    # furthermore, if string[index:] is not a palindrome, we want to skip this path

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
