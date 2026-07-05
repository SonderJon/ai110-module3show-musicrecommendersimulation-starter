"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    user_prefs_1 = {"genre": "pop", "mood": "happy", "energy": 0.8, "likes_acoustic": True}

    # Profile 2
    user_prefs_2 = {"genre": "edm", "mood": "energetic", "energy": 0.9, "likes_acoustic": False}

    # Extreme user prefs
    user_prefs_extreme = {"genre": "metal", "mood": "intense", "energy": 1.0, "likes_acoustic": False}

    # Conflicting acoustics
    user_prefs_conflicting = {"genre": "classical", "mood": "sad", "energy": 0.0, "likes_acoustic": True}


    print("USER 1")
    recommendations = recommend_songs(user_prefs_1, songs, k=5)

    print("\nTop recommendations:\n")
    for rec in recommendations:
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()
    
    print("USER 2")
    recommendations = recommend_songs(user_prefs_2, songs, k=5)

    print("\nTop recommendations:\n")
    for rec in recommendations:
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()
    
    print("USER 3")
    recommendations = recommend_songs(user_prefs_extreme, songs, k=5)

    print("\nTop recommendations:\n")
    for rec in recommendations:
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()
    
    print("USER 4")
    recommendations = recommend_songs(user_prefs_conflicting, songs, k=5)

    print("\nTop recommendations:\n")
    for rec in recommendations:
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()


if __name__ == "__main__":
    main()
