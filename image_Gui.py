import requests
import tkinter as tk
from tkinter import messagebox

def download_image():
    url = url_entry.get()
    file_name = name_entry.get()

    if not url or not file_name:
        messagebox.showerror("Error", "Please fill all fields")
        return

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10, stream=True)

        if response.status_code == 200:
            content_type = response.headers.get("Content-Type", "")

            if "image" not in content_type:
                messagebox.showerror("Error", "URL does not contain an image")
                return

            with open(file_name, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)

            messagebox.showinfo("Success", "Image downloaded successfully!")

        else:
            messagebox.showerror("Error", "Failed to download image")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- GUI ----------------

root = tk.Tk()
root.title("Image Downloader")
root.geometry("400x250")
root.resizable(False, False)

tk.Label(root, text="Image Downloader", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Image URL").pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

tk.Label(root, text="Save As (with .jpg/.png)").pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

tk.Button(root, text="Download Image", command=download_image,
          bg="green", fg="white", font=("Arial", 11, "bold")).pack(pady=15)

root.mainloop()
