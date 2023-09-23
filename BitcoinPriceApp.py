import tkinter as tk
import requests
from datetime import datetime

# Function to update Bitcoin price
def updatePrice():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        price = data["bpi"]["USD"]["rate"][:-2]
        lastUpdated = data["time"]["updated"]
        price_label.config(text = f"Price: ${price}")
        updated_label.config(text = f"Last Updated: {lastUpdated}")
    except Exception as e:
        price_label.config(text = "Error fetching data.")
        
# Create the main application window
app = tk.Tk()
app.title("Bitcoin Price App")
app.geometry("400x200")
app.configure(bg = "#effeff")

# Create and configure labels
app_name_label = tk.Label(app, text="Bitcoin Price App", font=("Helvetica", 18), bg="#effeff", fg="#1580c2")
price_label = tk.Label(app, text="Price: ", font=("Helvetica", 14), bg="#effeff", fg="#1580c2")
updated_label = tk.Label(app, text="Last Updated: ", font=("Helvetica", 12), bg="#effeff", fg="#1580c2")

# Create and configure update button
update_button = tk.Button(app, text="Update Price", font=("Helvetica", 12), bg="#1580c2", fg="#effeff", command=updatePrice)

# Place labels and button on the grid
app_name_label.pack(pady=20)
price_label.pack(pady=10)
updated_label.pack(pady=10)
update_button.pack()

# Initially update Bitcoin price
updatePrice()

# Start the Tkinter event loop
app.mainloop()