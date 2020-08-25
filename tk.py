from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


if __name__ == "__main__":
    root = Tk()
    root.title('请选择图片')
    frame = Frame(root, bd=2, relief=SUNKEN)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    canvas = Canvas(frame, bd=0)
    canvas.grid(row=0, column=0, sticky=N+S+E+W)
    frame.pack(fill=BOTH, expand=1)

    def printcoords():
        import shutil, os
        File = filedialog.askopenfilename(parent=root, initialdir=os.getcwd(), title='选择图片.')
        img = Image.open(File)
        out = img.resize((336, 192), Image.ANTIALIAS)  # resize image with high-quality
        filename = ImageTk.PhotoImage(out)
        canvas.image = filename
        canvas.create_image(0, 0, anchor='nw', image=filename)
        # print(File)

        dir = os.getcwd() + r'\test'
        shutil.rmtree(dir, True)
        os.makedirs(os.path.join(os.getcwd(), 'test'))

        shutil.copyfile(File, dir + r'\image')
        from test import test
        result = test()
        print(result)
        root.title(result)
    Button(root, text='选择', command=printcoords).pack()
    root.mainloop()