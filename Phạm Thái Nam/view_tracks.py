import tkinter as tk
import tkinter.scrolledtext as tkst
import font_manager as fonts
import tracks_library as lib  
from view_track import Viewtracks
from tkinter import messagebox
from tkinter import filedialog
import csv

class LibraryItem:
    def __init__(self, song, singer, rating):
        self.song = song
        self.singer = singer
        self.rating = rating
        self.play_count = 0
    
    def info(self):
        return f"{self.song} by {self.singer}, rated {self.rating}, played {self.play_count} times"

    @staticmethod
    def read_library(file_path):
        items = []
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader) 
            for row in reader:
                if len(row) >= 3:
                    song, singer, rating = row[:3]
                    items.append(LibraryItem(song, singer, int(rating)))
        return items

class ViewTracks:
    def __init__(self, root):
        self.root = root
        self.library_items = []
        self.create_widgets()

    def create_widgets(self):
        self.library_listbox = tk.Listbox(self.root, width=50, height=15)
        self.library_listbox.grid(row=4, column=0, columnspan=4, pady=10)

    def view_track(self):
        Viewtracks(tk.Toplevel(self.root))

    def create_track_list(self):
        messagebox.showinfo("Track List", "Track list created!")

    def update_tracks(self):
        update_window = tk.Toplevel(self.root)
        update_window.geometry("300x200")
        update_window.title("Update Track Rating")

        tk.Label(update_window, text="Track Key:").pack(pady=5)
        entry_key = tk.Entry(update_window)
        entry_key.pack(pady=5)
        
        tk.Label(update_window, text="New Rating:").pack(pady=5)
        entry_rating = tk.Entry(update_window)
        entry_rating.pack(pady=5)
        
        def update_rating():
            key = entry_key.get()
            new_rating = entry_rating.get()
            try:
                new_rating = int(new_rating)
                lib.set_rating(new_rating)
                messagebox.showinfo("Success", f"Updated rating for {key} to {new_rating}")
            except ValueError:
                messagebox.showerror("Error", "Invalid rating value")
            update_window.destroy()

        tk.Button(update_window, text="Update", command=update_rating).pack(pady=10)

    def load_library(self):
        file_path = "tracks_library.csv"
        self.library_items = LibraryItem.read_library(file_path)
        self.update_library()

    def update_library(self):
        self.library_listbox.delete(0, tk.END)
        for item in self.library_items:
            self.library_listbox.insert(tk.END, item.info())

def import_track_list(listbox, status_lbl):
    status_lbl.configure(text="Import Track List button was clicked!")
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            listbox.delete(0, tk.END)  
            for track in reader:
                listbox.insert(tk.END, track)

def export_track_list(listbox, status_lbl):
    status_lbl.configure(text="Export Track List button was clicked!")
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_path:
        with open(file_path, mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Key", "Song", "Singer", "Rating", "Play Count"])
            for key, track in lib.library.items():
                writer.writerow([key, track.song, track.singer, track.rating, track.play_count])
        status_lbl.configure(text="Track list exported successfully")
    else:
        status_lbl.configure(text="Export cancelled")
    
def increment_play_count(key):
    try:
        item = lib[key]
        item.play_count += 1
    except KeyError:
        return

    

window = tk.Tk()
window.geometry("520x400")
window.title("View Tracks")

fonts.configure()

header_lbl = tk.Label(window, text="Select an option by clicking one of the buttons below")
header_lbl.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

view_tracks = ViewTracks(window)

check_videos_btn = tk.Button(window, text="View Tracks", command=lambda: Viewtracks(tk.Toplevel(window)))
check_videos_btn.grid(row=1, column=0, padx=10, pady=10)

create_track_list_btn = tk.Button(window, text="Create Track List", command=view_tracks.create_track_list)
create_track_list_btn.grid(row=1, column=1, padx=10, pady=10)

update_tracks_btn = tk.Button(window, text="Update Tracks", command=view_tracks.update_tracks)
update_tracks_btn.grid(row=1, column=2, padx=10, pady=10)

btn_import_track_list = tk.Button(window, text="Import Track List", command=lambda: import_track_list(view_tracks.library_listbox, status_lbl))
btn_import_track_list.grid(row=2, column=0, padx=10, pady=10)

btn_export_track_list = tk.Button(window, text="Export Track List", command=lambda: export_track_list(view_tracks.library_listbox, status_lbl))
btn_export_track_list.grid(row=2, column=1, padx=10, pady=10)

status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
status_lbl.grid(row=3, column=0, columnspan=4, padx=10, pady=10)



window.mainloop()
