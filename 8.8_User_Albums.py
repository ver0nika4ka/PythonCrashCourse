def make_album(artist_name, album_name, n_songs=None):
    album = {'artist': artist_name, 'album': album_name}
    if n_songs:  # n_songs != None:  
        album['songs'] = n_songs
    return album

def print_album(album):
    print(f"Your favourite album - {album['album'].title()} by {album['artist'].title()}")

print("If you want to exit enter 'q' ")
while True:
    name = input("Tell me your favourite artis's name: ")
    if name == 'q':
        break
    album = input("Tell me your favourite album of this artist: ")
    if album == 'q':
        break
    some_album = make_album(name, album) 
    print_album(some_album)
    break