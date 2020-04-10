def make_album(artist_name, album_name, n_songs=None):
    album = {'artist': artist_name, 'album': album_name}
    if n_songs:  # n_songs != None:  
        album['songs'] = n_songs
    return album

album_1 = make_album('avril lavigne', 'head above water')
print(album_1)
album_2 = make_album(artist_name='green day',album_name='american idiot')
print(album_2)
# You can add calling function directly to print
print(make_album(album_name='Red Pill Blues', artist_name='maroon'))

album_4 = make_album('avril lavigne','head above water', n_songs=12)
print(album_4)