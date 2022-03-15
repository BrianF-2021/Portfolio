# from flask_app import app
# from flask import render_template,redirect,request,session,flash
from my_app.config.mysqlconnection import connectToMySQL
# from flask_app.models.user import User
from my_app import app
from flask import render_template, redirect, request, session
from my_app.models import date_time, user as usr, weather


@app.route('/weather')
def get_weather():
    # geo_locator.findCoord("MHT")
    # geo_locator.findCoord("Milford NH")
    #city_state = "Milford NH"
    city_state = "Rindge NH"
    weather_obj = weather.Weather(city_state)
    current_weather = weather_obj.get_current_weather_data()
    #my_weather = weather_obj.get_json_wx_data()
    dt = date_time.Date_Time()
    date,time = dt.get_current_datetime_formatted()

    return render_template("weather_page.html", current_weather = current_weather, city_state = city_state, date = date, time=time)

