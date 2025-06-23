import streamlit as st

st.markdown("""
╔═══╦╗─╔═══╗───╔═╗────────╔════╗──────────────╔═══╗
║╔═╗║║─║╔═╗║───║╔╝────────║╔╗╔╗║──────────────║╔═╗║
║║─║║║─║╚══╦══╦╝╚╦╗╔╗╔╦══╗╚╝║║╠╩═╦╗╔╦═╦╦══╦╗╔╗║║─╚╬══╦╗╔╦══╦══╦═╗╔╗─╔╗
║╚═╝║║─╚══╗║╔╗╠╗╔╣╚╝╚╝║╔╗║──║║║╔╗║║║║╔╬╣══╣╚╝║║║─╔╣╔╗║╚╝║╔╗║╔╗║╔╗╣║─║║
║╔═╗║╚╗║╚═╝║╔╗║║║╚╗╔╗╔╣╔╗║──║║║╚╝║╚╝║║║╠══║║║║║╚═╝║╚╝║║║║╚╝║╔╗║║║║╚═╝║
╚╝─╚╩═╝╚═══╩╝╚╝╚╝─╚╝╚╝╚╝╚╝──╚╝╚══╩══╩╝╚╩══╩╩╩╝╚═══╩══╩╩╩╣╔═╩╝╚╩╝╚╩═╗╔╝
────────────────────────────────────────────────────────║║───────╔═╝║
────────────────────────────────────────────────────────╚╝───────╚══╝
""")

st.title("Welcome to Al Safwa Tourism Company 🧳")

days = st.number_input("How many days will you stay?", min_value=1, max_value=365, step=1)
preference = st.selectbox("Do you prefer a sea or mountain view?", ["Sea", "Mountain"])
budget = st.selectbox("What is your budget?", ["Large", "Medium", "Small"])

if st.button("Get Recommendation"):
    if preference.lower() == "sea":
        if budget.lower() == "large":
            st.success("We recommend Maldives.🏝️ 🏝️ 🏝️")
        elif budget.lower() == "medium":
            st.success("We recommend Turkiye. 🏖️ 🏖️ 🏖️")    
        elif budget.lower() == "small":
            st.success("We recommend Dahab. 🌅 🌅 🌅") 
    elif preference.lower() == "mountain":
        if budget.lower() == "large":
            st.success("We suggest you visit Switzerland. 🏞️ 🏞️ 🏞️")
        elif budget.lower() == "medium": 
            st.success("We suggest you visit Georgia. 🌄 🌄 🌄") 
        elif budget.lower() == "small":
            st.success("We suggest you visit Mount St. Catherine. 🏔️ 🏔️ 🏔️ ")
    st.info("Thank you for choosing our company. 😊")


              
               
