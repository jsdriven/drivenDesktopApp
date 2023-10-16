from pymongo import MongoClient
import os
from dotenv import load_dotenv
import customtkinter
import logging
import Data.Post as Post
from bson.json_util import dumps
from Views import PostView
from tkinter import ttk
import tkinter
from tkinter import messagebox

class ListPostsView(customtkinter.CTkFrame):
    def __init__(self,parent):        
        super().__init__(parent)
        load_dotenv()
        self.Posts = []
        self.parent = parent
        self.bind('<Visibility>',lambda event:self.onLoad(event=event))
        #Below should be replace with Grid of Posts 
        # This will need to use Data.Post
        #self.text = customtkinter.CTkLabel(self, text="ListPostsView")
        #self.text.pack()
        
        #Grid Configuration for Table        
        self.rowconfigure(0,weight=1)         
        self.rowconfigure(1,weight=10) 
        self.columnconfigure(0,weight=1)          
        self.columnconfigure(1,weight=1)                 
        self.columnconfigure(2,weight=1)               
        self.columnconfigure(3,weight=1) 
         
        #Will need to add Frame here that contains Buttons for Editing and deleting selected posts
        self.EditButton = customtkinter.CTkButton(self,text="Edit",command=self.EditPost)
        self.EditButton.grid(row=0,column=0)
        self.DeleteButton = customtkinter.CTkButton(self,text="Delete",command=self.DeletePost)
        self.DeleteButton.grid(row=0,column=1)
        
        self.CopyButton = customtkinter.CTkButton(self,text="CopyID",command=self.CopyID)
        self.CopyButton.grid(row=0,column=2)
        
        self.RefreshButton = customtkinter.CTkButton(self,text="Refresh",command=self.RefreshData)
        self.RefreshButton.grid(row=0,column=3)
        
        
        #This will need to be put into a view class so that it can handle list of posts.
        self.postTable = ttk.Treeview(self)
        self.postTable["columns"] = ["Title","Tags","PostDate"]
        self.postTable.column("#0",width=0,stretch=False)
        self.postTable.heading("#0",text="",anchor="w")
        self.postTable.column("Title",anchor="center")
        self.postTable.heading("Title",text="Title",anchor="center")
        self.postTable.column("Tags",anchor="center")
        self.postTable.heading("Tags",text="Tags",anchor="center")
        self.postTable.column("PostDate",anchor="center")
        self.postTable.heading("PostDate",text="PostDate",anchor="center")
        self.postTable.grid(row=1,column=0,columnspan=4,sticky="WENS")
        
    def EditPost(self):
        selectedPost = self.postTable.focus()
        selectedPostinList = next(post for post in self.Posts if post.id == selectedPost)
        logging.info(selectedPostinList)
        self.parent.master.EditPost(selectedPostinList)
        #self.parent.event_generate("<<EditPost>>", *args)  
       
      
    def DeletePost(self):
        select = self.postTable.focus()
        logging.info("Selected item iid: " + select)
        confirm_box = messagebox.askquestion("Delete Post",'Are you sure you want to delete post ' + select, icon='warning')
        if confirm_box == 'no':
            return
        
        uri = "mongodb+srv://%s:%s@cluster0.cljhy.mongodb.net/?retryWrites=true&w=majority" % (os.getenv("DB_USER"),os.getenv("DB_PASS"))
        dbName="drivendev"
        try:
            client = MongoClient(uri)
            db = client[dbName]
            messagebox.showinfo("Delete",select)
            delResult = db.posts.delete_one({"_id":select})
            messagebox.showinfo("Delete",delResult)
            self.RefreshData()
            client.close()
        except Exception as e:
            client.close()
            logging.error(e)
        return
        
    def CopyID(self):   
        select = self.postTable.focus()
        self.clipboard_clear()
        self.clipboard_append(select)
        return
    
    def RefreshData(self):        
        for child in self.postTable.get_children():
            self.postTable.delete(child)        
        self.Posts = self.loadData()
        for post in self.Posts:
            logging.info(post.title)
            #This table need to be its own view 
            # Selected item should use iid to lookup the postId in the mast list contained in this object
            # The use that to get original post from list and pass to edit view
            self.postTable.insert("",tkinter.END,iid=post.id,values=(post.title,",".join(post.tags),post.postDate))
        return

    def onLoad(self,event):
        if(len(self.Posts) > 0):
            logging.info("Data already loaded.")
            return
        logging.info("LOADING LIST View")
        logging.info(event)
        logging.info("Loading Data")
        self.Posts = self.loadData()
        for post in self.Posts:
            logging.info(post.title)
            #This table need to be its own view 
            # Selected item should use iid to lookup the postId in the mast list contained in this object
            # The use that to get original post from list and pass to edit view
            self.postTable.insert("",tkinter.END,iid=post.id,values=(post.title,",".join(post.tags),post.postDate))

    def loadData(self):
        returnPosts = []
        try:
            uri = "mongodb+srv://%s:%s@cluster0.cljhy.mongodb.net/?retryWrites=true&w=majority" % (os.getenv("DB_USER"),os.getenv("DB_PASS"))
            dbName="drivendev"        
            client = MongoClient(uri)
            db = client[dbName]
            documents = db.posts.find()
            for doc in documents:
                returnPosts.append(Post(**doc))
            client.close()
        except Exception as e:
            messagebox.showerror("Error",e)
            client.close()
            logging.error(e)
        return returnPosts