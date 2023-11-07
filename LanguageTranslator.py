# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 10:32:44 2023

@author: DIGITS
"""

from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# from google_trans_new import google_translator  
# translator = google_translator()  
# translate_text = translator.translate('hello world',lang_src='en',lang_tgt='zh',pronounce=True)  
# print(translate_text)

root = Tk()
root.geometry("1100x320")
root.resizable(0,0)
#root.iconbitmap['.ico']
root['bg'] = 'lightgreen'

root.title('Language Translator App')
Label(root, text="Language Translator", font="Arial 20 bold", bg="skyblue").pack()

Label(root, text="Enter Text", font="arial 13 bold", bg="White").place(x=165, y=90)

Input_text = Entry(root, width=60)
Input_text.place(x=30, y=130)
Input_text.get()

Label(root, text="Output", font="Arial 13 bold", bg="White").place(x=780, y=90)
Output_text = Text(root, font="arial 10", height=5, wrap= WORD, padx=5, pady=5, width=50)
Output_text.place(x=600, y=130)

languages = list(LANGUAGES.values())

dest_lang = ttk.Combobox(root, values=languages, width=22)
dest_lang.place(x=130, y=180)
dest_lang.set("choose language")

def Translate():
    translator = Translator()
    translated = translator.translate(text=Input_text.get(), dest=dest_lang.get())
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)
    
trans_btn = Button(root, text="Translate", font="arial 17 bold", pady=5, command= Translate, bg="skyblue", activebackground="green")
trans_btn.place(x=445, y=180)  
  
root.mainloop()
