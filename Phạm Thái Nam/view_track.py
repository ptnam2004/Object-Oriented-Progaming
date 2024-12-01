import tkinter as tk
import tkinter.scrolledtext as tkst
import tracks_library as lib  # Assuming lib is handling track data management
import font_manager as fonts

def set_text(text_area, content):
    """Helper function to set text in a Text or ScrolledText widget."""
    text_area.delete("1.0", tk.END)
    text_area.insert("1.0", content)

class Viewtracks:
    def __init__(self, window):
        window.geometry("750x350")
        window.title("View Tracks")

        # Button to list all tracks
        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        # Label and Entry for inputting track number
        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # Button to check specific track details
        check_track_btn = tk.Button(window, text="View Track", command=self.view_track_clicked)
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)

        # ScrolledText for displaying the list of tracks
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # Text for displaying individual track details
        self.tracks_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.tracks_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        # Status label
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

    def list_tracks_clicked(self):
        """Displays all tracks in the ScrolledText widget."""
        tracks_list = lib.list_all()  # Get list of all tracks from the library
        set_text(self.list_txt, tracks_list)
        self.status_lbl.configure(text="List All Tracks button was clicked!")

    def view_track_clicked(self):
        """Displays and updates track details when a track is checked."""
        key = self.input_txt.get()
        song = lib.get_song(key)  # Fetch the song details by key
        if song:
            singer = lib.get_singer(key)
            rating = lib.set_rating(key)
            play_count = lib.get_play_count(key)
            
            # Increment the play count
            play_count += 1
            lib.update_play_count(key, play_count)  # Update the play count in the library
            
            # Display the updated track details
            track_details = f"{song}\n{singer}\nRating: {rating}\nPlays: {play_count}"
            set_text(self.tracks_txt, track_details)
        else:
            set_text(self.tracks_txt, f"Track {key} not found")
        
        self.status_lbl.configure(text="Check Track button was clicked!")

if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()  # Configure fonts using font_manager
    Viewtracks(window)  # Instantiate the Viewtracks window
    window.mainloop()
