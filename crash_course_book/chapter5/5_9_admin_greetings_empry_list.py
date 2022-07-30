user_list = ['admin', 'otto', 'laura', 'julia', 'rafael2gc']
#user_list = []
if user_list:
    for user in user_list:
        if user == 'admin':
            print(f"Hello {user}, would you like to see a status report")
        else:
            print(f"Hello {user}, nice to see you logging again")
else:
     print(f"We need some users")

