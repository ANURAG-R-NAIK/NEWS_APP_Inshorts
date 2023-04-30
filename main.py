import requests 
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk,Image
import io
import webbrowser

class Newsapp:
    
    def __init__(self): #constructor
        # starting window work
        # fetch data
        #initial GUI load
        #load first news item 
        
        
        # We will get the updated news from the api newsapi 
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=89b36f5f950246cdbc039cb3db122650').json()
        # print(data)
        
        
        self.load_gui() #tkinter window is used for loading the gui
        
        
        self.load_news_item(0) #gives first news  
        
        
        
    def load_gui(self):
        self.root = Tk()
        self.root.geometry('350x600')
        self.root.resizable(0, 0) # to prevent resizing the window 
        self.root.title('Apna News App')
        self.root.configure(background = 'black') 
      
     
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
             
              
    def load_news_item(self, index):
        #first we need to clear the screen before loading the next news item
        
        self.clear()
        
        # images code down here
        try:
            img_url = self.data['articles'][index]['urlToImage'] #this takes the url of the image
            raw_data = urlopen(img_url).read() #reads the url
            im = Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo = ImageTk.PhotoImage(im) #opens the photo and display in our window
            
        except: # if the news or image fails to get the url and load the news
            img_url = 'https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg'
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)
            
        
        label = Label(self.root,image=photo)
        label.pack()
        
        #FOR THE HEADING OF THE NEWS 
        heading = Label(self.root, text = self.data['articles'][index]['title'], bg = 'black', fg = 'white', wraplength = 350, justify = 'center')
        # wrpalength to avoid text to get cut, and justify to make all textncenter justified
        heading.pack(pady = (10,20))
        heading.config(font = ('verdana', 15))
        
        #FOR THE DESCRIPTION OF THE NEWS
        details = Label(self.root, text = self.data['articles'][index]['description'], bg = 'black', fg = 'white', wraplength = 350, justify = 'center')
        # wrpalength to avoid text to get cut, and justify to make all textncenter justified
        details.pack(pady = (2,20))
        details.config(font = ('verdana', 12))
        
        #frames are given for the buttons
        frame = Frame(self.root, bg = 'black')
        frame.pack(expand = True, fill = BOTH)
        
        if index != 0: #if it is the first nes then no previous button is showed 
            prev = Button(frame, text = 'PREV', width = 16, height = 3,command = lambda :self.load_news_item(index - 1))
            # the command is calling back the function by decrementing the index by one
            prev.pack(side = LEFT)
        
        read = Button(frame, text = 'READ MORE', width = 16, height = 3, command = lambda :self.open_link(self.data['articles'][index]['url']))
        #command line takes url for the news and directs it to the complete news page 
        read.pack(side = LEFT)
        
        if index != len(self.data['articles'])-1: # only if not the last news the next button is showed
            next = Button(frame, text = 'NEXT', width = 16, height = 3, command = lambda :self.load_news_item(index + 1))
            # the command is calling back the function by incrementing the index by one
            next.pack(side = LEFT)
        
        self.root.mainloop()
        
    def open_link(self, url):
        webbrowser.open(url)

obj = Newsapp()