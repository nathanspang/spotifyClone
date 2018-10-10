import datetime

from playlist import Playlist
from song import Song

nextAction = input(
    'Welcome to Spotify, would like to create a new playlist (new) list current playlists (view) or exit (exit)?: ')

playlists = []

while nextAction.lower() != 'exit':
    if nextAction.lower() == 'new':
        songs = []
        playlistName = input('What would you like to name your playlist? ')
        playlistGenre = input('What genre will this playlist contain? ')
        newSong = input('Would you like to add a song? (y) or (n) ')
        print()
        while newSong.lower() == 'y':
            songTitle = input('Song Title: ')
            songArtist = input('Song Artist: ')
            songGenre = input('Song Genre: ')
            songDuration = input('Song Duration: ')
            songs.append(Song(songTitle, songArtist, songGenre,
                              datetime.datetime.today().strftime('%Y-%m-%d'), songDuration))
            newSong = input('Would you like to add a song? (y) or (n) ')
            print()

        newPlaylist = Playlist(playlistName, playlistGenre, songs)
        playlists.append(newPlaylist.name)

        print('Playlist Added!')
        print(f'Current Playlists: {playlists}')
        print()

    elif nextAction.lower() == 'view':
        print(playlists)
    else:
        print(
            'Invalid Input, enter [new] to add new playlist, or [view] to view playlists.')
        initial = input(
            'Welcome to Spotify, would like to create a new playlist (new) or list current playlists? (view): ')
