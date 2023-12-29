def describe_city(city, country):
    return f'{city}, {country}'

result_1 = describe_city('Santiago', 'Chile')
result_2 = describe_city('Brasov', 'Romania')
result_3 = describe_city('London', 'United Kingdom')

print(result_1)
print(result_2)
print(result_3)

def make_album(artist_name, album_title, number_of_songs=None):
    album = {'artist_name': artist_name, 'abum_title': album_title}

    if number_of_songs:
        album['number_of_songs'] = number_of_songs

    return album

album_1 = make_album('Metallica', 'One')
album_2 = make_album('Metallica', 'Nothing Else Matters')
album_3 = make_album('Godsmack', 'Faceless', 14)

print(album_1)
print(album_2)
print(album_3)

while True:
    print('Enter q for any of the following prompts to quit: ')
    artist_name       = input('Enter an artist name: ')
    artist_album_name = input('Enter the artist\'s album name: ')
    artist_song_count = input('Enter the artist\'s album\'s song count: ')

    if artist_name == 'q' or artist_album_name == 'q' or artist_song_count == 'q':
        break

    if artist_song_count:
        album = make_album(artist_name, artist_album_name, artist_song_count)
    else:
        album = make_album(artist_name, artist_album_name)

    print(album)
