#-------------------------------------------------------------------
#   Name: Mihir Purwar
#   College: JIIT, Noida
#   Enroll: 15102155
#-------------------------------------------------------------------

def password_check_module(inputPassword):
    pwds = list(map(lambda x: x.strip(), inputPassword.split(',')))  # list of passwords
    for pwd in pwds:
        success = True  # checking whether password is correct or not, initializing to True
        if len(pwd) < 6:
            success = False
            print(pwd + ' Failure Password must be at least 6 characters long.')
        elif len(pwd) > 12:
            success = False
            print(pwd + ' Failure Password must be at max 12 characters long.')
        else:
            pwd_score = 5*[0]
            for character in pwd:
                temp = ord(character)
                if character in ['%', '!', ')', '(']:  # condition-[%!)(]
                    success = False
                    print(pwd + ' Failure Password cannot contain %!)(.')
                    pwd_score[4] = 1
                    break
                elif temp >= 97 and temp <= 122: pwd_score[0] = 1  # condition-[a-z]
                elif temp >= 48 and temp <= 57: pwd_score[1] = 1  # condition-[0-9]
                elif temp >= 65 and temp <= 90: pwd_score[2] = 1  # condition-[A-Z]
                elif character in ['*', '$', '_', '#', '=', '@']: pwd_score[3] = 1  # condition-[*$_#=@]
                
            if pwd_score[4] == 0:
                for i in range(4):
                    if pwd_score[i] == 0:
                        success = False
                        if i == 0: print(pwd + ' Failure Password must contain at least one letter from a-z.')
                        elif i == 1: print(pwd + ' Failure Password must contain at least one letter from 0-9.')
                        elif i == 2: print(pwd + ' Failure Password must contain at least one letter from A-Z.')
                        elif i == 3: print(pwd + ' Failure Password must contain at least one letter from *$_#=@.')
                        break
        if success:
            print(pwd + ' Success')
            
if __name__ == '__main__':
    inputPassword = input('Password: ')  # input password
    password_check_module(inputPassword)
