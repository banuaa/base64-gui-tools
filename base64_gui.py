import tkinter as tk
from tkinter import *
from base64 import b64encode
from base64 import b64decode
from tkinter import messagebox

class Base(object):
	def __init__(self, master):

		frame = Frame(master)
		frame.pack()

		self.storText = StringVar()
		self.storEnc = StringVar()
		self.storDec = StringVar()

		self.fontstyle = "Helvetica 11 bold"

		self.title = Label(root, text="Base64 EnDecode Tools", font="Helvetica 18 bold underline")
		self.title.pack(fill=tk.X, pady=10)

		self.plainText = Label(root, text="Plaintext", font=self.fontstyle, relief=RAISED)
		self.plainText.place(x=25, y=70, width=100)
		self.entryPT = Entry(root, text="", width=50, textvariable=self.storText)
		self.entryPT.place(x=130, y=71)

		self.encText = Label(root, text="Encrypted", font=self.fontstyle, relief=RAISED)
		self.encText.place(x=25, y=103, width=100)
		self.entryEnc = Entry(root, text="", width=50, textvariable=self.storEnc)
		self.entryEnc.place(x=130, y=104)

		self.decText = Label(root, text="Decrypted", font=self.fontstyle, relief=RAISED)
		self.decText.place(x=25, y=135, width=100)
		self.entryDec = Entry(root, text="", width=50, textvariable=self.storDec)
		self.entryDec.place(x=130, y=136)

		self.encButton = Button(root, text="Encode!", command=self.base64Encode, width=20, font=self.fontstyle)
		self.encButton.place(x=25, y=230)
		self.decButton = Button(root, text="Decode!", command=self.base64Decode, width=20, font=self.fontstyle)
		self.decButton.place(x=250, y=230)
		self.reset = Button(root, text="Reset!", command=self.reset, width=20, font=self.fontstyle)
		self.reset.place(x=140, y=185)

	def base64Encode(self):
		valPlaintext = self.entryPT.get().encode()
		encrypt = b64encode(valPlaintext).decode()
		self.storEnc.set(encrypt)

	def base64Decode(self):
		valEnc = self.entryEnc.get()
		try:
			decrypt = b64decode(valEnc).decode()
			self.storDec.set(decrypt)
		except:
			messagebox.showerror("Error", "Invalid Base64 Format!")

	def reset(self):
		self.storText.set("")
		self.storEnc.set("")
		self.storDec.set("")


if __name__ == "__main__":
	root = tk.Tk()
	root.configure(bg="#856ff8")
	root.resizable(width=False, height=False)
	root.title('Base64 EnDecode')
	Base(root)
	root.geometry("465x290")
	root.mainloop()