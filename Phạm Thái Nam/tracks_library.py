from library_item import LibraryItem


library = {}

library["01"] = LibraryItem("Shape of You", "Ed Sheeran", 5)
library["02"] = LibraryItem("Blinding Lights", "The Weeknd", 4)
library["03"] = LibraryItem("Rolling in the Deep", "Adele", 5)
library["04"] = LibraryItem("Someone Like You", "Adele", 4)
library["05"] = LibraryItem("Uptown Funk", "Mark Ronson ft. Bruno Mars", 5)
library["06"] = LibraryItem("Perfect", "Ed Sheeran", 5)
library["07"] = LibraryItem("Old Town Road", "Lil Nas X ft. Billy Ray Cyrus", 4)
library["08"] = LibraryItem("Havana", "Camila Cabello ft. Young Thug", 4)
library["09"] = LibraryItem("Dance Monkey", "Tones and I", 3)
library["10"] = LibraryItem("Bad Guy", "Billie Eilish", 4)

library["11"] = LibraryItem("Thank U, Next", "Ariana Grande", 5)
library["12"] = LibraryItem("Closer", "The Chainsmokers ft. Halsey", 4)
library["13"] = LibraryItem("Shallow", "Lady Gaga & Bradley Cooper", 5)
library["14"] = LibraryItem("Bohemian Rhapsody", "Queen", 5)
library["15"] = LibraryItem("Sweet Child O' Mine", "Guns N' Roses", 4)
library["16"] = LibraryItem("Believer", "Imagine Dragons", 4)
library["17"] = LibraryItem("Radioactive", "Imagine Dragons", 5)
library["18"] = LibraryItem("Stressed Out", "Twenty One Pilots", 4)
library["19"] = LibraryItem("Despacito", "Luis Fonsi ft. Daddy Yankee", 5)
library["20"] = LibraryItem("See You Again", "Wiz Khalifa ft. Charlie Puth", 5)

library["21"] = LibraryItem("Shake It Off", "Taylor Swift", 4)
library["22"] = LibraryItem("All of Me", "John Legend", 5)
library["23"] = LibraryItem("Love Yourself", "Justin Bieber", 4)
library["24"] = LibraryItem("Rockstar", "Post Malone ft. 21 Savage", 3)
library["25"] = LibraryItem("Hello", "Adele", 5)
library["26"] = LibraryItem("Sorry", "Justin Bieber", 4)
library["27"] = LibraryItem("Thinking Out Loud", "Ed Sheeran", 5)
library["28"] = LibraryItem("One Dance", "Drake ft. Wizkid & Kyla", 4)
library["29"] = LibraryItem("Cheap Thrills", "Sia ft. Sean Paul", 4)
library["30"] = LibraryItem("Wake Me Up", "Avicii", 5)

library["31"] = LibraryItem("Love Me Like You Do", "Ellie Goulding", 4)
library["32"] = LibraryItem("Levitating", "Dua Lipa", 5)
library["33"] = LibraryItem("Memories", "Maroon 5", 3)
library["34"] = LibraryItem("Blowin' in the Wind", "Bob Dylan", 4)
library["35"] = LibraryItem("Royals", "Lorde", 4)
library["36"] = LibraryItem("Faded", "Alan Walker", 4)
library["37"] = LibraryItem("Attention", "Charlie Puth", 4)
library["38"] = LibraryItem("Imagine", "John Lennon", 5)
library["39"] = LibraryItem("Firework", "Katy Perry", 4)
library["40"] = LibraryItem("Counting Stars", "OneRepublic", 5)

library["41"] = LibraryItem("Don't Start Now", "Dua Lipa", 5)
library["42"] = LibraryItem("I Will Always Love You", "Whitney Houston", 5)
library["43"] = LibraryItem("We Will Rock You", "Queen", 4)
library["44"] = LibraryItem("Billie Jean", "Michael Jackson", 5)
library["45"] = LibraryItem("Hotel California", "Eagles", 5)
library["46"] = LibraryItem("Toxic", "Britney Spears", 4)
library["47"] = LibraryItem("Poker Face", "Lady Gaga", 4)
library["48"] = LibraryItem("Lose Yourself", "Eminem", 5)
library["49"] = LibraryItem("Senorita", "Shawn Mendes & Camila Cabello", 4)
library["50"] = LibraryItem("God's Plan", "Drake", 4)

library["51"] = LibraryItem("What a Wonderful World", "Louis Armstrong", 5)
library["52"] = LibraryItem("Killing Me Softly", "The Fugees", 5)
library["53"] = LibraryItem("Halo", "Beyoncé", 5)
library["54"] = LibraryItem("Take Me to Church", "Hozier", 4)
library["55"] = LibraryItem("Can't Stop the Feeling!", "Justin Timberlake", 4)



def list_all():
    """Returns a formatted string of all tracks in the library."""
    track_list = []
    for key, track in library.items():
        track_list.append(f"{key}: {track.song} by {track.singer}, Rating: {track.rating}, Plays: {track.play_count}")
    return "\n".join(track_list)

def get_song(key):
    """Returns the song name for the given track key."""
    return library.get(key, None).song if key in library else None

def get_singer(key):
    """Returns the singer for the given track key."""
    return library.get(key, None).singer if key in library else None

def set_rating(key):
    """Returns the rating for the given track key."""
    return library.get(key, None).rating if key in library else None

def get_play_count(key):
    """Returns the play count for the given track key."""
    return library.get(key, None).play_count if key in library else None

def update_play_count(key, new_play_count):
    """Updates the play count for the track with the given key."""
    if key in library:
        library[key].play_count = new_play_count
    else:
        print(f"Track {key} not found.")

