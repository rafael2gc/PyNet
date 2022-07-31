favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }
# List people sho should take the poll

poll_people = ['jen', 'otto', 'julia', 'laura', 'phil']

for key in favorite_languages.keys():
    if key in poll_people:
        print(f"Hi {key}, thank you for taking the POLL")
    else:
        print(f"Hi Mane, take the Poll")

