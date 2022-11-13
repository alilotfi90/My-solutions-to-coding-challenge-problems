def phoneNumberMnemonics(phoneNumber):
    dic={"1":"1","0":"0","2":"abc","2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz","10":" "}
    result=[]
    if len(phoneNumber)==1:
        for a in dic[phoneNumber]:
            result.append(a)
        return result
    else:
        first=phoneNumber[0]
        tail=phoneNumber[1::]
        for a in dic[first]:
            for b in phoneNumberMnemonics(tail):
                result.append(a+b)
        return result