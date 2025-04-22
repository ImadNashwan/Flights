
# Import Necessary Libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


st.set_page_config(layout="wide", page_title = 'Simple DashBoard')
# Read Data
df = pd.read_csv('cleaned_df.csv', index_col= 0)
new_df = df[['ELAPSED_TIME', 'AIR_TIME', 'DISTANCE', 'ARRIVAL_DELAY','AIR_SYSTEM_DELAY' ]]
new_df.corr(numeric_only= True)


st.title('Fight Air Lines Data Report')
#new_df = df[['ELAPSED_TIME', 'AIR_TIME', 'DISTANCE', 'ARRIVAL_DELAY','AIR_SYSTEM_DELAY' ]]
#new_df.corr(numeric_only= True)

# Create title using html
#html_title = """<h1 style="color:white;text-align:center;"> Air Flight Report </h1>"""
#st.markdown(html_title,unsafe_allow_html=True)

st.image('Air Port.jpg')

# General Statistics
st.plotly_chart(px.histogram(df, x= 'AIRLINE', color='AIRLINE', title= 'The Air Lines Movement According Air Line Company'))
st.plotly_chart(px.pie(df, names= 'DAY_OF_WEEK', title='Percentage Distribution Air Lines Movement through the Day Week Number'))
st.plotly_chart(px.pie(df, names= 'Day_Cat', title='The Percentage Distribution of the Flights of The Air Lines Movement Through Period of Month Days '))
st.plotly_chart(px.pie(df, names= 'DEPARTURE_DELAY_Cat', title='The Percentage Distribution Flights of The Air Lines Movement Through Departue Time'))
st.plotly_chart(px.pie(df, names= 'ELAPSED_TIME_Cat', title='The Elapsed Time of the Air Flight Movments by Hours'))
st.plotly_chart(px.pie(df, names= 'AIR_TIME_Cat', color_discrete_sequence= ['red', 'blue', 'green', 'purple'], title='The Percentage Distribution Flights of The Air Lines Movement Through Departue Time in Hours'))
st.plotly_chart(px.pie(df, names= 'DISTANCE_Cat', title='The Percentage Distribution Flights of The Air Lines Movement Through Distance in Km'))
#st.plotly_chart()
#st.plotly_chart()

# Relation
st.plotly_chart(px.imshow(new_df.corr(numeric_only= True), title='The Relation between Delay Time Factors'))


# Columns
col1, col2=st.columns(2)
col1.write('### Cancelation of')
col2.write(('### Diverted of'))
# Canclled Flights

filtered_df = df.loc[df['CANCELLATION_REASON'] !='NO']

col1.plotly_chart(px.histogram(filtered_df, x= 'CANCELLATION_REASON', title= 'Number of Cancelled Trips of the Air Lines Movement According to the Reason', labels= {'CANCELLATION_REASON' : 'Reason of Cancelation'}))
col1.plotly_chart(px.histogram(df, x="AIRLINE", y="CANCELLED", title='The Cancelled Fight Through The Air Lines Movement According to the Air Line Company'))
col1.plotly_chart(px.histogram(df, x="DAY_OF_WEEK", y="CANCELLED", title='The Cancelled Fight Through The Air Lines Movement Through the Day of Week'))
col1.plotly_chart(px.histogram(df, x="Day_Cat", y="CANCELLED", title='The Cancelled Fight Through The Air Lines MovementThroug the Period of Month of Days'))
col1.plotly_chart(px.histogram(df, x="DISTANCE_Cat", y="CANCELLED", title='The Cancelled Fights of The Air Lines Movement Through Distamnce in Km'))
col1.plotly_chart(px.histogram(df, x="DEPARTURE_DELAY_Cat", y="CANCELLED", title='The Cancelled Fights of The Air Lines Movement Through Departue Time'))
#st.plotly_chart()
#st.plotly_chart()


# Diverted Flights
col2.plotly_chart(px.histogram(df, x="AIRLINE", y="DIVERTED", title='The Diverted Fights Through The Air Lines Movement Accroding to the Air Line Company'))
col2.plotly_chart(px.histogram(df, x="DAY_OF_WEEK", y="DIVERTED", title='The Diverted Fight Through The Air Lines Movement according the Day of Week'))
col2.plotly_chart(px.histogram(df, x="AIRLINE", y="DEPARTURE_DELAY", color='AIRLINE', title='The Departure Delayes of the Flight Movement Accrdng to the Air Lines Company'))

#st.plotly_chart()
#st.plotly_chart()
#st.plotly_chart()
#st.plotly_chart()





