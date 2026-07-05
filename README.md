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

User Profile: genre = pop, mood = happy, energy = 0.8, likes acoustic = True<br>
Listing top 5 recommendations
```
Top recommendations:

Sunrise City - Score: 0.87
Because: 
        User genre (pop) vs Song genre (pop). Match: 1.00
        User mood (happy) vs Song mood (happy). Match: 1.00
        User energy: User (0.8) vs Song energy (0.82). Match: 0.98
        User likes acoustics (True) vs Song acoustics (0.18). Match: 0.18

Gym Hero - Score: 0.57
Because: 
        User genre (pop) vs Song genre (pop). Match: 1.00
        User mood (happy) vs Song mood (intense). Match: 0.00
        User energy: User (0.8) vs Song energy (0.93). Match: 0.87
        User likes acoustics (True) vs Song acoustics (0.05). Match: 0.05

Rooftop Lights - Score: 0.54
Because: 
        User genre (pop) vs Song genre (indie pop). Match: 0.00
        User mood (happy) vs Song mood (happy). Match: 1.00
        User energy: User (0.8) vs Song energy (0.76). Match: 0.96
        User likes acoustics (True) vs Song acoustics (0.35). Match: 0.35

Backyard Anthem - Score: 0.53
Because:
        User genre (pop) vs Song genre (country). Match: 0.00
        User mood (happy) vs Song mood (happy). Match: 1.00
        User energy: User (0.8) vs Song energy (0.7). Match: 0.90
        User likes acoustics (True) vs Song acoustics (0.4). Match: 0.40

Velvet Sway - Score: 0.51
Because:
        User genre (pop) vs Song genre (soul). Match: 0.00
        User mood (happy) vs Song mood (happy). Match: 1.00
        User energy: User (0.8) vs Song energy (0.58). Match: 0.78
        User likes acoustics (True) vs Song acoustics (0.45). Match: 0.45
```

User Profile: genre = edm, mood = energetic, energy = 0.9, likes acoustic = False<br>
Listing top 5 recommendations
```
Top recommendations:

Grid Runner - Score: 0.98
Because: 
        User genre (edm) vs Song genre (edm). Match: 1.00
        User mood (energetic) vs Song mood (energetic). Match: 1.00
        User energy: User (0.9) vs Song energy (0.95). Match: 0.95
        User likes acoustics (False) vs Song acoustics (0.02). Match: 0.98

Gym Hero - Score: 0.39
Because: 
        User genre (edm) vs Song genre (pop). Match: 0.00
        User mood (energetic) vs Song mood (intense). Match: 0.00
        User energy: User (0.9) vs Song energy (0.93). Match: 0.97
        User likes acoustics (False) vs Song acoustics (0.05). Match: 0.95

Storm Runner - Score: 0.38
Because: 
        User genre (edm) vs Song genre (rock). Match: 0.00
        User mood (energetic) vs Song mood (intense). Match: 0.00
        User energy: User (0.9) vs Song energy (0.91). Match: 0.99
        User likes acoustics (False) vs Song acoustics (0.1). Match: 0.90

Broken Circuit - Score: 0.38
Because: 
        User genre (edm) vs Song genre (metal). Match: 0.00
        User mood (energetic) vs Song mood (intense). Match: 0.00
        User energy: User (0.9) vs Song energy (0.97). Match: 0.93
        User likes acoustics (False) vs Song acoustics (0.03). Match: 0.97

Sunrise City - Score: 0.35
Because: 
        User genre (edm) vs Song genre (pop). Match: 0.00
        User mood (energetic) vs Song mood (happy). Match: 0.00
        User energy: User (0.9) vs Song energy (0.82). Match: 0.92
        User likes acoustics (False) vs Song acoustics (0.18). Match: 0.82
```

User Profile: genre = metal, mood = intense, energy = 1.0, likes acoustic = False<br>
Listing top 5 recommendations
```
Top recommendations:

Broken Circuit - Score: 0.99
Because: 
        User genre (metal) vs Song genre (metal). Match: 1.00
        User mood (intense) vs Song mood (intense). Match: 1.00
        User energy: User (1.0) vs Song energy (0.97). Match: 0.97
        User likes acoustics (False) vs Song acoustics (0.03). Match: 0.97

Gym Hero - Score: 0.62
Because: 
        User genre (metal) vs Song genre (pop). Match: 0.00
        User mood (intense) vs Song mood (intense). Match: 1.00
        User energy: User (1.0) vs Song energy (0.93). Match: 0.93
        User likes acoustics (False) vs Song acoustics (0.05). Match: 0.95

Storm Runner - Score: 0.61
Because: 
        User genre (metal) vs Song genre (rock). Match: 0.00
        User mood (intense) vs Song mood (intense). Match: 1.00
        User energy: User (1.0) vs Song energy (0.91). Match: 0.91
        User likes acoustics (False) vs Song acoustics (0.1). Match: 0.90

Grid Runner - Score: 0.38
Because: 
        User genre (metal) vs Song genre (edm). Match: 0.00
        User mood (intense) vs Song mood (energetic). Match: 0.00
        User energy: User (1.0) vs Song energy (0.95). Match: 0.95
        User likes acoustics (False) vs Song acoustics (0.02). Match: 0.98

Sunrise City - Score: 0.33
Because: 
        User genre (metal) vs Song genre (pop). Match: 0.00
        User mood (intense) vs Song mood (happy). Match: 0.00
        User energy: User (1.0) vs Song energy (0.82). Match: 0.82
        User likes acoustics (False) vs Song acoustics (0.18). Match: 0.82
```

User Profile: genre = classical, mood = intense, energy = 0.0, likes acoustic = True<br>
Listing top 5 recommendations
```
Top recommendations:

Paper Moons - Score: 0.95
Because: 
        User genre (classical) vs Song genre (classical). Match: 1.00
        User mood (sad) vs Song mood (sad). Match: 1.00
        User energy: User (0.0) vs Song energy (0.2). Match: 0.80
        User likes acoustics (True) vs Song acoustics (0.97). Match: 0.97

Spacewalk Thoughts - Score: 0.32
Because: 
        User genre (classical) vs Song genre (ambient). Match: 0.00
        User mood (sad) vs Song mood (chill). Match: 0.00
        User energy: User (0.0) vs Song energy (0.28). Match: 0.72
        User likes acoustics (True) vs Song acoustics (0.92). Match: 0.92

Desert Mirage - Score: 0.31
Because: 
        User genre (classical) vs Song genre (folk). Match: 0.00
        User mood (sad) vs Song mood (relaxed). Match: 0.00
        User energy: User (0.0) vs Song energy (0.31). Match: 0.69
        User likes acoustics (True) vs Song acoustics (0.94). Match: 0.94

Library Rain - Score: 0.29
Because: 
        User genre (classical) vs Song genre (lofi). Match: 0.00
        User mood (sad) vs Song mood (chill). Match: 0.00
        User energy: User (0.0) vs Song energy (0.35). Match: 0.65
        User likes acoustics (True) vs Song acoustics (0.86). Match: 0.86

Coffee Shop Stories - Score: 0.29
Because: 
        User genre (classical) vs Song genre (jazz). Match: 0.00
        User mood (sad) vs Song mood (relaxed). Match: 0.00
        User energy: User (0.0) vs Song energy (0.37). Match: 0.63
        User likes acoustics (True) vs Song acoustics (0.89). Match: 0.89
```
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



