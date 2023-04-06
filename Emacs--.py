import os
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import *
from tkinter.filedialog import *

is_emacs_heretic = False


def main():
    def new_file():
        window.title('untitled')
        text_area.delete(1.0, END)

    def open_file():
        file = askopenfilename(defaultextension='.txt', filetypes=[('All Files', "*.*"), ('Text Documents', "*.txt")])
        try:
            window.title(os.path.basename(file))
            text_area.delete(1.0, END)
            file = open(file, "r")
            text_area.insert(1.0, file.read())
        except Exception:
            print("Couldn't read file")
        finally:
            file.close()

    def save_file():
        file = filedialog.asksaveasfilename(initialfile='untitled.txt',
                                            defaultextension='.txt',
                                            filetypes=[('All Files', "*.*"), ('Text Documents', "*.txt")])
        if file is None:
            return
        else:
            try:
                window.title(os.path.basename(file))
                file = open(file, "w")
                file.write(text_area.get(1.0, END))
            except Exception:
                print("Couldn't save file")
            finally:
                file.close()

    def manual():
        showinfo('Are you DUMB?', "C'mon...... You don't need a manual for this......")

    def quit_editor():
        window.destroy()
        exit(0)

    def emacs(event):
        global is_emacs_heretic
        if is_emacs_heretic:
            showerror('', "I can't believe you use Emacs......")
            showerror('', 'What a shame! WHAT A SHAME!')
            showerror('', 'It leads to PERMANENT pinky damage.')
            showerror('', "GET OUT OF HERE! I DON'T WANT TO SEE YOU ANYMORE!")
            quit_editor()
        else:
            showwarning('', '<C-x>? You seem like a Emacs hErETiC......')
            showwarning('', 'Stop it, get some help.')
            is_emacs_heretic = True

    window = Tk()
    window.iconbitmap('Emacs--.ico')
    window.title('Emacs--')
    window_width = 500
    window_height = 500
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))
    text_area = Text(window, font=('Consolas', '16'))
    text_area.config(fg="#00FF00", bg="#000000")
    scroll_bar = Scrollbar(text_area)
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)
    text_area.grid(sticky=N + E + S + W)
    scroll_bar.pack(side=RIGHT, fill=Y)
    text_area.config(yscrollcommand=scroll_bar.set)
    menu_bar = Menu(window)
    window.config(menu=menu_bar)
    file_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='File', menu=file_menu)
    file_menu.add_command(label='New', command=new_file)
    file_menu.add_command(label='Open', command=open_file)
    file_menu.add_command(label='Save', command=save_file)
    file_menu.add_separator()
    file_menu.add_command(label='Exit', command=quit_editor)
    help_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='Help', menu=help_menu)
    help_menu.add_command(label='Manual', command=manual)

    # Emacs--
    window.bind("<Control-x>", emacs)

    window.mainloop()


if __name__ == '__main__':
    main()
