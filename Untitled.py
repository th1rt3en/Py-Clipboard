
# coding: utf-8

# In[1]:


import pyperclip as pc
from keyboard import *
from Tkinter import *
from ttk import *
from time import ctime, sleep
import re


# In[2]:


s = []


# In[3]:


def func():
    sleep(0.1)
    global s
    s += [[ctime(), pc.paste()]]


# In[4]:


def clean(string):
    return ''.join(map(lambda x: x.strip(), string.split('\n')))


# In[5]:


def hour(time):
    return re.findall(r'\d{1,2}:\d{1,2}:\d{1,2}', time)[0]


# In[6]:


def clear():
    s[:] = []


# In[ ]:


def exit():
    unhook_all_hotkeys()


# In[7]:


def run():
    sleep(0.1)
    root = Tk()
    note = Notebook(root)
    for i in range(~-len(s)/10 + 1):
        tab = Frame(note)
        for j in range(min(len(s)-i*10, 10)):
            Label(tab, text = '%s : %.30s' % (hour(s[::-1][i*10+j][0]), clean(s[::-1][i*10+j][1]))).grid(row=j, column=0)
            Button(tab, text = 'Copy', command = lambda: pc.copy(s[::-1][i*10+j][1])).grid(row=j, column=1)
        note.add(tab, text = 'Page ' + str(i+1))
    note.pack()
    Button(root, text = 'Clear', command = clear).pack(side=BOTTOM)
    root.wm_attributes("-topmost", 1)
    root.after(200, lambda: root.focus_force())
    root.title('PyClipboard')
    root.mainloop()


# In[8]:


add_hotkey('ctrl+c', func)
add_hotkey('ctrl+b', run)
add_hotkey('ctrl+alt+c', exit)

