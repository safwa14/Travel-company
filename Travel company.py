import streamlit as st
from PIL import Image

# 🎨 خلفية الصفحة
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1506744038136-46273834b3fb");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 💬 باقي التطبيق
st.title("Welcome to Al Safwa Tourism Company 🧳")

days = st.number_input("How many days will you stay?", min_value=1, max_value=365, step=1)
preference = st.selectbox("Do you prefer a sea or mountain view?", ["Sea", "Mountain"])
budget = st.selectbox("What is your budget?", ["Large", "Medium", "Small"])

if st.button("Get Recommendation"):
    st.subheader("Based on your preferences:")

    if preference.lower() == "sea":
        if budget.lower() == "large":
            st.success("🏝 Maldives")
        elif budget.lower() == "medium":
            st.success("🏖 Turkiye")
        else:
            st.success("🌅 Dahab")
    elif preference.lower() == "mountain":
        if budget.lower() == "large":
            st.success("🏞 Switzerland")
        elif budget.lower() == "medium":
            st.success("🌄 Georgia")
        else:
            st.success("🏔 Mount St. Catherine")

    st.info("Thank you for choosing Al Safwa 😊")

              
               
