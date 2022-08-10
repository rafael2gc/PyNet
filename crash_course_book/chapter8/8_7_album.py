def make_album(name, album_title):
    """ store in a dictionary """
    dic = {'name': name.title(), 'at': album_title.title()}
    return dic
info = make_album('caetano', 'circulando')
print(info)

info = make_album('chico science', 'afrociberdelia')
print(info)

info = make_album('planet hemp', 'usuario')
print(info)
