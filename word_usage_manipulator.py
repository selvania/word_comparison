import tkinter as tk
import pandas as pd
import numpy as np
import json

top = tk.Tk()

f = open("word_usage_data_eng.json")

data = json.load(f)

c = ['wordcount']

df = pd.DataFrame.from_dict(data, orient='index',columns=c)

print(df.head())

f.close()

worda = tk.StringVar()
wordb = tk.StringVar()

wordacount = ""
wordbcount = ""
wordapercent = "Word one:"
wordbpercent = "Word two:"

def compare_words():
    word1 = worda.get()
    word2 = wordb.get()
    if (word1 in data) and (word2 in data):
    
        word1count = int(data[word1])
        word2count = int(data[word2])
        
        totalcount = word1count + word2count
        
        wordapercent = "Word one: " + str(int((word1count/totalcount)*100))+"%"
        wordbpercent = "Word two: " + str(int((word2count/totalcount)*100))+"%"

        wordacount = str(word1count)
        wordbcount = str(word2count)
        
        lab4 = tk.Label(top, text=wordapercent)
        lab4.grid(column=1, row=6)

        lab5 = tk.Label(top, text=wordbpercent)
        lab5.grid(column=1, row=8)

        lab6 = tk.Label(top, text=wordacount,width=10)
        lab6.grid(column=2, row=7)

        lab7 = tk.Label(top, text=wordbcount,width=10)
        lab7.grid(column=2,row=9)
        return word1count,word2count,wordapercent,wordbpercent
    
    elif word1 not in data:
        lab4 = tk.Label(top, text="Word one not found.", justify="left")
        lab4.grid(column=0, row=6, columnspan=3, sticky="w")
                        
        lab5 = tk.Label(top, text="Please review data and try again.", justify="left")
        lab5.grid(column=0, row=8, columnspan=3, sticky="w")

        lab6 = tk.Label(top, text="",width=10, sticky="w")
        lab6.grid(column=2, row=7, columnspan=3, sticky="w")

        lab7 = tk.Label(top, text="",width=10)
        lab7.grid(column=2,row=9, columnspan=3, sticky="w")
    elif word2 not in data:
        lab4 = tk.Label(top, text="Word two not found.", justify="left")
        lab4.grid(column=0, row=6, columnspan=3, sticky="w")
                        
        lab5 = tk.Label(top, text="Please review data and try again.", justify="left")
        lab5.grid(column=0, row=8, columnspan=3, sticky="w")

        lab6 = tk.Label(top, text="",width=10)
        lab6.grid(column=2, row=7, columnspan=3, sticky="w")

        lab7 = tk.Label(top, text="",width=10)
        lab7.grid(column=2,row=9, columnspan=3, sticky="w")
    else:
        lab4 = tk.Label(top, text="Neither word found.", justify="left")
        lab4.grid(column=0, row=6, columnspan=3, sticky="w")
                        
        lab5 = tk.Label(top, text="Please review data and try again.", justify="left")
        lab5.grid(column=0, row=8, columnspan=3, sticky="w")

        lab6 = tk.Label(top, text="",width=10)
        lab6.grid(column=2, row=7, columnspan=3, sticky="w")

        lab7 = tk.Label(top, text="",width=10)
        lab7.grid(column=2,row=9, columnspan=3, sticky="w")

lab1 = tk.Label(top, height=5, text="Word_Comparison")
lab1.grid(column=1, row=0)

lab2 = tk.Label(top, text="Word one:")
lab2.grid(column=1,row=1)

entry1 = tk.Entry(top, textvariable = worda)
entry1.grid(column=1, row=2)

lab3 = tk.Label(top, text="Word two:")
lab3.grid(column=1,row=3)

entry2 = tk.Entry(top, textvariable = wordb)
entry2.grid(column=1, row=4)

button1 = tk.Button(top,command=compare_words,text="go",width=10,padx=2,pady=2,activebackground="dark grey")
button1.grid(column=3, row=5)

lab4 = tk.Label(top, text=wordapercent)
lab4.grid(column=1, row=6)

lab5 = tk.Label(top, text=wordbpercent)
lab5.grid(column=1, row=8)

lab6 = tk.Label(top, text=wordacount, width=10)
lab6.grid(column=2, row=7)

lab7 = tk.Label(top, text=wordbcount,width=10)
lab7.grid(column=2,row=9)

labfr1 = tk.LabelFrame(top,height=10)
labfr1.grid(row=10)

labfr2 = tk.LabelFrame(top,width=10)
labfr2.grid(column=0)

labfr3 = tk.LabelFrame(top,width=10)
labfr3.grid(column=4)

top.mainloop()
