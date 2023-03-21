# Import relevant modules
import subprocess
import webbrowser
import tkinter as tk

# Start the Django server in a subprocess
def start_server():
    subprocess.Popen(["python3", "manage.py", "runserver"])

# Stop the Django server
def stop_server():
    subprocess.run(["pkill", "-f", "runserver"])

# Open the web page in the user's browser
def open_browser():
    webbrowser.open("http://127.0.0.1:8000/")

# Create the GUI window
root = tk.Tk()
root.geometry("300x200")
root.title("eBookstore Manager")

# Create a label and button for starting the server and opening the web page
label = tk.Label(root, text="Welcome to the eBookstore Manager!")
label.pack(pady=10)

button_start = tk.Button(root, text="Start eBookstore Server", command=start_server)
button_start.pack(pady=5)

button_open = tk.Button(root, text="Open eBookstore in Browser", command=open_browser)
button_open.pack(pady=5)

button_stop = tk.Button(root, text="Stop eBookstore Server", command=stop_server)
button_stop.pack(pady=5)

# Start the TKinter event loop, keeping the GUI window open and running
root.mainloop()
