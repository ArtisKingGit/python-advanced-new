from customtkinter import *
from CTkTable import CTkTable
from PIL import Image
from subprocess import call


app = CTk()
app.geometry("856x645")
app.resizable(0,0)
app.title("School Bookshop")

set_appearance_mode("light")



def open_orders():
    app.destroy()
    call(["python", "Orders.py"])
    
def open_feedback():
    app.destroy()  # Destroy the current window
    call(["python", "feedback.py"])
    
def open_settings():
    app.destroy()
    call(["python", "settings.py"])
    
def open_returns():
    app.destroy()
    call(["python", "returns.py"])
    
sidebar_frame = CTkFrame(master=app, fg_color="#2A8C55", width=176, height=650, corner_radius=0)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(fill="y", anchor="w", side="left")

#The logo for the app
logo_img_data = Image.open("logo.png")
logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(77.68, 85.42))
CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(pady=(38, 0), anchor="center")

#Analytics
analytics_img_data = Image.open("analytics_icon.png")
analytics_img = CTkImage(dark_image=analytics_img_data, light_image=analytics_img_data)
CTkButton(master=sidebar_frame, image=analytics_img, text="Dashboard", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(60, 0))

#Feedback
feedback_img_data = Image.open("feedback_icon.png")
feedback_img = CTkImage(dark_image= feedback_img_data, light_image= feedback_img_data)
CTkButton(master = sidebar_frame, image = feedback_img, text = "Feedback", fg_color= "transparent", font = ("Arial Bold", 14), hover_color="#207244", anchor = "w", command= open_feedback).pack(anchor = "center", ipady =5, pady = (16, 0 ))
 
#Orders
#package_img_data = Image.open("package_icon.png")
#package_img = CTkImage(light_image=package_img_data)
#CTkButton(master=sidebar_frame, image=package_img, text="Orders", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w", command=open_orders).pack(anchor="center", ipady=5, pady=(16, 0))


