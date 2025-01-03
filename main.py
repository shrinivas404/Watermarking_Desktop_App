from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageDraw

window = Tk()
window.title("Watermarking Desktop App")
window.maxsize(600, 600)

# watermark function
def watermark_my_image():
    file_path = filedialog.askopenfilename(title="Open Image File",
                                           filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico")])
    image = Image.open(file_path)
    img_1 = ImageDraw.Draw(image)
    img_1.text((30,30), text = text_entry.get(), font_size=40)
    image.show()
    image.save(f"{edited_image_name.get()}.jpg")

# Entry
text_entry = Entry(width=40)
text_entry.grid(row=0, column=0, padx=20, pady=20)

# buttons
watermark_button = Button(text="Watermark", padx=10, pady=10, command=watermark_my_image)
watermark_button.grid(row=0, column=1)

edited_image_name = Entry(width=40)
edited_image_name.grid(row=1, column=0, padx=20, pady=30)

window.mainloop()

