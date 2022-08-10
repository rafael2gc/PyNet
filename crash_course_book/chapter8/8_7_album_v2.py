def make_album(name, album_title, songs=0):
    """ create a dictionary """
    album_dict = {
            'name': name,
            'at': album_title,
            }
    if songs:
        album_dict['songs'] = songs
    return album_dict



guy = make_album('zeca baleiro', 'ziriguidum')
print(guy)
guy = make_album('altemar dutra', 'boemio', songs=7)
print(guy)

