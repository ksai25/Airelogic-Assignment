import sys
import music
import requests
import concurrent.futures

def requestCall(url: str, type="GET", params=None, headers=None) -> requests.request or None:
    ''' Common method for the API request calls for Musicbrainz & Lyrics   '''
    try:
        response = requests.request(type, url, headers=headers, params=params)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError:
        pass

def requestLyrics(song_title,url: str,songobj) -> None:
    ''' This method will be called in a loop & it will calculate the wordcount of all the songs'''
    word_count = 0
    response_lyrics = requestCall(url,"GET")
    if response_lyrics :
        lyrics = response_lyrics.json()['lyrics']
        word_count = len(lyrics.split())
        record_obj = music.Recording(songtitle=song_title,word_count=word_count)
        record_obj.assign_wordcount(song_title,word_count)


def findArtist(artistname):
    '''
    Function to check whether the Artist name ,input by the user is available in musicbrainz database
    if the Artist exists , function will return the name & the id of the Artist
    '''
    print("Searching the Author in the Musicbrainz DB.........")
    url = f"http://musicbrainz.org/ws/2/artist?query={artistname}?&fmt=json&limit=1"
    response_json = requestCall(url,"GET")
    artist_json = response_json.json()
    if len(artist_json['artists']) == 0:
        print(f"The Artist information is not present in the Musicbrainz database")
        artist_obj = None
        return artist_obj
    else:
        artist_jid = artist_json['artists'][0]['id']
        artist_jname = artist_json['artists'][0]['name']
        artistFoundFlag = True
        artist_obj = music.Artist(artist_id=artist_jid, artist_name=artist_jname)
        return artist_obj



def findRecordings(artistobj: music.Artist) -> None:

    '''Function to get the songs of the Artist from an API call '''

    print("Getting all the songs by the Artist from Musicbrainz database............ ")
    url = f"http://musicbrainz.org/ws/2/recording/?artist={artistobj.artist_id}&limit=100&fmt=json"
    response_json1 = requestCall(url,"GET")
    recording_json = response_json1.json()
    recordings = response_json1.json()['recordings']
    recordTitle= []
    artistobj.store_songs(recordings)


def getLyrics(artistobj:music.Artist,songobj:music.Recording):
    ''' Get Lyrics Function will loop through all the songs by the Artist and
        get the corresponding Lyrics from the API call.

    '''
    print("Fetching & Calculating the wordcount of the Songs by the Artist..........")
    # To remove the duplications from the song list
    artistobj.songs = list(dict.fromkeys(artistobj.songs))
    # Used threadpool executor to speed up the process by executing them in concurrent and parallel mode
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for songtitle in artistobj.songs:
            print(f"Getting the Lyrics for the song : {songtitle}")
            url = f"https://api.lyrics.ovh/v1/{artistobj.artist_name}/{songtitle}"
            futures.append(executor.submit(requestLyrics(songtitle,url,songobj)))

 #       for future in concurrent.futures.as_completed(futures):
 #           print(future.result())





