from urllib import response
import streamlit as st
import pickle
import requests 


movies = pickle.load(open("movie.pkl","rb"))


similarity = pickle.load(open("similarity.pkl","rb"))

# def decompress_pickle(file):

#     data = bz2.BZ2File(file, 'rb')
#     data = pickle.load(data)
#     return data

# similarity = decompress_pickle('simi.pbz2')

def fetch_poster(movie_id):

    data = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=26ddc1b99298c03a4bd756cfcfb3c5e9")
    # poster_path = data['poster_path']
    data = data.json()
    poster_path = data['poster_path']
    
    return f"https://image.tmdb.org/t/p/original/{poster_path}"

def recommend(movie_name):

    movie_index = movies[movies['title'] == movie_name].index[0]
    distances = similarity[movie_index]
    
    top = sorted(list(enumerate(distances)),reverse=True , key=lambda x: x[1])[1:7]
    
    movies_recommended = []
    movies_poster = []
    for i in top:
        movies_recommended.append(movies.title.iloc[i[0]])

        movie_id = movies.id.iloc[i[0]]
        movies_poster.append(fetch_poster(movie_id))
        
    return movies_recommended ,movies_poster

st.title("Movie Recommendation System")
movie_name = st.selectbox("Movie Name for recommendation" , movies['title'] )

if st.button("Recommend"):

    name,posters = recommend(movie_name)

    col1, col2,col3 = st.columns(3)
    col4,col5,col6 = st.columns(3)

    with col1:
        st.text(name[0])
        st.image(posters[0])
    with col2:
        st.text(name[1])
        st.image(posters[1])
    with col3:
        st.text(name[2])
        st.image(posters[2])
    with col4:
        st.text(name[3])
        st.image(posters[3])
    with col5:
        st.text(name[4])
        st.image(posters[4])
    with col6:
        st.text(name[5])
        st.image(posters[5])


    



