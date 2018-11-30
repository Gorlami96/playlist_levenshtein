import numpy as np
import csv

def read_playlist(filename):
    """
    Input: filename of CSV file listing (song,artist,genre) triples
    Output: List of (song,artist,genre)
    """
    playlist = []
    for line in open(filename):
        bits = [b.strip() for b in line.split(',')]
        playlist.append(bits)
    return playlist

def compare_track(track1 , track2 , compareType = 'Song'):
    if (compareType == 'Song'):
        if(track1 == track2):
            return True
        return False
    elif(compareType == 'Genre'):
        if (track1[2] == track2[2]):
            return True
        return False
    else:
        if (track1[1] == track2[1]):
            return True
        return False

def playlist_transform(l1 , l2 , compareType = 'Song'):
     m = len(l1)
     n = len(l2)
     dp = np.zeros((m+1 , n+1) , int)
     for i in range(m+1):
         for j in range(n+1):
             if i==0:
                 dp[i][j] = j
             elif j==0:
                 dp[i][j] = i
             elif (compare_track(l1[i-1] , l2[j-1] , compareType)):
                 dp[i][j] = dp[i-1][j-1]
             else:
                 dp[i][j] = 1 + min(dp[i][j-1] , dp[i-1][j] , dp[i-1][j-1])
     print(str(dp[m][n]) + " edits required to convert playlist 1 into playlist 2.")
     print_edits(l1,l2,dp)
     pass

def print_edits(l1,l2,dp):
    i=len(l1)
    j=len(l2)
    curr = [i,j]
    while(curr[0]>=0 and curr[1]>=0):
        if (curr[0]-1)>=0 and ((curr[1]-1) >=0 )and (dp[curr[0]-1][curr[1]-1] == dp[curr[0]][curr[1]]):
            print("Leave" + str(l1[curr[0]-1]) + " unchanged")
            curr = [curr[0]-1 , curr[1]-1]
        elif (curr[0]-1)>=0 and ((curr[1]-1) >=0 ) and  (dp[curr[0]-1][curr[1]-1] == (dp[curr[0]][curr[1]] -1)):
            curr = [curr[0]-1 , curr[1]-1]
            print("Replace" + str(l1[curr[0]]) + " with" + str(l2[curr[1]]))
        elif((curr[1]-1) >=0 )and  ( (dp[curr[0]][curr[1]-1] == dp[curr[0]][curr[1]]) or (dp[curr[0]-1][curr[1]-1] == (dp[curr[0]][curr[1]] -1)) ):
            curr = [curr[0] , curr[1]-1]
            print("Insert" + str(l2[curr[1]]))
        else:
            curr = [curr[0]-1 , curr[1]]
            print("delete" + str(l1[curr[0]]))
            
            
if __name__=="__main__":
    #obtain local copy from http://secon.utulsa.edu/cs2123/blues1.csv
    b1 = read_playlist("blues1.csv")
    #obtain local copy from http://secon.utulsa.edu/cs2123/blues2.csv
    b2 = read_playlist("blues2.csv")
    print("Playlist 1")
    for song in b1:
        print(song)
    print("Playlist 2")
    for song in b2:
        print(song)

    print('\n')
    print("Results: " + '\n' )
    print("Comparing playlist similarity by song")
    playlist_transform(b1,b2)
    print("Comparing playlist similarity by genre")
    playlist_transform(b1,b2,"Genre")
    print("Comparing playlist similarity by artist")
    playlist_transform(b1,b2,"Artist")
    #include your own playlists below

        

##l1 = [('abc', 'def', 'ghi'), ('ads', 'asas', 'vcxv') , ('sada' , 'sfg' , 'asd')]
##l2 = [('abc', 'defs', 'ghi') ,('ads', 'asas', 'vcxv')]
##dp = compare_lists(l1 , l2)
##print(dp)
            
                 
     
    
    
