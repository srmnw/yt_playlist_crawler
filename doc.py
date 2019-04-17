import os

OUTPUT_DIR = 'playlists'

def create_doc(name, playlist):
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    if '/' in name:
        name = name.replace('/', '_')
    with open('playlists/Playlist_' + name + '.txt', 'w+') as file:
        for item in playlist:
            file.write(item['snippet']['title'] + '\n')
        file.close()
    print("=> Playlist: '{}' successful created with {} titles".format(name, len(playlist)))
