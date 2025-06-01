import tkinter
from tkinter import ttk
from tkinter import messagebox
import math

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Integral (Trapesium)")

        frame = tkinter.Frame(self.root)
        frame.pack()

        user_info_frame = tkinter.LabelFrame(frame, text="Integral Kalkulator")
        user_info_frame.grid(row=0, column=0, padx=50, pady=40)

        
        tkinter.Label(user_info_frame, text="Fungsi f(x): ").grid(row=0, column=0)
        self.fungsi_entry = tkinter.Entry(user_info_frame, width=30)
        self.fungsi_entry.grid(row=1, column=0)

        
        tkinter.Label(user_info_frame, text="Batas Bawah: ").grid(row=0, column=1)
        self.bawah_entry = tkinter.Entry(user_info_frame)
        self.bawah_entry.grid(row=1, column=1)

        
        tkinter.Label(user_info_frame, text="Batas Atas: ").grid(row=0, column=2)
        self.atas_entry = tkinter.Entry(user_info_frame)
        self.atas_entry.grid(row=1, column=2)

        for widget in user_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=10)

        
        hitung_button = tkinter.Button(frame, text="Hitung Integral", command=self.hitung_integral)
        hitung_button.grid(row=2, column=0, pady=10)

    def f(self, x, expr):
        """Evaluasi fungsi dari input pengguna dengan variabel x"""
        try:
            return eval(expr, {"x": x, "math": math, "__builtins__": {}})
        except:
            raise ValueError("Ekspresi fungsi tidak valid.")

    def hitung_integral(self):
        try:
            fungsi_str = self.fungsi_entry.get()
            a = float(self.bawah_entry.get())
            b = float(self.atas_entry.get())

            if a >= b:
                raise ValueError("Batas bawah harus lebih kecil dari batas atas.")

            n = 1000  
            h = (b - a) / n
            total = 0.5 * (self.f(a, fungsi_str) + self.f(b, fungsi_str))

            for i in range(1, n):
                x = a + i * h
                total += self.f(x, fungsi_str)

            hasil = total * h
            messagebox.showinfo("Hasil Integral", f"Hasil integral dari {fungsi_str} dari {a} sampai {b} adalah:\n{hasil}")

        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {e}")


root = tkinter.Tk()
app = MainApp(root)
root.mainloop()

