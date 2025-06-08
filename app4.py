import streamlit as st
import pickle
import base64
import os

st.set_page_config(page_title="Student Domain Recommender", layout="wide")


def add_bg(image_file):
    if not os.path.exists(image_file):
        st.error(f"Background image not found: {image_file}")
        return
    with open(image_file, "rb") as img:
        encoded_string = base64.b64encode(img.read()).decode()

    st.markdown(
        f"""
        <style>
        
        .stApp {{
            background: none;
        }}
        .blurred-bg {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            filter: blur(8px) brightness(60%);
            z-index: -1;
        }}
        </style>
        
        """,
        unsafe_allow_html=True
    )


add_bg("img2.png")


model = pickle.load(open("model1.pkl", "rb"))


job_categories = {
    0: "CRM & Technical Support",
    1: "Data Science & Analytics",
    2: "Database & Data Management",
    3: "Management & Business",
    4: "Network & Security",
    5: "Software Development & Engineering",
    6: "Software Testing & Quality Assurance",
    7: "UI/UX & Design"
}


book_type_mapping = {
    "Action and Adventure": 0,
    "Anthology": 1,
    "Art": 2,
    "Autobiographies": 3,
    "Biographies": 4,
    "Childrens": 5,
    "Comics": 6,
    "Cookbooks": 7,
    "Diaries": 8,
    "Dictionaries": 9,
    "Drama": 10,
    "Encyclopedias": 11,
    "Fantasy": 12,
    "Guide": 13,
    "Health": 14,
    "History": 15,
    "Horror": 16,
    "Journals": 17,
    "Math": 18,
    "Mystery": 19,
    "Poetry": 20,
    "Prayer books": 21,
    "Religion-Spirituality": 22,
    "Romance": 23,
    "Satire": 24,
    "Science": 25,
    "Science fiction": 26,
    "Self help": 26,
    "Series": 28,
    "Travel": 29,
    "Trilogy": 30
}



def predict_model(os, algo, prog_concept, soft_eng, com_net, electronics, com_arch, maths, comm, int_type_books):
    input_data = [
        float(os), float(algo), float(prog_concept), float(soft_eng),
        float(com_net), float(electronics), float(com_arch), float(maths),
        float(comm), float(int_type_books)
    ]
    prediction = model.predict([input_data])
    return prediction[0]


def main():
    st.markdown("<h1 style='color: white;'>Student Domain Recommendation System</h1>", unsafe_allow_html=True)

    os = st.number_input("Marks in Operating Systems", 0.0, 100.0)
    algo = st.number_input("Marks in Algorithms", 0.0, 100.0)
    prog_concept = st.number_input("Marks in Programming Concepts", 0.0, 100.0)
    soft_eng = st.number_input("Marks in Software Engineering", 0.0, 100.0)
    com_net = st.number_input("Marks in Computer Networks", 0.0, 100.0)
    electronics = st.number_input("Marks in Electronics", 0.0, 100.0)
    com_arch = st.number_input("Marks in Computer Architecture", 0.0, 100.0)
    maths = st.number_input("Marks in Mathematics", 0.0, 100.0)
    comm = st.number_input("Marks in Communication Skills", 0.0, 100.0)

    book_choice = st.selectbox("Interested Type of Books", list(book_type_mapping.keys()))
    int_type_books = book_type_mapping[book_choice]

    if st.button("Predict"):
        try:
            result = predict_model(os, algo, prog_concept, soft_eng, com_net,
                                   electronics, com_arch, maths, comm, int_type_books)
            job_name = job_categories.get(result, "Unknown Category")
            st.success(f"Predicted Job Role: {job_name}")
        except Exception as e:
            st.error(f"Error during prediction: {e}")

    if st.button("About"):
        st.info("Created by Prince, Kaustubh, Pavani, Moitryee, and Snehal.")

if __name__ == "__main__":
    main()
