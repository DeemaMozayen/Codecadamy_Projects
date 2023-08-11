
import csv
compromised_users = []

# You need to include absolute path, not just file name for VSCode to know where the files are.
# Also, included 'r' character at beginning of path to interpret as a raw string, not a normal one
# This means that the backslashes are viewed as strings and not escape characters in python 

with open(r'C:\Users\SMoza\hello\Python Scripts\# Codecadamy Project 9 - Files\passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)
  for line in password_csv:
    compromised_users.append(line['Username'])

with open(r'C:\Users\SMoza\hello\Python Scripts\# Codecadamy Project 9 - Files\compromised_users.txt', 'w') as compromised_user_file:
  for user in compromised_users:
    compromised_user_file.write(user)

import json
with open(r'C:\Users\SMoza\hello\Python Scripts\# Codecadamy Project 9 - Files\boss_message.json', 'w') as boss_message:
  boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}
  json.dump(boss_message_dict, boss_message)

with open(r'C:\Users\SMoza\hello\Python Scripts\# Codecadamy Project 9 - Files\new_passwords.csv', 'w') as new_passwords_obj:
  slash_null_sig = """ _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/"""
  new_passwords_obj.write(slash_null_sig )