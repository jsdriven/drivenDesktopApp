import customtkinter
import logging
from tkinter import messagebox
import Data.Post as Post
import Data.PostUpdate as PostUpdate
import tkinter
from datetime import datetime
from pymongo import MongoClient
import os
from dotenv import load_dotenv

class CreatePostView(customtkinter.CTkFrame):
    def __init__(self,parent):        
        super().__init__(parent)
        load_dotenv()
        #self.text = customtkinter.CTkLabel(self, text="CreatePostView")
        #self.text.pack()
        self.Post = None
        self.Mode = "Create"
        #self.bind('<Visibility>',lambda event:self.onLoad(event=event))
        
        #Grid Configuration 
        self.rowconfigure([0,1,2,4,5],weight=1)
        self.rowconfigure(3,weight=10)
        self.columnconfigure([0,1,2,3,4],weight=1)
        
        #Title input
        self.titleLabel = customtkinter.CTkLabel(self, text="PostTitle")
        self.titleEntry = customtkinter.CTkEntry(self, placeholder_text="Title")
        self.titleLabel.grid(row=0,column=0,sticky="WENS")
        self.titleEntry.grid(row=0,column=1,sticky="WENS")
        
        #Tags input
        self.TagsLabel = customtkinter.CTkLabel(self, text="Tags")
        self.TagsEntry = customtkinter.CTkEntry(self)
        self.TagsLabel.grid(row=1,column=0,sticky="WENS")
        self.TagsEntry.grid(row=1,column=1,sticky="WENS")
        
        #Description input 
        self.DescriptionLabel = customtkinter.CTkLabel(self, text="Description")
        self.DescriptionEntry = customtkinter.CTkTextbox(self)
        self.DescriptionLabel.grid(row=2,column=0,sticky="WENS")
        self.DescriptionEntry.grid(row=2,column=1,padx=5,pady=5,sticky="WENS")
        
        #Content Input
        self.ContentLabel = customtkinter.CTkLabel(self, text="Content")
        self.ContentEntry = customtkinter.CTkTextbox(self)
        self.ContentLabel.grid(row=3,column=0,sticky="WENS")
        self.ContentEntry.grid(row=3,column=1,columnspan=2,padx=5,pady=5,sticky="WENS")
        
        #TODO
        # Create/Edit Button
        self.EditButton = customtkinter.CTkButton(self,text="Edit",command=self.EditPost)
        self.CreateButton = customtkinter.CTkButton(self,text="Create",command=self.CreatePost)
        
        #ReccomendLink Input
        self.RecommendLabel = customtkinter.CTkLabel(self, text="RecommendLink")
        self.RecomendEntry = customtkinter.CTkEntry(self)
        self.RecommendLabel.grid(row=4,column=0,sticky="WENS")
        self.RecomendEntry.grid(row=4,column=1,columnspan=1,padx=5,pady=5,sticky="WENS")
        
        #TODO
        # Back Button
        #This function should just generate an event that send the signal 
        #Back to main frame - that will now need to cache the last page.
        #This should be used everywhere
        
        self.BackButton = customtkinter.CTkButton(self,text="Back")
        self.BackButton.grid(row=5,column=0)
        
    def CreatePost(self):
        postDate = datetime.now()
        postId = self.titleEntry.get().replace(" ","-")+"-"+postDate.strftime("%m-%d-%Y")
        description = self.DescriptionEntry.get(1.0,'end-1c')
        content = self.ContentEntry.get(1.0,'end-1c')
        tags = self.TagsEntry.get().split(",")
        output = """ PostTitle: %s
        Tags: %s
        Description: %s
        PostDate: %s
        ID: %s
        """ %(self.titleEntry.get(), tags, description, postDate,postId)
        newPost = Post(id=postId,title=self.titleEntry.get(),tags=tags,content=content,description=description,postDate=postDate,comments=[],likes=[])
        messagebox.showinfo('PostInfo',newPost)
        self.CreatePostInDB(post=newPost)
        #Above needs to create post object then use pymongo to create
    
    def CreatePostInDB(self, post):
        uri = "mongodb+srv://%s:%s@cluster0.cljhy.mongodb.net/?retryWrites=true&w=majority" % (os.getenv("DB_USER"),os.getenv("DB_PASS"))
        dbName="drivendev"
        returnPosts = []
        try:
            client = MongoClient(uri)
            db = client[dbName]
            newPost = db.posts.insert_one(post.dict(by_alias=True))
            messagebox.showinfo("Post Create", newPost)
            client.close()
        except Exception as e:
            client.close()
            messagebox.showerror('Post Error',e)
            logging.error(e)
        return
        
        
    def EditPost(self):
        #This will need to do the same as the Create Post but will 
        #Need to use the Update Object (TODO IMplement) 
        #And check if there is a difference from the current object.
        
        #Need to get the Id from the Post Object
        # also need to compare what is entered vs the original object
        
        description = self.DescriptionEntry.get(1.0,'end-1c')
        content = self.ContentEntry.get(1.0,'end-1c')
        tags = self.TagsEntry.get().split(",")
        title=self.titleEntry.get()
        recommendLink = self.RecomendEntry.get()
        editDict = {}
        if(self.Post.title != title):
            editDict["title"]= title
        if(self.Post.recommendLink != recommendLink):
            editDict["recommendLink"]= recommendLink
        if(self.Post.content != content):
            editDict["content"]= content
        if(self.Post.description != description):
            editDict["description"] = description
            #One of these is returning a new line and it needs to be parsed
            logging.info(self.Post.description)
            logging.info(description)
        if(self.Post.tags != tags):
            editDict["tags"]= tags
        if(len(editDict) == 0):
            messagebox.showinfo("EditTest", "No Changes")
        else:
            #This piece should now Update the post
            logging.info(editDict)
            update = PostUpdate(**editDict)
            self.EditPostInDB(update=update.dict(exclude_none=True), postId=self.Post.id)  
                     
        return
    
    def EditPostInDB(self, update, postId):
        uri = "mongodb+srv://%s:%s@cluster0.cljhy.mongodb.net/?retryWrites=true&w=majority" % (os.getenv("DB_USER"),os.getenv("DB_PASS"))
        dbName="drivendev"
        try:
            client = MongoClient(uri)
            db = client[dbName]
            db.posts.update_one({"_id":postId}, {"$set":update})
            client.close()            
            messagebox.showinfo("Edit",f'Post with id {postId} updated with {update}')   
        except Exception as e:
            client.close()
            messagebox.showerror('Post Error',e)
            logging.error(e)
        return
        
    def setPost(self, post):
        self.Post = post
        self.titleEntry.delete(0,tkinter.END)
        self.TagsEntry.delete(0,tkinter.END)
        self.DescriptionEntry.delete('1.0',tkinter.END)
        self.ContentEntry.delete('1.0',tkinter.END)
        self.RecomendEntry.delete(0,tkinter.END)    
        if(post != None):
            self.titleEntry.insert(0,self.Post.title)
            self.TagsEntry.insert(0,self.Post.TagsToString())
            self.DescriptionEntry.insert('1.0',self.Post.description)
            self.ContentEntry.insert('1.0',self.Post.content)            
            if(self.Post.recommendLink != None):
                logging.info("No Reccomended Link - Will not set ")
                self.RecomendEntry.insert(0,self.Post.recommendLink)
            self.Mode = "Edit"
            self.CreateButton.grid_remove()                
            self.EditButton.grid(row=5,column=1)
        else:            
            self.Mode = "Create"
            self.EditButton.grid_remove()
            self.CreateButton.grid(row=5,column=1)  


