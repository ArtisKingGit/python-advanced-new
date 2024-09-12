from customtkinter import *
from PIL import Image
from tkintermapview import *

app = CTk()

app.geometry("1280x720")
app.title("Map")

widget = TkinterMapView(app, width =600, height = 400)
widget.pack(fill = "both", expand=True)

widget.set_address("Nairobi Kenya",marker=True)


app.mainloop()

