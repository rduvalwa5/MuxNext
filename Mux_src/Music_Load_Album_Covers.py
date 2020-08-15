'''
Created on Jan 30, 2018

@author: rduvalwa2
'''
import Music_Get_Functions
#import pymysql 
import pymysql.cursors
import os
import platform
from Musicdb_info import login_info_default, login_info_osxAir, login_info_xps, login_info_WIN64_Air, login_info_osx




class Load_Album_Covers():
    def __init__(self,isNotTest):
        print("*************** Node Name is ",platform.uname().node)
        if platform.uname().node == 'C1246895-XPS':
            self.conn = pymysql.connect(host='OSXAir', user='rduval', password='blu4jazz', db='NextMusic')
#            self.conn  = c.connect(login_info_xps)
        elif platform.uname().node == 'MaxBookPro17OSX.hsd1.wa.comcast.net':
            self.conn = pymysql.connect(host='localhost', user='rduvalwa2', password='blu4jazz', db='NextMusic')
            self.server = 'MaxBookPro17OSX' 
            self.base = "/Users/rduvalwa2/python-eclipse-workspace/MuxNext/AlbumCovers"
        elif platform.uname().node == 'OSXAir.hsd1.wa.comcast.net':
            self.conn = pymysql.connect(host='OSXAir.hsd1.wa.comcast.net', user='rduval', password='blu4jazz', db='NextMusic')
            self.server = 'OSXAir' 
            self.base = "/Users/rduvalwa2/eOxigen-workspace/Mux/AlbumCovers"
        elif platform.uname().node == 'Randalls-MBP.home':
            print("Host is " , 'Randalls-MBP.home')
            self.conn = pymysql.connect(host='OSXAir.hsd1.wa.comcast.net', user='rduval', password='blu4jazz', db='NextMusic')            
        else:
            print("Host is " , 'default')
            self.conn = pymysql.connect(host='OSXAir', user='rduvalwa2', password='blu4jazz', db='NextMusic')
            self.server = 'OSXAir' 
            self.base = "/Users/rduvalwa2/eOxigen-workspace/Mux/AlbumCovers"
 
#        self.notTestRun =  isNotTest
        self.genreList = ['Alternative', 'BlueGrass', 'Blues', 'Classical', 'Country', 'Folk', 'Holiday', 'Indie Rock'\
                            'Jazz', 'Latino','Metal','New Age', 'Pop', 'Punk','R&B','Reggae', 'Rock', 'RockaBilly', 'Soundtrack'\
                            'Soul', 'Talk','TestGenre', 'TexMex', 'Traditional', 'World']
        
    def get_all_album_covers(self):
        albumCovers = []
        albumCover_list = os.listdir(self.base)
        for cover in albumCover_list:
            if os.path.isfile(self.base + "/" + cover):
                albumCovers.append((cover))
                albumCovers.sort()
        return albumCovers
    
        
    def initial_load_album_covers(self):
        idx = 0
        covers = self.get_all_album_covers()
        cursor = self.conn.cursor()
        trunkate = "truncate  `NextMusic`.album_covers ;"
        cursor.execute(trunkate)
        for cov in covers:
            insertStatement = "INSERT into NextMusic.album_covers (cover_idx, album_cover) values(" +str(idx)+"," + "\"" + cov + "\");"
            idx = idx + 1
            print(insertStatement)
            cursor.execute(insertStatement)
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()    
    
    
        
if __name__  == '__main__':
    loadCov = Load_Album_Covers(True)
    covers = loadCov.get_all_album_covers()
    for cov in covers:
        print(cov)
    loadCov.initial_load_album_covers()
#    loadCov.initial_load_album_covers_temp()
    