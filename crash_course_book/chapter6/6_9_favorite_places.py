favorite_places = {
        'rafael': ['vitoria'],
        'laura': ['Aracroca', 'patos'],
        'julia': ['regencia', 'itaunas', 'vicosa']
        }
for key, values in favorite_places.items():
    print(f"{key}'s favotire places are:")
    for data in values:
        print(f"\t - {data}")

