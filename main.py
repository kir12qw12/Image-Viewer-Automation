from playwright.sync_api import sync_playwright
import requests
import time
from PIL import Image, ImageTk
import tkinter as tk

# Сайт с рандомной картинкой
IMG_URL = "https://picsum.photos/1920/1080"
IMG_PATH = "random.jpg"

def show_fullscreen(path):
    root = tk.Tk()
    root.attributes("-fullscreen", True)

    img = Image.open(path)
    tk_img = ImageTk.PhotoImage(img)  # <-- вот это ключ: используем ImageTk.PhotoImage

    label = tk.Label(root, image=tk_img)
    label.pack()

    root.after(5000, root.destroy)  # 5 секунд
    root.mainloop()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://picsum.photos/")

    # Скачиваем картинку
    r = requests.get(IMG_URL)
    with open(IMG_PATH, "wb") as f:
        f.write(r.content)

    browser.close()

# Показываем на весь экран
show_fullscreen(IMG_PATH)
