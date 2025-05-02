import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw
from core.image_processor import ImageProcessor
from gui.gui import GUI


class TkinterApp(GUI):
    def __init__(self, root):
        self.root = root
        self.image = None
        self.selected_action = tk.StringVar(value="canny")

        self.setup_ui()

    def setup_ui(self):
        self.root.title("🖼️ App name")
        self.root.geometry("500x600")
        self.root.configure(bg="#f0f0f0")

        #tk.Label(self.root, text="App name", font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#333").pack(pady=20)

        placeholder_img = Image.new('RGB', (250, 250), color="lightgray")
        draw = ImageDraw.Draw(placeholder_img)
        draw.text((95, 110), "No image", fill="white")
        self.placeholder_photo = ImageTk.PhotoImage(placeholder_img)

        self.img_label = tk.Label(self.root, image=self.placeholder_photo, bg="#ffffff", bd=2, relief="solid")
        self.img_label.image = self.placeholder_photo
        self.img_label.pack(pady=10)

        tk.Button(self.root, command=self.upload_image,
                  text="📂 Upload Image", font=("Arial", 12),
                  bg="#2196f3", fg="white", padx=10, pady=5).pack(pady=10)

        tk.Radiobutton(self.root, text="Canny edge detector", variable=self.selected_action, value="canny").pack()
        tk.Radiobutton(self.root, text="Sobel operator", variable=self.selected_action, value="sobel").pack()
        tk.Radiobutton(self.root, text="Prewitt operator", variable=self.selected_action, value="prewitt").pack()


        tk.Label(self.root, text="Threshold:", bg="#f0f0f0").pack()
        self.threshold_entry = tk.Entry(self.root)
        self.threshold_entry.insert(0, "100")  # domyślna wartość
        self.threshold_entry.pack(pady=5)

        tk.Button(self.root, command=self.apply_transformation,
                  text="Apply Filter", font=("Arial", 12),
                  bg="#673ab7", fg="white", padx=10, pady=5).pack(pady=20)



    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.image = Image.open(file_path).resize((250, 250))
            photo = ImageTk.PhotoImage(self.image)
            self.img_label.config(image=photo)
            self.img_label.image = photo

    def apply_transformation(self):
        if self.image is None:
            messagebox.showwarning("Warning", "Please upload an image first!")
            return

        try:
            threshold = int(self.threshold_entry.get())  # Pobierz wartość z inputa
        except ValueError:
            messagebox.showerror("Błąd", "Wprowadź poprawną wartość liczbową!")
            return

        try:
            transformed_image = ImageProcessor.apply_filter(self.image, self.selected_action.get(),threshold)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return

        photo = ImageTk.PhotoImage(transformed_image)

        new_window = tk.Toplevel()
        new_window.title("Transformed Image")
        label = tk.Label(new_window, image=photo)
        label.image = photo
        label.pack()

        def download_image():
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
            if file_path:
                transformed_image.save(file_path)

        tk.Button(new_window, text="Download Image", command=download_image).pack(pady=10)