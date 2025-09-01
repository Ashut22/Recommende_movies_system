# Movie Recommender System 🎬

An interactive web app that recommends movies similar to a selected movie using content-based filtering.

## Features
- Select a movie from a dropdown to get 5 similar movie recommendations.
- Displays movie posters alongside titles.
- Uses **TF-IDF vectorization** and **cosine similarity** for content-based recommendations.
- Clean and intuitive interface built with **Streamlit**.

## How It Works
1. Preprocessed movie data (`movie_list.pkl`) and similarity matrix (`similarity_tf_idf`) are loaded.  
2. User selects a movie from the dropdown.  
3. The app calculates the top 5 similar movies based on the similarity matrix.  
4. Movie posters are fetched from **TMDb API** and displayed with the movie names.

## Tech Stack
- Python, Pandas, NumPy  
- Scikit-learn (TF-IDF & cosine similarity)  
- Streamlit for the web interface  
- TMDb API for movie posters

## Screenshot
*(Optional: Add a screenshot of the app here)*

## Usage
Run the app locally with:
```bash
streamlit run app.py

