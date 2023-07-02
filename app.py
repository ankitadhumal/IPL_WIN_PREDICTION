import streamlit as st
import pickle
import pandas as pd

#Dropdown Options
teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']

#Dropdown Options
cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru']


pipe = pickle.load(open('pipe.pkl','rb'))
st.title('IPL Win Predictor')

#st.beta_columns for 2 box in same line
col1, col2 = st.columns(2)
#Creating Variables to take input from user

with col1: #st.selectbox is for dropdown option
    batting_team = st.selectbox('Select the batting team',sorted(teams))
with col2: #st.selectbox is for dropdown option
    bowling_team = st.selectbox('Select the bowling team',sorted(teams))

#st.selectbox is for dropdown option
selected_city = st.selectbox('Select host city',sorted(cities))

#st.number_input is for taking value in number from user
target = st.number_input('Target')

col3,col4,col5 = st.columns(3) #st.beta_columns for 3 box in same line

with col3:
    score = st.number_input('Score')
with col4:
    overs = st.number_input('Overs completed')
with col5:
    wickets = st.number_input('Wickets out')

#st.button for button
if st.button('Predict Probability'):
    runs_left = target - score
    balls_left = 120 - (overs*6)
    wickets_left = 10 - wickets
    crr = score/overs
    rrr = (runs_left*6)/balls_left

#dataframe form.passing dictionary
    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets_left':[wickets_left],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    #To display we use st.header or st.text
    st.header(batting_team + "- " + str(round(win*100)) + "%")
    st.header(bowling_team + "- " + str(round(loss*100)) + "%")