import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("data:image/jpeg;base64,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");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

col1, col2, col3 = st.columns(3)
with col2:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/F1.svg/420px-F1.svg.png", width=200)

data = pd.read_csv("f1_2010-2021.csv")
driver = pd.read_csv("driver_standings_2010-2021.csv")
team = pd.read_csv("constructor_standings_2010-2021.csv")
circuits = pd.read_csv("circuits.csv")

tab1, tab2, tab3, tab4 = st.tabs(['Home', 'Team Wins-comparison', 'Driver Points-comparison','Driver and constructor standings'])
with tab1:
    st.write("Formula One (also known as Formula 1 or F1) is the highest class of international racing for open-wheel"
             " single-seater formula racing cars sanctioned by the Fédération Internationale de l'Automobile (FIA). "
             "The World Drivers' Championship, which became the FIA Formula One World Championship in 1981, has been "
             "one of the premier forms of racing around the world since its inaugural season in 1950. "
             "The word formula in the name refers to the set of rules to which all participants' cars must conform. "
             "A Formula One season consists of a series of races, known as Grands Prix, which take place worldwide "
             "on both purpose-built circuits and closed public roads.")
    st.header("Locations of Grand Prix")
    st.map(circuits)

with tab2:
    st.header("How would you like to see the data?")
    way1 = st.checkbox("According to Year")
    way2 = st.checkbox("According to Grand Prix")
    if way1:
        way2 = None
        selectbox = st.selectbox(
            "Select any one of the following years",
            (data['year'].unique())
        )
        st.write("Total wins of a team in the respective year:")
        data1 = data[data['year'] == selectbox]
        fig1 = plt.figure(figsize=(10, 4))
        plt.bar(data1['team'].unique(), data1['team'].value_counts(), color='#69b3a2')
        st.pyplot(fig1)


        st.write("Cumulative wins of team till the respective year:")
        for i in range(0, data.shape[0]):
            if selectbox == data['year'][i]:
                 newdata = data[:i]
        fig2 = plt.figure(figsize=(10, 4))
        plt.barh(newdata['team'].unique(), newdata['team'].value_counts(), color='#69b3a2')
        st.pyplot(fig2)

    if way2:
        way1 = None
        selectbox2 = st.selectbox(
            "Select any one of the following countries",
            (data['grand_prix'].unique())
        )
        data2 = data[data['grand_prix'] == selectbox2]
        fig = plt.figure(figsize=(10, 4))
        plt.bar(data2['team'].unique(), data2['team'].value_counts(), color='#69b3a2')
        st.pyplot(fig)

with tab3:
    st.header("Choose 2 drivers to compare")
    col6, col7 = st.columns(2)
    with col6:
        participant1 = st.selectbox("Select Driver 1", driver['fullname'].unique())
    with col7:
        participant2 = st.selectbox("Select Driver 2", driver['fullname'].unique())

    fig3 = plt.figure(figsize=(10, 4))
    data3 = driver[driver['fullname'] == participant1]
    data4 = driver[driver['fullname'] == participant2]
    plt.plot(data3['year'], data3['points'])
    plt.plot(data4['year'], data4['points'])
    plt.legend([participant1, participant2])
    st.pyplot(fig3)

with tab4:
    st.header("Driver and Constructor Standings in a particular year")
    selectbox3 = st.selectbox("Select a year to see driver and constructor standings", driver['year'].unique())
    col4, col5 = st.columns(2)
    with col4:
        for i in range(0, driver.shape[0]):
            if selectbox3 == driver['year'][i]:
                st.write(driver.iloc[i, 3] + "'s  Points:", driver.iloc[i, 5])
    with col5:
        for i in range(0, team.shape[0]):
            if selectbox3 == team['year'][i]:
                st.write(team.iloc[i, 1] + "'s Points:", team.iloc[i, 2])
