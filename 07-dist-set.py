"""
Course      : Python Is Easy       | Homework    : #7
Home Assignment : Dictionary & Set | Student Name: Abu Hdz  | Date : 19 Apr 2019
Requirement:gg
"""

# Assign variable set
favSong = {"album":"Dreaming Of Loud", "release":2006, "genre":"Pop Rock - R&B", "length": "3:38", "label": "Moslet - Interscope", \
    "songWriter":"Ryan Tedder", "producer":"Greg Wells" }

def checkVar(key, val):
    if(key in favSong):
        return ("The Key is exist!")
    return ("The Key is not exist!")

print (checkVar("length", "5:90"))

# Print to screen
print ("This is Wiki about song 'Appologize' by OneRepublic")
print ("-----------------------------------------------------")
print ("Album        : " + favSong["album"])
print ("Release      : " + str(favSong["release"]))
print ("Genre        : " + favSong["genre"])
print ("Song length  : " + favSong["length"])
print ("Label        : " + favSong["label"])
print ("Song Writer  : " + favSong["songWriter"])
print ("Producer     : " + favSong["producer"])
