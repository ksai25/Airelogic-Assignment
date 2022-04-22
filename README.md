Purpose & Approach  :
The objective of this application is to accept an Artist Name from the user and
display the calculated average word count

Prerequsites/Recommended version:
Python 3.5 or above
Please install all the dependencies using the command pip3 install -r requirements.txt
Run main.py to execute the program

Functionality
1. Accepts an Artistname from the user
2. Check whether the Artist exist in the Musicbrainz database
3. Fetch all the songs of this Artist  from the Musicbrainz Database
4. Loop through and find whether lyrics are available for the songs in the Lyrice database
5. Find the word count for each song and store it
6. Finally calculate the mean of the word count

Observation & Initiatives
1. Musicbrainz database has duplication of the Artistname
    - Taken the first occurance by using limit = 1 in the request
2. Musicbrainz has repetition of the recordings and
    hence repeated calculation of the wordcount for the same song should be avoided.
    - Stored the songs in a list and removed the duplicate song title fromt he list
3. Lyrics API should be called in a loop as we need to fetch the lyrics for all the songs to calculate the wordcount
    - Used concurrent.futures.ThreadPoolExecutor() ,to have concurrent execution of the requests



