import pickle
import streamlit as st
import requests

# Page Config
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🎬 Movie Recommender System</h1>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="text-align: center; font-size:18px; margin-top:20px;">
        <b>Welcome to the AI-powered Movie Recommender 🎥 <br>
        Just select a movie you like, and we’ll suggest 5 similar movies along with their posters.</b>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
        /* Hide the Streamlit header */
        header {visibility: hidden;}
        
        /* Hide the footer */
        footer {visibility: hidden;}
        
        /* Hide the top-right hamburger menu */
        #MainMenu {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

# Function to fetch posters from TMDB
def fetch_poster(movie_id):
    api_key = "4edd85b9fb58c71196ff9fd9850ed867"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters


# Load data
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity_tf_idf','rb'))


col1, col2,col3,col4,col5,col6= st.columns(6)


with col1:
    st.image("https://image.tmdb.org/t/p/w500//z7uo9zmQdQwU5ZJHFpv2Upl30i1.jpg", width=200)

with col2:
    st.image("https://image.tmdb.org/t/p/w500//aotTZos5KswgCryEzx2rlOjFsm1.jpg", width=200)
with col3:
    st.image("https://media.themoviedb.org/t/p/w440_and_h660_face/rzRb63TldOKdKydCvWJM8B6EkPM.jpg", width=200)
with col4:
    st.image("https://image.tmdb.org/t/p/w500//4yIQq1e6iOcaZ5rLDG3lZBP3j7a.jpg",width = 200)
with col5:
    st.image("https://image.tmdb.org/t/p/w500//43d0IzrPaapqrYRHkfKfnpSNEKm.jpg",width = 200)
with col6:
    st.image("https://image.tmdb.org/t/p/w500//iKP6wg3c6COUe8gYutoGG7qcPnO.jpg",width = 200)




st.markdown("---")

# ----------------- Recommender Section -----------------
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "🎞️ Type or select a movie from the dropdown:",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(recommended_movie_names[i])
            st.image(recommended_movie_posters[i])
