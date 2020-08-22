'''
Created on Aug 19, 2020
This code compares Type code between Albums and songs
@author: rduvalwa2
'''
import platform
import pymysql.cursors
from Musicdb_info import *
from Music_Get_Functions import musicGet_Functions
        
if __name__ == "__main__" :
        print("*************** Node Name is ", platform.uname().node)
        if platform.uname().node == 'MaxBookPro17OSX.hsd1.wa.comcast.net':
            serv = login_info_osx
            base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
            server = 'MaxBookPro17OSX' 
        elif platform.uname().node == 'OSXAir.hsd1.wa.comcast.net':
            serv = login_info_osxAir
            base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
            server = 'OSXAir' 
        else:
            print("Host is " , 'default')
            serv = login_info_default
            
        host = serv['host']
        user = serv['user']
        password = serv['password']
        db = "nextmusic"
        conn = pymysql.connect(host=host, user=user, password=password, db=db)

      
        m = musicGet_Functions(True)
        
        statement = "select  distinct album2songs.`album`, artist_albums.`album`, album2songs.type, artist_albums.type, album2songs.artist \
        from NextMusic.album2songs, NextMusic.artist_albums \
        where artist_albums.album = album2songs.`album`  \
        and  artist_albums.type != album2songs.type  \
        order by album2songs.`album`;"
            
#        print(statement)
        cursor = conn.cursor()
        try:
            cursor.execute(statement)
            result = cursor.fetchall()  
            print(result)
            if not result:
                print("Types between album and songs the same")
        except conn.Error as err:
            print("Exception is ", err)
#        print(result)
        for output in result:
            res = list(output)
            print(res)
        cursor.close()

    
    