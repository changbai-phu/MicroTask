import streamlit as stm
from streamlit_extras.stodo import to_do 
from call_db import DatabaseManager, SessionManager
import calendar_setup as cal_st
from datetime import datetime
import time 
  
# Setup database
# db_name = "goal_tracker.db"
# db_manager = DatabaseManager(db_name=db_name)
# db_manager.create_table()

stm.set_page_config(page_title="This is a Simple Streamlit WebApp") 
stm.title("This is the Home Page Geeks.") 
stm.text("Geeks Home Page") 

def display_calendar():
    calendar = calendar(
    events=cal_st.calendar_events,
    options=cal_st.calendar_options,
    custom_css=cal_st.custom_css,
    key='calendar', # Assign a widget key to prevent state loss
    )
    stm.write(calendar)
# 
# def add_event():
# 
# def pomodoro_timer():
# 
# def main_app():
# 
if __name__ == "__main__":
    # main_app()
    display_calendar()