# streamlit run pto_tool.py
# importing libraries for python
import streamlit as st
import numpy as np
import pandas as pd
import datetime as dt


# introduction titles for the page
st.title("PTO TOOL (Calculator)")
st.write("Hello! This tool will help you calculate the number of remaining PTO hours for anyone.")
st.write("Thank you!")


# asking for employee name, start date and end date
employee_name = st.text_input("Please enter employee's name you want to calculate for!")
start_date = st.date_input("Please enter first day of work")
end_date = st.date_input("Please enter last day of work")


# taking users vacation and sick PTO hours
vacation_pto_hours_used = st.number_input("Please enter the number of vacation PTO hours used already", min_value = 00.00, max_value = 120.00)
sick_pto_hours_used = st.number_input("Please enter the number of sick PTO hours used already", min_value = 00.00, max_value = 120.00)


# calculating the current year
x = dt.datetime.now()
current_year = x.year


# calculating total number of days worked by the employee
total_delta = end_date - start_date
total_num_of_days = total_delta.days + 1


# calculating number of days worked in the current year
start_date_year = start_date.year
currentyear_firstdate = dt.date(current_year, 1, 1)

if start_date_year < current_year:
    delta = end_date - currentyear_firstdate
    current_num_of_days = delta.days + 1
else:
    delta = end_date - start_date
    current_num_of_days = delta.days + 1


# choosing employee type between Corporate and Property
employee_type = st.radio("Please choose between Corporate or Property (Employee Type)", ("Corporate", "Property"), index = 0)


# if employee type is corporate
if employee_type == "Corporate":
    st.write(employee_name + " has worked a total of " + str(total_num_of_days) + " days for the company.") # total number of days
    st.write(employee_name + " has worked " + str(current_num_of_days) + " days for the company in the current year.") # number of days in current year


    vacation_pto = round(current_num_of_days * (120.00/365.00), 2) # calculating vacation pto and rounding it to 2 decimal points.
    sick_pto = round(current_num_of_days * (40.00/365.00), 2) # calculating vacation pto and rounding it to 2 decimal points.


    st.write(employee_name + " is elgible for " + str(round(vacation_pto, 2)) + " vacation PTO hours out of 120 hours in the current year.")
    st.write(employee_name + " is elgible for " + str(round(sick_pto, 2)) + " sick PTO hours out of 40 hours in the current year.")
    st.write(employee_name + " has used " + str(round(vacation_pto_hours_used, 2)) + " vacation PTO hours in the current year.")
    st.write(employee_name + " has used " + str(round(sick_pto_hours_used, 2)) + " sick PTO hours in the current year.")


    if vacation_pto_hours_used > vacation_pto:
        st.write(employee_name + " owes the company " + str(round((vacation_pto_hours_used - vacation_pto), 2)) + " vacation PTO hours for the current year.")
        st.write(employee_name + " owes the company " + str(round((sick_pto_hours_used - sick_pto), 2)) + " sick PTO hours for the current year.")
    else:
        st.write(" The company owes " + str(round((vacation_pto - vacation_pto_hours_used), 2)) + " vacation PTO hours to " + employee_name + " for the current year.")
        st.write(" The company owes " + str(round((sick_pto - sick_pto_hours_used), 2)) + " sick PTO hours to " + employee_name + " for the current year.")


# if employee type is property
else:
    st.write(employee_name + " has worked a total of " + str(total_num_of_days) + " days for the company.")
    st.write(employee_name + " has worked " + str(current_num_of_days) + " days for the company in the current year.")


    vacation_pto = round(current_num_of_days * (80.00/365.00), 2) # calculating vacation pto and rounding it to 2 decimal points.
    sick_pto = round(current_num_of_days * (40.00/365.00), 2) # calculating vacation pto and rounding it to 2 decimal points.


    st.write(employee_name + " is elgible for " + str(round(vacation_pto, 2)) + " vacation PTO hours out of 80 hours in the current year.")
    st.write(employee_name + " is elgible for " + str(round(sick_pto, 2)) + " sick PTO hours out of 40 hours in the current year.")
    st.write(employee_name + " has used " + str(round(vacation_pto_hours_used, 2)) + " vacation PTO hours in the current year.")
    st.write(employee_name + " has used " + str(round(sick_pto_hours_used, 2)) + " sick PTO hours in the current year.")


    if vacation_pto_hours_used > vacation_pto:
        st.write(employee_name + " owes the company " + str(round((vacation_pto_hours_used - vacation_pto), 2)) + " vacation PTO hours for the current year.")
        st.write(employee_name + " owes the company " + str(round((sick_pto_hours_used - sick_pto), 2)) + " sick PTO hours for the current year.")
    else:
        st.write(" The company owes " + str(round((vacation_pto - vacation_pto_hours_used), 2)) + " vacation PTO hours to " + employee_name + " for the current year.")
        st.write(" The company owes " + str(round((sick_pto - sick_pto_hours_used), 2)) + " sick PTO hours to " + employee_name + " for the current year.")