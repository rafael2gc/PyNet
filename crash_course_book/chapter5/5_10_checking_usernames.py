current_users = ['admin', 'otto', 'laura', 'julia', 'rafael2gc']
new_users = ['amin', 'root', 'pi', 'zz', 'Rafael2gc']
current_users_lower = [user.lower() for user in current_users]
#print(current_users_lower)
#print ("*" * 30)
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user}, that name is taken. You need a new username!")
    else:
        print(f"Great {new_user}, that name is available")
