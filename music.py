"""
Course      : Python Is Easy
Homework    : #2
Lecture     : Function
Student Name: Abu Hdz
Date        : 06 Apr 2019
"""
# Assign variable                                                 
# Song Title, Album, Release, Genre, Length, Song Writer, isDisbanded
song = [1, "Girls Like You", "Red Pill Blues", 2018, "Pop Rock", 3.55, "Adam Levine, Henry Wang", False], \
       [2, "Apologize", "Dreaming Out Loud", 2006, "Pop Rock - R&B", 3.28, "Ryan Tender", False], \
       [3, "Hey Jude", "Revolution", 1968, "Pop Rock", 3.28, "Lennon-McCartney", True]

def getGenre(number):
    return song[number][3] 
         
def getAlbum(number):
    return song[number][2] 

def getRelease(number):
    return song[number][3] 
    
def getSong(number):
    return song[number][1] 

def getDisbanded(number):
    return song[number][7] 

# List of Songs:
# 0 - Girls Like You
# 1 - Appologize 
# 2 - Hey Jude

# Get song #1
songNumber = 0

print("Song Title       : " + getSong(songNumber))
print("Music Album      : " + getAlbum(songNumber))
print("Release year     : " + str(getRelease(songNumber)))
print("Group Disbanded  : " + str(getDisbanded(songNumber)))