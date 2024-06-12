import tkinter as tk
import json
import urllib.request
import requests

from io import BytesIO
from PIL import ImageTk, Image


def display_image(image_url):
    with urllib.request.urlopen(image_url) as url:
        image_data = url.read()

    image_stream = BytesIO(image_data)
    image = ImageTk.PhotoImage(Image.open(image_stream))

    image_label.config(image=image)
    image_label.image = image


def get_image_url():

    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiY2JiMDBmYzMtNWNmMi00OTllLTg4MDgtNTQ5Yjk4NTM1M2YxIiwidHlwZSI6ImFwaV90b2tlbiJ9.JDUJUMdzN0WXOjrA48dw1ta3GFt9gb0v7Xzh1X4MepE"}

    url = "https://api.edenai.run/v2/image/generation"
    payload = {
        "providers": "openai",
        "text": input_field.get(),
        "resolution": "512x512",
        "fallback_providers": ""
    }

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)

    return result['openai']['items'][0]['image_resource_url']


def render_image():
    print("Generating")

    try:
        error_label.place_forget()
        image_url = get_image_url()
    except KeyError:
        error_label.place(x=500, y=105)
    else:
        display_image(image_url)


window = tk.Tk()
window.title("AI Image Generator")
window.geometry("1000x750")

error_label = tk.Label(window, text="Prompt can not be empty!", fg="red")

input_field = tk.Entry(window, width=20)
input_field.place(x=440, y=90)

image_label = tk.Label(window)
image_label.place(x=250, y=150)

generate_button = tk.Button(window, text="Create", height=1, bg="black", fg="white", command=render_image)
generate_button.place(x=565, y=85)

window.mainloop()
