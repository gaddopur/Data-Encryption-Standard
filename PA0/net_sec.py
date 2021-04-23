from tkinter import *

def do_enc_dec(string):
    '''This function does the encryption and decryption
    Since this encryption algorithm is symmetric algorithm 
    do encryption and decryption can be done by same function'''
    new_string = []
    for ch in string:
        if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
            new_string.append(chr(ord('z')-ord(ch)+ord('a')))
        elif ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
            new_string.append(chr(ord('Z')-ord(ch)+ord('A')))
        else:
            new_string.append(ch)
    new_string = "".join(new_string)
    return new_string

def do_enc(event):
    enc_msg.set(do_enc_dec(str(dec_msg.get())))

def do_dec(event):
    dec_msg.set(do_enc_dec(str(enc_msg.get())))


if __name__ == "__main__":

    root = Tk()
    root.geometry("800x500")
    root.title('Encryption and Decryption')

    enc_msg, dec_msg = StringVar(), StringVar()

    ## This box for decrypted message
    f1 = Frame(root, height=200, borderwidth=6, relief=SUNKEN)
    f1.pack(fill="x", pady=12)
    f1.pack_propagate(0)

    ## This box for encrypted message
    f2 = Frame(root, height=200, borderwidth=6,relief=SUNKEN)
    f2.pack(fill="x")
    f2.pack_propagate(0)

    l = Label(f1, text="Decrypted Message", background="#000000", fg="#fff")
    l.pack(pady=12)
    l = Label(f2, text="Encrypted Message", background="#000000", fg="#fff")
    l.pack(pady=12)

    decentry = Entry(f1, textvariable=dec_msg, width=100)
    decentry.pack()
    decentry.bind("<KeyRelease>", do_enc)

    encentry = Entry(f2, textvariable=enc_msg, width=100)
    encentry.pack()
    encentry.bind("<KeyRelease>", do_dec)

    root.mainloop()