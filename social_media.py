from fastapi import FastAPI
from fastapi.params import Body
media = FastAPI()

# PATH OPERATION
@media.get("/") #decorator
def read_root(): #FUNCTION
    return ("Welcome to My Social Media API Project.")

@media.get("/posts")
def read_posts():
    return {'Data': 'This is your first post.'}

@media.post("/add_post")
def add_posts(payload : dict = Body(...)):     #payload: Variable that stores the body. Can be given any name.
# Body is created in Postman
    print(payload)
    return{"Message":"Successfully created.", "Post": payload}
    
    