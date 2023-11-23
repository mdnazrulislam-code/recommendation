import streamlit as st 
import pickle
import pandas as pd 
import requests


css = '''
<style>
    [data-testid="stSidebar"]{
        min-width: 400px;
        max-width: 800px;
    }
</style>
'''
st.set_page_config(page_title="Movie Recommendation System", layout="wide")
st.markdown(css, unsafe_allow_html=True)



def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=bc8e9c009edbbaae181ac7badbc5a273&language=en-US")
    data = response.json()
    
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


st.title('Movie Recommender System')


movies_dict = pickle.load(open('data/movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('data/similarity.pkl', 'rb'))

selected_movie_name = st.selectbox(
    'Select a movie ',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommendations = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0], use_column_width='auto')
    with col2:
        st.text(names[1])
        st.image(posters[1], use_column_width='auto')

    with col3:
        st.text(names[2])
        st.image(posters[2], use_column_width='auto')
    with col4:
        st.text(names[3])
        st.image(posters[3], use_column_width='auto')

    with col5:
        st.text(names[4])
        st.image(posters[4], use_column_width='auto')

    with col1:
        st.text(names[5])
        st.image(posters[5], use_column_width='auto')
    with col2:
        st.text(names[6])
        st.image(posters[6], use_column_width='auto')

    with col3:
        st.text(names[7])
        st.image(posters[7], use_column_width='auto')
    with col4:
        st.text(names[8])
        st.image(posters[8], use_column_width='auto')

    with col5:
        st.text(names[9])
        st.image(posters[9], use_column_width='auto')