#List of Orders
list_img_data = Image.open("list_icon.png")
list_img = CTkImage(dark_image=list_img_data, light_image=list_img_data)
CTkButton(master=sidebar_frame, image=list_img, text="List of Orders", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

#Returns
returns_img_data = Image.open("returns_icon.png")
returns_img = CTkImage(dark_image=returns_img_data, light_image=returns_img_data)
CTkButton(master=sidebar_frame, image=returns_img, text="Returns", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w", command= open_returns).pack(anchor="center", ipady=5, pady=(16, 0))

#Settings
settings_img_data = Image.open("settings_icon.png")
settings_img = CTkImage(dark_image=settings_img_data, light_image=settings_img_data)
CTkButton(master=sidebar_frame, image=settings_img, text="Settings", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w", command= open_settings).pack(anchor="center", ipady=5, pady=(16, 0))

#Account Signed in 
person_img_data = Image.open("person_icon.png")
person_img = CTkImage(dark_image=person_img_data, light_image=person_img_data)
btn_accounts = CTkButton(master=sidebar_frame, image=person_img, text="Account", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(160, 0))

#Left Pannel
main_view = CTkFrame(master=app, fg_color="#fff",  width=680, height=650, corner_radius=0)
main_view.pack_propagate(0)
main_view.pack(side="left")

#The Title Frame
title_frame = CTkFrame(master=main_view, fg_color="transparent")
title_frame.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))

CTkLabel(master=title_frame, text="Orders", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="nw", side="left")

CTkButton(master=title_frame, text="+ New Order",  font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55", hover_color="#207244", command= open_orders).pack(anchor="ne", side="right")

#The metrics frame
metrics_frame = CTkFrame(master=main_view, fg_color="transparent")
metrics_frame.pack(anchor="n", fill="x",  padx=27, pady=(36, 0))

orders_metric = CTkFrame(master=metrics_frame, fg_color="#2A8C55", width=200, height=60)
orders_metric.grid_propagate(0)
orders_metric.pack(side="left")

#Logistics
logitics_img_data = Image.open("logistics_icon.png")
logistics_img = CTkImage(light_image=logitics_img_data, dark_image=logitics_img_data, size=(43, 43))

CTkLabel(master=orders_metric, image=logistics_img, text="").grid(row=0, column=0, rowspan=2, padx=(12,5), pady=10)

CTkLabel(master=orders_metric, text="Orders", text_color="#fff", font=("Arial Black", 15)).grid(row=0, column=1, sticky="sw")
CTkLabel(master=orders_metric, text="123", text_color="#fff",font=("Arial Black", 15), justify="left").grid(row=1, column=1, sticky="nw", pady=(0,10))

#Shipping Frame
shipped_metric = CTkFrame(master=metrics_frame, fg_color="#2A8C55", width=200, height=60)
shipped_metric.grid_propagate(0)
shipped_metric.pack(side="left",expand=True, anchor="center")

shipping_img_data = Image.open("shipping_icon.png")
shipping_img = CTkImage(light_image=shipping_img_data, dark_image=shipping_img_data, size=(43, 43))

CTkLabel(master=shipped_metric, image=shipping_img, text="").grid(row=0, column=0, rowspan=2, padx=(12,5), pady=10)

CTkLabel(master=shipped_metric, text="Shipping", text_color="#fff", font=("Arial Black", 15)).grid(row=0, column=1, sticky="sw")
CTkLabel(master=shipped_metric, text="91", text_color="#fff",font=("Arial Black", 15), justify="left").grid(row=1, column=1, sticky="nw", pady=(0,10))

delivered_metric = CTkFrame(master=metrics_frame, fg_color="#2A8C55", width=200, height=60)
delivered_metric.grid_propagate(0)
delivered_metric.pack(side="right",)

delivered_img_data = Image.open("delivered_icon.png")
delivered_img = CTkImage(light_image=delivered_img_data, dark_image=delivered_img_data, size=(43, 43))

CTkLabel(master=delivered_metric, image=delivered_img, text="").grid(row=0, column=0, rowspan=2, padx=(12,5), pady=10)

CTkLabel(master=delivered_metric, text="Delivered", text_color="#fff", font=("Arial Black", 15)).grid(row=0, column=1, sticky="sw")
CTkLabel(master=delivered_metric, text="23", text_color="#fff",font=("Arial Black", 15), justify="left").grid(row=1, column=1, sticky="nw", pady=(0,10))

search_container = CTkFrame(master=main_view, height=50, fg_color="#F0F0F0")
search_container.pack(fill="x", pady=(45, 0), padx=27)

CTkEntry(master=search_container, width=305, placeholder_text="Search Order", border_color="#2A8C55", border_width=2).pack(side="left", padx=(13, 0), pady=15)

CTkComboBox(master=search_container, width=125, values=["Date", "Most Recent Order", "Least Recent Order"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff").pack(side="left", padx=(13, 0), pady=15)
CTkComboBox(master=search_container, width=125, values=["Status", "Processing", "Confirmed", "Packing", "Shipping", "Delivered", "Cancelled"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff").pack(side="left", padx=(13, 0), pady=15)

#Tables
table_data = [
    ["Order ID", "Item Name", "Customer", "Address", "Status", "Quantity"],
    ['3833', 'Smartphone', 'Arthur', '123 main St', 'Confirmed', '8'],
    ['6432', 'Laptop', 'Patrick', '456 Elm St', 'Packing', '5'],
    ['2180', 'Tablet', 'Jacinta', '789 Oak St', 'Delivered', '1'],
    ['5438', 'Headphones', 'Zedi', '101 Pine St', 'Confirmed', '9'],
    ['9144', 'Camera', 'Boniface', '202 Cedar St', 'Processing', '2'],
    ['7689', 'Printer', 'Nathan', '303 Maple St', 'Cancelled', '2'],
    ['1323', 'Smartwatch', 'Jumba', '404 Birch St', 'Shipping', '6'],
    ['7391', 'Keyboard', 'Curtis', '505 Redwood St', 'Cancelled', '10'],
    ['4915', 'Monitor', 'Benjamin', '606 Fir St', 'Shipping', '6'],
    ['5548', 'External Hard Drive', 'Baraka', '707 Oak St', 'Delivered', '10'],
    ['5485', 'Table Lamp', 'Alvie', '808 Pine St', 'Confirmed', '4'],
    ['7764', 'Desk Chair', 'Kaice', '909 Cedar St', 'Processing', '9'],
    ['8252', 'Coffee Maker', 'Stanley', '1010 Elm St', 'Confirmed', '6'],
    ['2377', 'Blender', 'Lincon', '1111 Redwood St', 'Shipping', '2'],
    ['5287', 'Toaster', 'Ty Barack', '1212 Maple St', 'Processing', '1'],
    ['7739', 'Microwave', 'Jijo', '1313 Cedar St', 'Confirmed', '8'],
    ['3129', 'Refrigerator', 'Morgan', '1414 Oak St', 'Processing', '5'],
    ['4789', 'Vacuum Cleaner', 'Armon James', '1515 Pine St', 'Cancelled', '10']
]

table_frame = CTkScrollableFrame(master=main_view, fg_color="transparent")
table_frame.pack(expand=True, fill="both", padx=27, pady=21)
table = CTkTable(master=table_frame, values=table_data, colors=["#E6E6E6", "#EEEEEE"], header_color="#2A8C55", hover_color="#B4B4B4")
table.edit_row(0, text_color="#fff", hover_color="#2A8C55")
table.pack(expand=True)

app.mainloop()