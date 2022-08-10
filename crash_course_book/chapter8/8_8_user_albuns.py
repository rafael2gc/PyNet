def make_album(name, album_title, songs=0):
    """ create a dictionary """
    album_dict = {
            'name': name,
            'at': album_title,
            }
    if songs:
        album_dict['songs'] = songs
    return album_dict

print("Enter 'q' at any time to stop.")
while True:
    name = input(f"What is the artist name?")
    if name == 'q':
        break
    album_title = input(f"What is the album title?")
    if album_title == 'q':
        break

    guy = make_album(name, album_title)
    print(guy)
#guy = make_album('altemar dutra', 'boemio', songs=7)
#print(guy)

