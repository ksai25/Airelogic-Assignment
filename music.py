import music
import numpy as np
import sys


class Recording:
    ''' Class to hold the details of the Song ( title , lyrics available in the API call,wordcount)
        A list to hold all the songs details
    '''
    songdetails = []
    def __init__(self, songtitle=None, lyrics_avail=False, word_count=0) -> None:
        self.songtitle = songtitle
        self.lyrics_avail = False
        self.word_count = 0
        self.songdetails.append(self)

    def assign_wordcount(self, songtitle,word_count) -> None:
        ''' Method to assign the song title and the word count for each song '''
        self.songtitle = songtitle
        self.lyrics_avail = True
        self.word_count = word_count


    def calcAvg_wordCount(self) -> None:
        '''Method to calculate the Average word count of all the songs given by the Artist'''
        word_counts = []
        print("----------------------------------------------------------------")
        for record in Recording.songdetails:
            print (f"Song : {record.songtitle} ;   Wordcount : {record.word_count}")
            word_counts.append(record.word_count)
        if len(word_counts) > 0:
            Avg = int(np.mean(word_counts))
            print("--------------------------------------------------------------------------------")
            print(f"The Average word count of all the songs for the Artist is : {Avg}")
            print("--------------------------------------------------------------------------------")
        else:
            print(f"Songs not available for the Artist in the lyrics database")
            print("--------------------------------------------------------------------------------")

class Artist(object):
    '''Class to hold the details of the Artist'''
    def __init__(self, artist_id, artist_name,  songs=None, avgwordcount=0) -> None:
        self.artist_id = artist_id
        self.artist_name = artist_name
        self.songs = []
        self.avgwordcount =0


    def store_songs(self,artist_songs:dict) -> None:
        ''' Method to store all the Song title given by the Artist '''
        for artist_song in artist_songs:
            self.songs.append(artist_song['title'])
        #for song in self.songs:
        #    print(f"Song in the artist.songs object : {song} ")
