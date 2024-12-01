class LibraryItem:
    def __init__(self, song, singer, rating=0):
        self.song = song
        self.singer = singer
        self.rating = rating
        self.play_count = 0
        if not self.validate_song(song):
            raise ValueError(f"Invalid song: {song}")
        if not self.validate_singer(singer):
            raise ValueError(f"Invalid singer: {singer}")
        if not self.validate_rating(rating):
            raise ValueError(f"Invalid rating: {rating}")
    def increment_play_count(self):
        """Increments the play count by 1."""
        self.play_count += 1

    def get_details(self):
        """Returns formatted details of the track."""
        return f"{self.song}\n{search_by_singer}\nRating: {self.rating}\nPlays: {self.play_count}"
    def validate_song(self, song):
        return isinstance(song, str) and bool(song.strip())

    def validate_singer(self, singer):
        return isinstance(singer, str) and bool(singer.strip())

    def validate_rating(self, rating):
        return isinstance(rating, int) and 0 <= rating <= 5

    def info(self):
        return f"{self.song} - {self.singer} {self.stars()}"

    def stars(self):
        stars = ""
        for i in range(self.rating):
            stars += "*"
        return stars
    
library = [
    
    LibraryItem("Shape of You", "Ed Sheeran", 5),
    LibraryItem("Blinding Lights", "The Weeknd", 4),
    LibraryItem("Rolling in the Deep", "Adele", 5),
    LibraryItem("Someone Like You", "Adele", 4),
]
def search_by_song(song):
    results = []
    for item in library:
        if song.lower() in item.song.lower():
            results.append(item)
    return results

def search_by_singer(singer):
    results = []
    for item in library:
        if singer.lower() in item.singer.lower():
            results.append(item)
    return results

def search_by_singer(singer):
    results = []
    for item in library:
        if singer.lower() == item.singer.lower():
            results.append(item)
    return results

search_results = search_by_song("Shape of You")
for result in search_results:
    print(result.info())

search_results = search_by_singer("Ed Sheeran")
for result in search_results:
    print(result.info())

search_results = search_by_song("Shape of You")
for result in search_results:
    print(result.info())
# libraryitem.py




    

