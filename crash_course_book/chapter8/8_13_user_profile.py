def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

#user_profile = build_profile('albert', 'einstein', location = 'princeton', field = 'physics')
user_profile = build_profile('Rafael', 'Giuri Costa', location = 'USU', field = 'Tudo', time = 'Fluminense')
#print(user_profile)
for key, value in user_profile.items():
    print(f"- {key}: {value}")
