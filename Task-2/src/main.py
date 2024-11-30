import customtkinter as ctk
from make_requests import MakeRequests

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

class MyFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.label = ctk.CTkLabel(self, text="Where data goes...")
        self.label.pack(fill="both", padx=20)



class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.init_window()
        self.requester = MakeRequests()

    def init_window(self):
        self.title('Weather App Demo')
        self.minsize(width=800, height=400)
        self.init_ui()

    def init_scroll_frame(self):
        self.my_frame = MyFrame(master=self.inner_grid, corner_radius=0, fg_color="transparent")
        self.my_frame.pack(fill="both")


    def init_ui(self):
        self.inner_grid = ctk.CTkFrame(self)
        self.inner_grid.pack(side='right', fill='both', expand=True, padx=5, pady=5)
        self.init_scroll_frame()

        self.get_rand_button = ctk.CTkButton(self, text="Get 5 cities", command=self.get_random_cites)
        self.get_rand_button.pack(side="top", fill="y", pady=(10, 0))

        self.input_label = ctk.CTkLabel(self, text="Enter desired city name:")
        self.input_label.pack(pady=(10, 0), fill="x")

        self.input_textbox = ctk.CTkEntry(self, placeholder_text="Type here...")
        self.input_textbox.pack(pady=(5, 10), padx=20, fill="x")

        self.get_named_button = ctk.CTkButton(self, text="Get!", command=self.get_random_cites)
        self.get_named_button.pack(side="top", fill="y", pady=(10, 0))

    def get_random_cites(self):
        data = self.requester.collect_cities()
        print(data)

if __name__ == '__main__':
    app = App()
    app.mainloop()

