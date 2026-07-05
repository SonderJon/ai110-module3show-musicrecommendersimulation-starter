# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

### Phase 1
Streaming platofrms like Spotify analyze song metadata (title, artists, genre, etc) and audio data.
Then, using the song analytics and user history, songs are recommended that fit a user's preferences or that users with similar preferences have enjoyed
This system will prioritize genre, mood, energy, and acousrticness for recommendations
score = (genre_match * w1) + (mood_match * w2) + (energy_closeness * w3) + (acoustic_fit * w4)
The above score can be modified with weights to prioritize different attributes

### Phase 2
User profile:<br>
    favorite_genre: str<br>
    favorite_mood: str<br>
    target_energy: float<br>
    likes_acoustic: bool<br>
Finalized scoring: (0.35 × genre_match) + (0.25 × mood_match) + (0.25 × energy_match) + (0.15 × acoustic_match)
Genre match has the most weight, followed by mood and energy, then accoustics being the least important.
If likes_acoustic is True, acoustic_match = acousticness.
Else, acoustic_match = 1 - acousticness (the inverse)
This system places more weight on genre, biasing towards users who prioritize genre rather than mood or energy, for example
Planned flow:<br>
    Input: user preferences
    Process: parse input, loop through songs with scoring system, rank scored songs
    Output: top recommendations
---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



