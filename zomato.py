import pandas as pd
import streamlit as st

#Reading two files
reviews1 = pd.read_csv('reviews1_01.csv', encoding='ISO-8859-1')
data_cluster = pd.read_csv('data_cluster_01.csv', encoding='ISO-8859-1')


# Streamlit app
st.title("Angkasa Pura 2 Airport Review Dashboard 02")

# Filter cuisines
selected_cuisines = st.multiselect("Pilih Provinsi atau kota", data_cluster.columns[8:52])
if selected_cuisines:
    # Filter restaurants based on selected cuisines
    filtered_restaurants = data_cluster[data_cluster.apply(lambda row: any(cuisine in row["Cuisines"] for cuisine in selected_cuisines), axis=1)]

    # Display top 5 restaurants based on average ratings
    st.subheader("Bandara AP2 di area")
    top_restaurants = filtered_restaurants.sort_values(by="Rating", ascending=False).head(5)
    st.table(top_restaurants[["Name", "Rating"]])

    # Restaurant details
    selected_restaurant = st.selectbox("Pilih Bandara", top_restaurants["Name"])
    selected_reviews = reviews1[reviews1["Restaurant"] == selected_restaurant].head(5)

    # Display reviews
    st.subheader("Reviews")
    st.table(selected_reviews[["Reviewer", "Rating", "Review","Time"]])
else:
    st.info("Pilih Bandara untuk melihat review dan comment tiap bandara.")
