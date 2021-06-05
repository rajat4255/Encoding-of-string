#Code for encoding
def Encoding(strchar):
    w=len(strchar)
    m=list()
    count=1
    c=strchar[0]
    
    for i in range(1,w):
        
        if c==strchar[i]:
            count=count+1
        else:
            x=ord(c)
            x=x+count
            char=chr(x)
            #print(char)
            m.append(char)
            if count>1:
                #print(count)
              m.append(count)
            c=strchar[i]
            count=1
    #print(c)
    m.append(c)
    #print(count)
    m.append(count)
    
    for i in range(len(m)):
        
        print(m[i],end="")
        
            
    return " "





print(Encoding(input()))




