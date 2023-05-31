# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 00:46:52 2020

@author: Matt
"""

import requests
import tkinter as tk

HEIGHT = 400
WIDTH = 600

def get(event):
    text = event.widget.get()
    get_weather(text)
    
def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        
        final_str = 'City: %s \nConditions: %s \nTemperature (F): %s' % (name, desc, temp)
    except:
        final_str = 'An error occurred while \nretreiving the information'
    
    return final_str

def get_weather(city):
    API_key = '<API KEY FOR OPENWEATHER HERE>'
    url = 'http://api.openweathermap.org/data/2.5/weather?'
    params = {'APPID': API_key, 'q':city,'units':'Imperial'}
    response = requests.get(url, params = params)
    weather = response.json()
    label['text'] = format_response(weather)

    
root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

back_image = tk.PhotoImage(file='background_image.png')
background_label = tk.Label(root, image= back_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg = "#80c1ff", bd=5)
frame.place(anchor='n',relwidth=0.7, relheight=0.1, relx=0.5, rely=0.1)

entry = tk.Entry(frame, font=('Calibri', 14))
entry.bind('<Return>',get)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text = "Get Weather", bg = "gray", fg = "white", command=lambda: get_weather(entry.get()))
button.place(relx=.7, rely=0, relwidth=0.3 , relheight=1)

lower_frame = tk.Frame(root, bg = "#80c1ff", bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.7, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, bg='white', font=('Calibri',16))
label.place(relwidth=1, relheight=1)

root.mainloop()
