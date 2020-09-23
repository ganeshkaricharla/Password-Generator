import string


def count_letter_type(pwd):
    '''Counts the no of Uppercase ,Lowercase letters ,digits ,Special characters and size and returns the list'''
    li=[0,0,0,0,len(pwd)]
    for i in pwd:
        if i in string.ascii_uppercase:
            li[0]+=1
        elif i in string.ascii_lowercase:
            li[1]+=1
        elif i in string.digits:
            li[2]+=1
        elif i in string.punctuation:
            li[3]+=1
    return li

def report_count(upr,lwr,dgt,punc,size):
    li_str=[]
    li_chk=[False,False,False,False,False]
    if upr>=1:
        li_str.append("Satisfied  #Secure")
        li_chk[0]=True
    else:
        li_str.append("Not Satisfied  #UnSecure")
    if lwr>=1:
        li_str.append("Satisfied  #Secure")
        li_chk[1]=True
    else:
        li_str.append("Not Satisfied  #UnSecure")
    if dgt>=1:
        li_str.append("Satisfied  #Secure")
        li_chk[2]=True
    else:
        li_str.append("Not Satisfied  #UnSecure")
    if punc>=1:
        li_str.append("Satisfied  #Secure")
        li_chk[3]=True
    else:
        li_str.append("Not Satisfied  #UnSecure")

    if size<=8:
        li_str.append("Length should be more than 8 characters to be more secure        #Size of Your Password is {}".format(size))
    elif size>8 and size<=15:
        li_str.append("Perfect Length for a Password        #Size of Your Password is {}".format(size))
        li_chk[4]=True
    elif size>15:
        li_str.append("Password is Secure,But a long Password is Easy to Forget        #Size of Your Password is {}".format(size))
        li_chk[4]=True

    li=[li_str,li_chk]
    return li

def validation(pwd):
    data=count_letter_type(pwd)
    report=report_count(data[0],data[1],data[2],data[3],data[4])
    dis_report=report[0]
    chk_report=report[1]
    Recommended=True
    for i in chk_report:
        Recommended=Recommended and i
    if Recommended:
        dis_report.append("Recommended")
    else:
        dis_report.append("Not recommended")
    return dis_report
    

