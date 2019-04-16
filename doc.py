
def create_doc(name, playlist):
    with open('playlists/Playlist_' + name + '.txt', 'w+') as file:
        for item in playlist:
            file.write(item['snippet']['title'] + '\n')
        file.close()
    print("=> Playlist: '{}' successful created with {} titles".format(name, len(playlist)))
