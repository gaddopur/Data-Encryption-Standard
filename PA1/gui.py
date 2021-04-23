from tkinter import *
from tkinter.ttk import *
from des import init, diff_bit, preprocess_key, Weak_key_demonstration
from matplotlib.figure import Figure

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

class Combo:
    '''just for create combox from tkinter'''
    def __init__(self, root, values, col):
        self.combo = Combobox(root)
        self.combo['values'] = values
        self.combo.current(0)
        self.combo.place(x=col, y=20)
        self.combo.bind("<<ComboboxSelected>>", do_enc)
    
    def get(self):
        return self.combo.get()

def do_enc(event):
    '''this function call the function for encryption'''
    try:
        if not len(dec.get()) or not len(user_key.get()):
            enc_var.set("")
            return
        key = preprocess_key(hex_bin(user_key.get()), int(block_size.get())//2)
        enc_msg = init(dec.get(), int(block_size.get()), int(num_rounds.get()), key)
        enc_var.set(enc_msg[int(num_rounds.get())-1])
    
    except:
        enc_var.set("")

def draw_graph(diff, labels, label):
    ''' this is for draw the graph'''
    root1 = Toplevel()
    L = Label(root1, text=label)
    L.pack()
    canvas1 = Canvas(root1, height=HEIGHT, width=WIDTH)
    canvas1.pack()
    frame1 = Frame(root1)
    frame1.place(relx=0.05,rely=0.05,relwidth =0.9, relheight = 0.9,anchor = 'nw')
    
    x, y = [], []
    for z in range(len(diff)):
        y.append(diff[z])
        x.append(z)

    fig = Figure(figsize = (6, 6),dpi = 100)                
    plot1 = fig.add_subplot(111)
    plot1.set_xlabel(labels[0])
    plot1.set_ylabel(labels[1])
    plot1.plot(x,y)

    canvas = FigureCanvasTkAgg(fig, master = frame1)                       
    canvas.draw()
    canvas.get_tk_widget().place(relwidth = 1,relheight = 1,anchor = 'nw')


def Avalanche_effect_with_ciphertext():
    ''' Function name self explaionatory'''
    try:
        if not len(dec.get()) or not len(user_key.get()):
            enc_var.set("")
            return
        key = preprocess_key(hex_bin(user_key.get()), int(block_size.get())//2)
        enc_msg1 = init(dec.get(), int(block_size.get()), int(num_rounds.get()), key)
        enc_msg2 = init(diff_bit(dec.get(), 1), int(block_size.get()), int(num_rounds.get()), key)
        diff = [0]*(int(num_rounds.get())+1)
        diff[0] = 1
        
        for i in range(1, len(diff)):
            for j in range(len(enc_msg1[i-1])):
                diff[i] += (enc_msg1[i-1][j] != enc_msg2[i-1][j])
        draw_graph(diff, ["x-num rounds", "y-hamming distance betweem two cipher text"], "Avalanche effect wiht cyphertext")
    except:
        enc_var.set("")

def hex_bin(msg):
    return bin(int(msg, 16))[2:]

def Avalanche_effect_with_key():
    try:
        if not len(dec.get()) or not len(user_key.get()):
            enc_var.set("")
            return
        key = preprocess_key(hex_bin(user_key.get()), int(block_size.get())//2)
        enc_msg1 = init(dec.get(), int(block_size.get()), int(num_rounds.get()), key)
        key1 = key
        key = preprocess_key(key, int(block_size.get())//2, 1)
        print(key, key1)
        enc_msg2 = init(dec.get(), int(block_size.get()), int(num_rounds.get()), key)
        diff = [0]*(int(num_rounds.get())+1)
        diff[0] = 1
        
        for i in range(1, len(diff)):
            for j in range(len(enc_msg1[i-1])):
                diff[i] += (enc_msg1[i-1][j] != enc_msg2[i-1][j])
        draw_graph(diff, ["x-num rounds", "y-hamming distance betweem two cipher text"], "Avalanche effect with key")
    except:
        enc_var.set("")

class userEntry:
    def __init__(self, root, msg, x, f=0):
        self.var = StringVar()
        self.entry = Entry(root, textvariable=self.var)
        self.entry.insert(0, msg)
        self.entry.place(relx = x,rely = 0.4, relwidth = 0.4,relheight = 0.2,anchor = 'nw')
        if f:
            self.entry.bind("<KeyRelease>", do_enc)

    def get(self):
        return self.var.get()

def Weak_key():
    key = preprocess_key(hex_bin(user_key.get()), int(block_size.get())//2)
    keys = Weak_key_demonstration(key, int(num_rounds.get()), int(block_size.get()))

    root1 = Toplevel()
    root1.geometry(f"{WIDTH}x{HEIGHT}")
    fig = Figure(figsize = (6, 6),dpi = 100)      
    frame1 = Frame(root1)
    frame1.place(relx=0.05,rely=0.05,relwidth =0.9, relheight = 0.9,anchor = 'nw')
    var = StringVar()
    msg = Message(frame1, textvariable=var, width=500)
    msg.pack()
    print(keys)
    tmp = ""
    for i in range(len(keys)):
        tmp += "The key for round "+str(i+1)+" is:  "+keys[i]
        tmp += '\n'
    var.set(tmp)

if __name__ == "__main__":
    HEIGHT, WIDTH = 500, 800
    root = Tk()
    root.geometry("800x500")
    root.title('DES encryption and decryption')

    dec_frame = Frame(root, height=200, borderwidth=6, relief=SUNKEN)
    dec_frame.pack(fill="x")
    dec_frame.pack_propagate(0)

    block_size = Combo(dec_frame, ("Full Block size", 32, 64, 128), 100)
    num_rounds = Combo(dec_frame, ("Number of rounds", 1, 8, 16, 32), 500)

    dec = userEntry(dec_frame, "Enter plain text here", 0.55, 1)
    user_key = userEntry(dec_frame, "Enter key or weak key in hexadecimal form", 0.05)
    
    enc_frame = Frame(root, height=200, borderwidth=6, relief=SUNKEN)
    enc_frame.pack(fill="x")
    enc_frame.pack_propagate(0)

    enc_label = Label(enc_frame, text="Here Encrypted message will be shown")
    enc_label.pack(pady=20)

    enc_var = StringVar()
    enc_msg = Message(enc_frame, textvariable=enc_var, width=500)
    enc_msg.pack()

    button1 = Button(enc_frame,text = "Avalanche effect(plaintext)", command = Avalanche_effect_with_ciphertext)
    button1.place(relx = 0.1,rely = 0.7,relwidth = 0.3,relheight = 0.2,anchor = 'nw')

    button2 = Button(enc_frame,text = "Avalanche effect(key)", command = Avalanche_effect_with_key)
    button2.place(relx = 0.45,rely = 0.7,relwidth = 0.2,relheight = 0.2,anchor = 'nw')

    button3 = Button(enc_frame,text = "Weak key Demonstration", command = Weak_key)
    button3.place(relx = 0.7,rely = 0.7,relwidth = 0.2,relheight = 0.2,anchor = 'nw')

    root.mainloop()
