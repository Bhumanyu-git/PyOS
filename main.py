import tkinter
from tkinter import ttk, messagebox, simpledialog
import os

def showApps():
    functions = tkinter.Toplevel()
    functions.title("Apps")
    functions.geometry("400x400")
    functions.configure(bg="skyblue")

    root = tkinter.Frame(functions, bg="skyblue")
    root.pack(expand=True, fill="both")

    label = tkinter.Label(root, text="Available Apps", font=("Arial", 18, "bold"), fg="black", bg="skyblue")
    label.pack(pady=20)

    tkinter.Button(root, text="File Manager", command=file_manager, width=20, bg="white", fg="black",
                   font=("Arial", 12)).pack(pady=10)

    tkinter.Button(root, text="Calculator", command=calculator, width=20, bg="white", fg="black",
                   font=("Arial", 12)).pack(pady=10)

    tkinter.Button(root, text="Text Editor", command=text_editor, width=20, bg="white", fg="black",
                   font=("Arial", 12)).pack(pady=10)

    tkinter.Button(root, text="About", command=lambda: messagebox.showinfo("About", "PyOS v1.0"), width=20, bg="white",
                   fg="black", font=("Arial", 12)).pack(pady=10)

def file_manager():
    window = tkinter.Toplevel()
    window.title("File Manager")
    window.geometry("600x400")
    window.configure(bg="yellow")

    def write_file():
        filename = simpledialog.askstring("Filename", "Enter file name:")
        if filename:
            content = simpledialog.askstring("Content", "Enter content to write:")
            try:
                with open(filename, "w") as file:
                    file.write(content or "")
                messagebox.showinfo("Success", "File written successfully!")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def read_file():
        filename = simpledialog.askstring("Filename", "Enter file name to read:")
        try:
            with open(filename, "r") as file:
                messagebox.showinfo("Content", file.read())
        except FileNotFoundError:
            messagebox.showerror("Not Found", "File not found!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_file():
        filename = simpledialog.askstring("Filename", "Enter file name to delete:")
        try:
            os.remove(filename)
            messagebox.showinfo("Success", f"Deleted '{filename}'")
        except FileNotFoundError:
            messagebox.showerror("Not Found", "File not found!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(window, text="Write File", command=write_file).pack(pady=20)
    ttk.Button(window, text="Read File", command=read_file).pack(pady=20)
    ttk.Button(window, text="Delete File", command=delete_file).pack(pady=20)


def calculator():
    expr = simpledialog.askstring("Calculator", "Enter mathematical expression:")
    if expr:
        try:
            result = eval(expr)
            messagebox.showinfo("Result", f"The answer is {result}")
        except Exception as e:
            messagebox.showerror("Error", str(e))


def text_editor():
    window = tkinter.Toplevel()
    window.title("Text Editor")
    window.geometry("600x400")
    window.configure(bg="pink")

    text_area = tkinter.Text(window, wrap="word", font=("Consolas", 12), bg="white", fg="black")
    text_area.pack(expand=True, fill="both", padx=10, pady=10)

    def open_file():
        from tkinter import filedialog
        file_path = filedialog.askopenfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "r", encoding="utf-8") as f:
                text_area.delete("1.0", tkinter.END)
                text_area.insert(tkinter.END, f.read())

    def save_file():
        from tkinter import filedialog
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(text_area.get("1.0", tkinter.END))
            messagebox.showinfo("Saved", "File saved!")

    def clear_text():
        text_area.delete("1.0", tkinter.END)

    button_frame = tkinter.Frame(window, bg="pink")
    button_frame.pack(fill="x", padx=10, pady=(0, 10))

    tkinter.Button(button_frame, text="Open", command=open_file, width=10).pack(side="left", padx=5)
    tkinter.Button(button_frame, text="Save", command=save_file, width=10).pack(side="left", padx=5)
    tkinter.Button(button_frame, text="Clear", command=clear_text, width=10).pack(side="left", padx=5)

if __name__ == "__main__":
    window = tkinter.Tk()
    window.title("PyOS")
    window.geometry("800x600")

    root = tkinter.Frame(window, bg="green")
    label = ttk.Label(root, text="Welcome to PyOS", font=("Arial", 40, "bold"), foreground="white", background="green")
    button = tkinter.Button(root, text="PyOS", fg="white", bg="darkgreen", command=showApps,
                            font=("Arial", 12, "bold"))

    root.pack(fill=tkinter.BOTH, expand=True)
    label.pack(expand=True, fill="y")
    button.pack(side="bottom", fill="x")

    window.mainloop()