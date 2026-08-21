import string
import secrets
import copy

def create_pw(pw_length=12):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    alphabet = letters + digits +special_chars
    pwd = ''
    pwd_strong = False

    while not pwd_strong :
        pwd =''
        for i in range(pw_length):
            pwd += ''.join(secrets.choice(alphabet))
            if any(char in  special_chars for char in pwd) and sum(char in digits for char in pwd) >= 2:
                pwd_strong = True
    return pwd
    

if __name__ == '__main__':
    print(create_pw())


lst1 = [[1,2],[3,4],[5,6,7]]
lst2 = copy.copy(lst1)
lst2[2][1] = 20
print(lst1,"lst1-------")
print(lst2,"lst2----")
