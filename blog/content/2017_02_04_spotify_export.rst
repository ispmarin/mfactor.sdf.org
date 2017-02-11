Export CSV playlists to Spotify
###############################

:date: 2017-02-04
:tags: music, spotify,
:category: music
:slug: 2017_02_04_spotify_csv_playlist
:authors: Ivan Marin
:summary: How to create a Spotify playlist from a CSV file

I'm a orphan from Grooveshark, used to listen to it non-stop. All kinds of music were there.
As it wasn't strictly legal, it got closed, of course. During this time, I amassed a large
number of tracks that I enjoyed, even made some playlists.

I saved these playlists on CSV files a long time ago. Cleaning up some old stuff,
I came across these files and decided that they should become some Spotify playlists.
But how?

There are several scripts that convert CSVs with Artist and Song name to a XPLS format,
but to transfer to Spotify, all scripts would need some form of access to my account.
As I was not willing to provide my credentials, they wouldn't work.

I finally found the `Playlist Converter <http://www.playlist-converter.net/#/>`_, that
transforms the playlist into Spotify track codes, without needing my credentials.
Awesome! After uploading the CSVs, the site would convert to Spotify track codes.
I then created an empty playlist on Spotify, copied and pasted the track codes
on the Spotify client, and voilá, all songs were there.
