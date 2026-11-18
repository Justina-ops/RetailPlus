#Register page: To register account for new user and store it in user_info.txt file. 
#Programmer: Chan Yi Yang and Yew Kai Qian 
#Date: 10/09/2025

def register():
    print('Retail Plus.com')
    print('='*60)

    while True:
        login = input('Are you a new user? (Y/N): ').strip().lower()

        if login == 'y':
            gmail_c = input('Enter your email address: ').strip()
            passw_c = input('Create a new password\n'\
                            '• Must > 8 characters long\n'\
                            '• Must include letters and numbers\n'\
                            'Password: ').strip()
            check_passwc = input('Confirm your new password: ').strip()

            duplicate = False

            # Safely check for duplicates
            with open('user_info.txt', 'a+') as f:
                f.seek(0)
                for line in f:
                    line = line.strip()
                    if not line or ':' not in line:  # skip invalid lines
                        continue
                    saved_gmail, _ = line.split(':', 1)
                    if gmail_c == saved_gmail:
                        print('\nThis email is already registered.')
                        while True:
                            retry = input('Do you want to try again? (Y/N): ').strip().lower()
                            if retry == 'y':
                                print('='*60)
                                duplicate = True
                                break
                            elif retry == 'n':
                                print('\nThank You')
                                exit()
                            else:
                                print('\nInvalid Input. Please enter (Y/N)')
                        break

                if duplicate:
                    continue

                # ---- Validation Rules ----
                email_valid = '@' in gmail_c and gmail_c.endswith('.com') and any(c.isalpha() for c in gmail_c)
                password_valid = (len(passw_c) > 8 and any(c.isalpha() for c in passw_c) and any(c.isdigit() for c in passw_c))
                password_match = (passw_c == check_passwc)

                # ---- Account Creation ----
                if email_valid and password_valid and password_match:
                    print('\nAccount creation successful!')
                    print('='*60)
                    f.write(f'{gmail_c}:{passw_c}\n')
                    return
                else:
                    print('\nAccount creation failed!')
                    if not gmail_c:
                        print('Gmail cannot be empty.')
                    elif not email_valid:
                        print('Gmail must contain letters, "@" and end with ".com"')
                    if not passw_c:
                        print('Password cannot be empty.')
                    elif not password_valid:
                        print('Password must be >8 characters, contain letters and numbers.')
                    if not password_match:
                        print('Passwords do not match.')

                    print('\nSample format:')
                    print('Email: xxxx@xxxx.com')
                    print('Password: abcde1234\n')

                    while True:
                        retry = input('Do you want to try again? (Y/N): ').strip().lower()
                        if retry == 'y':
                            print('='*60)
                            break
                        elif retry == 'n':
                            print('Thank You')
                            exit()
                        else:
                            print('\nInvalid Input. Please enter (Y/N)\n')

        elif login == 'n':
            return
        else:
            print('\nInvalid Input. Please enter (Y/N)')
            print('='*60)
