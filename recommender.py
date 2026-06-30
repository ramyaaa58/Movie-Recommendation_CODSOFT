# Movie Recommendation System

## Overview

The Movie Recommendation System is a beginner-friendly desktop application built with Python and Tkinter. It uses content-based filtering, TF-IDF vectorization, and cosine similarity to recommend movies that are similar to the one selected by the user.

## Features

- Search a movie by name
- Recommend the top 10 similar movies
- Clear the recommendations
- Exit the application
- Random Movie button for quick suggestions
- About and Help dialogs for guidance

## Technologies Used

- Python
- Tkinter
- Pandas
- NumPy
- Scikit-learn
- Pillow (optional)

## Recommendation Algorithm

The recommendation engine uses:

- **TF-IDF Vectorizer** to convert movie text features into numerical vectors
- **Cosine Similarity** to measure similarity between movies based on combined content

Important movie fields are combined into a single text feature, including title, genre, description, director, and cast.

## Installation

1. Create and activate a Python virtual environment.
2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python main.py
```

## Dataset

The project includes a sample `movies.csv` dataset with movie titles, genres, descriptions, director names, cast lists, and ratings.

## Screenshots

> Add screenshots here after you run the app.

## Future Improvements

- Add real movie poster thumbnails with Pillow
- Load a larger dataset
- Add keyword-based search suggestions
- Support collaborative filtering and user ratings
- Connect to an online movie database API
