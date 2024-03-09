class Song:
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}

    def __init__(self,name,artist,genre) -> None:
        self.artist = artist
        self.genre = genre
        self.name =name
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

        
    @classmethod   
    def add_song_to_count(cls):
        cls.count+= 1

    
    @classmethod
    def add_to_genres(cls,genre):
        cls.genres.add(genre)

    @classmethod
    def add_to_artists(cls,artist):
        cls.artists.add(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1


song1 = Song("Shape of You", "Ed Sheeran", "Pop")
song2 = Song("Out of Touch", "Hall & Oates", "Pop")
song3 = Song("99 Problems", "Jay Z", "Rap")

print(f"Total songs: {Song.count}")
print(f"Genres: {Song.genres}")
print(f"Artists: {Song.artists}")
print(f"Genre count: {Song.genre_count}")
print(f"Artist count: {Song.artist_count}")