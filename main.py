import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1530525555924-ea911cdf2a2c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8ZjElMjB3YWxscGFwZXJ8ZW58MHx8MHx8&w=1000&q=80");
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

data = pd.read_csv("C:/Users/Savri/Downloads/F1/f1_2010-2021/f1_2010-2021.csv")
driver = pd.read_csv("C:/Users/Savri/Downloads/F1/f1_2010-2021/driver_standings_2010-2021.csv")
team = pd.read_csv("C:/Users/Savri/Downloads/F1/f1_2010-2021/constructor_standings_2010-2021.csv")
circuits = pd.read_csv("C:/Users/Savri/Downloads/circuits.csv")

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