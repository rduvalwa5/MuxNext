'''
Created on Mar 16, 2017
@author: rduvalwa2
'''

from Music_Get_Functions import musicGet_Functions
        
if __name__ == "__main__" :       
    mux = musicGet_Functions(True)
    myPath = "/Users/rduvalwa2/iTunes/iTunes Media/Music/Amazula/Montego Bay"    
    album = "The Supremes Gold [Disc 1]"
    artist = "The Supremes"
    genre = "R&B"
    inType = "CD"    
#    mux.add_songs_in_path(myPath, album, artist, genre, inType)
    mux.add_album(album, artist, genre, inType)
    mux.add_artist(artist, genre)
