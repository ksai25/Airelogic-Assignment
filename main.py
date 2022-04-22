import time
import datetime
import music_api
import music
import re
import numpy as np



while True:

        choice = input("Please key in your choice from the options given below : \n" +
                      "###########################################################\n" +
                       "1.Find the Average words of the songs of an Artist \n" +
                       "2.Exit \n"
                    )

        if (choice == '1'):
            artist_obj = None
            record_obj = None
            artist_name = input("Please enter an Artist name")
            artist_obj = music_api.findArtist(artist_name)
            if artist_obj:
                print(artist_obj.artist_name,artist_obj.artist_id)
                music_api.findRecordings(artist_obj)
                music_api.getLyrics(artist_obj,record_obj)
                music.Recording.calcAvg_wordCount(artist_obj)

        elif (choice == '2'):
            sys.exit()

        else:
            print("Please enter a valid Option [1 or 2]")
            print("###########################################")





