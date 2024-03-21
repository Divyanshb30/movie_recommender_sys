import streamlit as st
import pickle
import requests

movies_name = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_name['title'].values
similarity = pickle.load(open('similarity.pkl', 'rb'))


def rec(movie):
    movie_index = movies_name[movies_name['title'] == movie].index[0]
    movies = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_names = []
    recommended_posters = []
    for j in movies:
        movie_id = movies_name.iloc[j[0]]['id']
        recommended_names.append(movies_name.iloc[j[0]]['title'])
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_names,recommended_posters


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


st.title('CinReco Recommender')

selected_movie_name = st.selectbox(
    'What do you feel like watching?',
    movies_list
)

if st.button('Recommend'):
    recommended_movie_names, recommended_movie_posters = rec(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

