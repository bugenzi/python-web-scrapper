import index
import tkinter

root = tkinter.Tk()
canvas1 = tkinter.Canvas(root, width=400, height=300)
heading = tkinter.Text(root, width=400, height=20)
canvas1.pack()

entry1 = tkinter.Entry(root)
entry2 = tkinter.Entry(root)

entry1.insert(0, "URL")
entry2.insert(1, "Direction")

entry1.bind("<Button-1>", )

canvas1.create_window(200, 140, window=entry1)
canvas1.create_window(200, 30, window=entry2)


def get_input_data():
    # direction = entry1.get()
    x = index.getUrl(entry1.get())

    if index.getUrl(entry1.get()):
        label1 = tkinter.Label(root, text="Radi uspjesno ste poslali")
        canvas1.create_window(200, 70, window=label1)
        index.scrapping_data(entry2.get(), x)
    else:
        label2 = tkinter.Label(root, text="Pogresno ste unijeli parametre")
        canvas1.create_window(200, 70, window=label2)


button = tkinter.Button(text="Skrejpaj stranicu", command=get_input_data)
canvas1.create_window(200, 250, window=button)

root.mainloop()
