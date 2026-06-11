import streamlit as st
import pickle
import Movie_Rating_Prediction_With_Python as nb

movies_list = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_list['title'].values

st.title('FilmFinder')

select_movie_name = st.selectbox(
'Pick a movie you love:',
(movies_list))


if st.button("Find Similar Movies"):
    data = nb.recommend(select_movie_name)
    st.subheader("Top Recommendations")

    badge_bg = "#1A1B26"
    badge_text = "#7AA2F7"
    movie_text = "#BB9AF7"
    border_color = "#24283B"

    for idx, movie in enumerate(data):
        html_layout = f'<div style="display: flex; align-items: center; font-family: \'Segoe UI\', Helvetica, Arial, sans-serif; padding: 8px 0; border-bottom: 1px solid {border_color}; margin-bottom: 4px;"><span style="background-color: {badge_bg}; color: {badge_text}; font-weight: bold; padding: 2px 8px; border-radius: 4px; font-size: 14px; margin-right: 15px;">#{idx+1}</span><span style="color: {movie_text}; font-size: 18px; font-weight: 500;">{movie}</span></div>'

        st.markdown(html_layout, unsafe_allow_html=True)