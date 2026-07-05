from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Loads songs from a CSV file."""
    songs = []
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if not row.get("id"):
                continue
            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores a single song against user preferences."""
    # Expected return format: (score, reasons)
    GENRE_WEIGHT = 0.35
    MOOD_WEIGHT = 0.25
    ENERGY_WEIGHT = 0.25
    ACOUSTIC_WEIGHT = 0.15


    genre_match = 1 if song.get("genre") == user_prefs.get("genre") else 0
    mood_match = 1 if song.get("mood") == user_prefs.get("mood") else 0
    energy_match = 1 - abs(song.get("energy") - user_prefs.get("energy"))
    if user_prefs.get("likes_acoustic"):
        acoustic_match = song.get("acousticness")
    else:
        acoustic_match = 1 - song.get("acousticness")

    score = (GENRE_WEIGHT * genre_match) + (MOOD_WEIGHT * mood_match) + (ENERGY_WEIGHT * energy_match) + (ACOUSTIC_WEIGHT * acoustic_match)
    reasons = [
        f"\n\tUser genre ({user_prefs.get('genre')}) vs Song genre ({song.get('genre')}). Match: {genre_match:.2f}",
        f"\n\tUser mood ({user_prefs.get('mood')}) vs Song mood ({song.get('mood')}). Match: {mood_match:.2f}",
        f"\n\tUser energy: User ({user_prefs.get('energy')}) vs Song energy ({song.get('energy')}). Match: {energy_match:.2f}",
        f"\n\tUser likes acoustics ({user_prefs.get('likes_acoustic')}) vs Song acoustics ({song.get('acousticness')}). Match: {acoustic_match:.2f}"
    ]
    return (score, reasons)

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Functional implementation of the recommendation logic."""
    # Expected return format: (song_dict, score, explanation)

    song_scores = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        song_scores.append((song, score, ''.join(reasons)))
    song_scores.sort(key=lambda x: x[1], reverse=True)
    return song_scores[:k]
