#Login Page: To allow authorised staff to log in into the Retail Plus system by verifying their registered email and password against the saved user information in the user_info.txt. 
#Programmer: Chan Yi Yang 
#Date: 27/08/2025

def login():
    while True:
        gmail1 = input('Enter your email address: ').strip()
        passw1 = input('Enter your password: ').strip()
    
        found = False

        # use with-statement for safe file handling
        with open('user_info.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if not line or ":" not in line:  # skip empty or bad lines
                    continue
                
                saved_gmail, saved_password = line.split(":", 1)  # split only once
                if gmail1 == saved_gmail and passw1 == saved_password:
                    print('='*60)
                    print('Welcome to Retail Plus ^_^')
                    print('='*60)
                    found = True
                    return  # exit function once login is successful
        
        if not found:
            print('\nWrong email or password')
            while True:
                retry = input('\nDo you want to retry? (Y/N): ').strip().lower()
                if retry == 'y':
                    print('='*60)
                    break
                elif retry == 'n':
                    print('\nThank You!')
                    exit()
                else:
                    print('\nInvalid Input')
                    print('Please enter (Y/N)')
