import customtkinter as ctk
from make_requests import MakeRequests
from tkinter import *

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

class ScrollFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, data=None, **kwargs):
        super().__init__(master, **kwargs)
        self.frames = []
        self.init_data(data)

    def init_data(self, data):
        if not data:
            return self.frames.append(DataFrame(master=self))
        for city in data[0]:
            label_text =\
f"""
    Name: {city["name"]}, {city["country"]}
        Current Temperature: {city["temp"]} C
        Humidity: {city["humidity"]}%
        Clouds:  {city["clouds_percent"]}% of sky covered by clouds
        Weather : {city["clouds"]}
        Weather description: {city["weather_desc"]}
"""
            self.frames.append(DataFrame(self, label_text=label_text).pack(fill="x", padx=5, expand=True))
        if data[1] and data[2]:
            self.frames.append(DataFrame(self, label_text=f"Avg. Temperature: {data[1]}").pack(fill="x", padx=5, expand=True))
            self.frames.append(DataFrame(self, label_text=f"Coldest City: {data[2]}").pack(fill="x", padx=5, expand=True))

        for frame in self.frames:
            if frame != None:
                frame.pack()


class DataFrame(ctk.CTkFrame):
    def __init__(self, master, label_text="Data goes here...", **kwargs):
        super().__init__(master, **kwargs)
        self.label = ctk.CTkLabel(self, text=label_text)
        self.label.pack(fill="x", padx=5)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.init_window()
        self.requester = MakeRequests()

    def init_window(self):
        self.title('Weather App Demo')
        self.minsize(width=800, height=400)
        self.init_ui()

    def init_scroll_frame(self, data=None):
        try:
            self.scroll_frame._parent_frame.destroy()
        except AttributeError:
            pass
        finally:
            self.scroll_frame = ScrollFrame(master=self.inner_grid, data=data, corner_radius=0, fg_color="transparent")
            self.scroll_frame.pack(fill="both", expand=True)

    def init_ui(self):
        self.inner_grid = ctk.CTkFrame(self)
        self.inner_grid.grid_rowconfigure(0, weight=1)
        self.inner_grid.grid_columnconfigure(0, weight=1)
        self.inner_grid.pack(side='right', fill='both', expand=True, padx=5, pady=5)
        self.init_scroll_frame()

        self.get_rand_button = ctk.CTkButton(self, text="Get 5 cities", command=self.get_random_cites)
        self.get_rand_button.pack(side="top", fill="y", pady=(10, 0))

        self.input_label = ctk.CTkLabel(self, text="Enter desired city name:")
        self.input_label.pack(pady=(10, 0), fill="x")

        self.input_textbox = ctk.CTkEntry(self, placeholder_text="Type here...")
        self.input_textbox.pack(pady=(5, 10), padx=20, fill="x")

        self.get_named_button = ctk.CTkButton(self, text="Get!", command=self.get_named_city)
        self.get_named_button.pack(side="top", fill="y", pady=(10, 0))


    def get_random_cites(self):
        data = self.requester.collect_cities()
        self.init_scroll_frame(data=data)

    def get_named_city(self):
        city = self.input_textbox.get()
        if city:
            data = self.requester.get_by_name(city)
            self.init_scroll_frame(data=data)
        else:
            print("No data to lookup, please enter a city.")

if __name__ == '__main__':
    app = App()
    app.mainloop()

