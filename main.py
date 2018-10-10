import datetime

from playlist import Playlist
from song import Song

nextAction = input(
    'Welcome to Spotify, would like to create a new playlist (new) or exit (exit)?: ')

playlists = []


if nextAction.lower() == 'new':
    songs = []
    playlistName = input('What would you like to name your playlist? ')
    playlistGenre = input('What genre will this playlist contain? ')
    anotherSong = input('Would you like to add a song? (y) or (n) ')
    print()
    while anotherSong.lower() == 'y':
        songTitle = input('Song Title: ')
        songArtist = input('Song Artist: ')
        songGenre = input('Song Genre: ')
        songDuration = input('Song Duration: ')
        newSong = Song(songTitle, songArtist, songGenre,
                       datetime.datetime.today().strftime('%Y-%m-%d'), songDuration)
        songs.append(newSong.title)
        anotherSong = input('Would you like to add a song? (y) or (n) ')
        print()

    newPlaylist = Playlist(playlistName, playlistGenre, songs)
    playlists.append(newPlaylist.name)

    print('Playlist Added!')
    print(f'Current Playlists: {playlists}')
    print(f'Songs in created playlist: {songs}')
    print()

else:
    print(
        'Invalid Input, enter [new] to add new playlist, or [view] to view playlists.')
    initial = input(
        'Welcome to Spotify, would like to create a new playlist (new) or exit (exit): ')
