from tkinter import messagebox
import requests
from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.geometry("500x500")
window.title("Current Weather Forecasts")

image_path = "output-onlinepngtools.png"
def resize_image(image_path, new_width, new_height):
    img_pil = Image.open(image_path)
    img_resized = img_pil.resize((new_width, new_height), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img_resized)
    return img_tk

resized_image = resize_image(image_path, 300, 200)
label = Label(image=resized_image)
label.pack(anchor="center")

font = ['Ariel',15,'normal']
label1 = Label(font=font,text="Enter the city:")
label1.place(x=20,y=200)

city_entry = Entry(width=12)
city_entry.place(x=130,y=200)

def clear_frame():
    for widget in frame.winfo_children():
        widget.destroy()
def search():
    entry_content = city_entry.get()
    if not entry_content:
        messagebox.showwarning(message="Please enter a city name first.",title="Error!")
    else:
        clear_frame()
        city = city_entry.get()
        target_url = f"http://api.weatherapi.com/v1/current.json?key=7cc62caa739747899bc161433240802&q={city}&aqi=no"
        response = requests.get(target_url).json()
        label1 = Label(frame, text="City:",font=font, bg="#C6C1C0")
        label1.place(x=20,y=10)

        label2 = Label(frame, font=font, bg="#C6C1C0", text=response['location']['name'])
        label2.place(x=60, y=10)

        country_label = Label(frame, text="Country:", font=font, bg="#C6C1C0")
        country_label.place(x=20, y=40)

        country = Label(frame, font=font, bg="#C6C1C0", text=response['location']['country'])
        country.place(x=90, y=40)

        temp_label = Label(frame, text="Temperature:", font=font, bg="#C6C1C0")
        temp_label.place(x=20, y=70)

        temperature = Label(frame, font=font, bg="#C6C1C0", text=f"{response['current']['temp_c']} C | {response['current']['temp_f']} F")
        temperature.place(x=120, y=70)

        condition_label = Label(frame, text="Condition:", font=font, bg="#C6C1C0")
        condition_label.place(x=20, y=100)

        condition = Label(frame, font=font, bg="#C6C1C0", text=response['current']['condition']['text'])
        condition.place(x=100, y=100)

        feelslike_label = Label(frame, text="Feels Like:", font=font, bg="#C6C1C0")
        feelslike_label.place(x=20,y=130)

        feelslike = Label(frame, font=font, bg="#C6C1C0", text=f"{response['current']['feelslike_c']} C | {response['current']['feelslike_f']} F")
        feelslike.place(x=100, y=130)

        datetime_label = Label(frame, text="Last Updated:", font=font, bg="#C6C1C0")
        datetime_label.place(x=20, y=160)

        datetimeshow = Label(frame, font=font, bg="#C6C1C0", text=response['current']['last_updated'])
        datetimeshow.place(x=120,y=160)


search_button = Button(font=font,text="Search",width=6,height=1,command=search)
search_button.place(x=270,y=200)

def clear_func():
    clear_frame()
    city_entry.delete(0,END)

clear_button = Button(font=font,text="Clear",width=6,height=1,command=clear_func)
clear_button.place(x=380,y=200)

frame = Frame(window, width=430, height=230, bg="#C6C1C0")
frame.place(x=30,y=250)
frame.pack_propagate(False)

def info():
    messagebox.showinfo(message="The weather updates every 15 minutes.")

info_button = Button(font=font,text="Info",width=1,height=1,command=info)
info_button.place(x=425,y=10)

window.mainloop()
