# FilmFinder Movie Recommendation App

A simple movie recommendation project using Python, Streamlit, and a movie dataset.
The app suggests similar movies based on tags created from movie overview, genres, keywords, cast, and crew.

## Files

- `app.py` - Streamlit application front end.
- `Movie_Rating_Prediction_With_Python.py` - Python script that builds the recommendation model and defines `recommend()`.
- `Movie_Rating_Prediction_With_Python.ipynb` - Notebook with the preprocessing and model creation steps.
- `movies.pkl` - Pickled movie DataFrame used by the app.
- `tmdb_5000_movies.csv` - Movie dataset file.
- `tmdb_5000_credits.csv` - Credits dataset file.
- `requirements.txt` - Python dependencies.

## How it works

1. Preprocesses movie metadata: overview, genres, keywords, cast, and crew.
2. Converts text to tags and vectorizes them.
3. Computes cosine similarity between movies.
4. Recommends the top 5 movies similar to the selected title.

## Install

1. Open a terminal in the `Week1` folder.
2. Create a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

> Note: `ast` and `pickle` are part of Python standard library, so they do not need separate installation.

## Run the app

In the `Week1` folder, run:

```powershell
streamlit run app.py
```

Then open the local URL shown in the terminal.

## Use the app

- Choose a movie from the drop-down menu.
- Click `Find Similar Movies`.
- The app shows five recommended movies based on similarity.

## If you want to rebuild the model

1. Open `Movie_Rating_Prediction_With_Python.ipynb` or run `Movie_Rating_Prediction_With_Python.py`.
2. Make sure the CSV files are in the same folder.
3. Generate `movies.pkl` again with the same preprocessing steps.

## Notes

- `app.py` loads `movies.pkl` and calls `recommend()` from `Movie_Rating_Prediction_With_Python.py`.
- Keep `movies.pkl` in the same folder as `app.py`.