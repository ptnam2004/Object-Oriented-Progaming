import tkinter as tk
from tkinter import ttk, messagebox

def load_list():
    try:
        with open('track_list.txt', 'r') as file:
            return [line.strip().split(',') for line in file.readlines()]
    except FileNotFoundError:
        messagebox.showerror("Error", "track list file not found!")
        return []

def save_list(tracks):
    with open('track_list.txt', 'w') as file:
        for title, url in tracks:
            file.write(f"{title},{url}\n")

def update_tracks(title, new_url):
    if not title or not new_url:
        messagebox.showwarning("Input Error", "Both title and URL must be provided.")
        return
    tracks = load_list()
    for track in tracks:
        if track[0] == title:
            track[1] = new_url
            break
    else:
        messagebox.showwarning("Not Found", "tracks not found in the list.")
        return
    save_list(tracks)
    messagebox.showinfo("Success", "tracks updated!")

def delete_tracks(title):
    if not title:
        messagebox.showwarning("Input Error", "Title must be provided.")
        return
    Tracks = load_list()
    new_tracks = [track for track in Tracks if track[0] != title]
    if len(new_tracks) == len(Tracks):
        messagebox.showwarning("Not Found", "tracks not found in the list.")
        return
    save_list(new_tracks)
    messagebox.showinfo("Success", "tracks deleted!")

def main():
    root = tk.Tk()
    root.title("Update tracks")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)

    ttk.Label(frame, text="track Title:").grid(row=0, column=0, sticky=tk.W)
    title_entry = ttk.Entry(frame)
    title_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

    ttk.Label(frame, text="New URL:").grid(row=1, column=0, sticky=tk.W)
    url_entry = ttk.Entry(frame)
    url_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

    ttk.Button(frame, text="Update track", command=lambda: update_tracks(title_entry.get().strip(), url_entry.get().strip())).grid(row=2, column=0, columnspan=2, pady=5)
    ttk.Button(frame, text="Delete tracks", command=lambda: delete_tracks(title_entry.get().strip())).grid(row=3, column=0, columnspan=2, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()