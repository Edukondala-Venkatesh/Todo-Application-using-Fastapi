from fastapi import FastAPI
from todo import  models
from todo.database import engine
from todo.Routers import todoRouters, userRouters, authentication, FilterRouter

app=FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(todoRouters.router)
app.include_router(userRouters.router)
app.include_router(FilterRouter.router)


# -----------------------------------------------------------------------------------------------------------------------------------------------



