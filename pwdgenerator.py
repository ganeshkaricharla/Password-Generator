import string, random

def generatePasswordws(size):
    temp=''
    for _ in range(10):
        temp+=random.choice(string.ascii_uppercase)
        temp+=random.choice(string.ascii_lowercase)
        temp+=random.choice(string.digits)
        temp+=random.choice(string.punctuation)
    return temp[0:size]