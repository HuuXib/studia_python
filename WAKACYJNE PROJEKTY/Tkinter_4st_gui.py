import tkinter as tk 

#program to bedzie proste menu kalkulatora

okno = tk.Tk()
okno.title("Kalkulator")
okno.geometry("500x300")

label = tk.Label(okno, text="Kalkulator", font = ("Comic Sans", 16))
# label.pack(row=0, column = 0, columnspan=3, pady= 10)
label.grid(row = 0, column = 0, columnspan=3,pady=10)


buttons = [
    ("1",1,0), ("2",1,1),("3",1,2),
    ("4", 2,0), ("5",2,1),("6",2,2),
    ("7",3,0),("8",3,1),("9",3,2),("0",4,0)
]

for (text, r , c) in buttons:
    btn = tk.Button(okno, text=text, width=5, height=2)
    btn.grid(row=r,column=c,padx=5,pady=5)

okno.mainloop()