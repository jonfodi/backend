from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, get_db
import models
import schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/users/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.User).filter(models.User.id == user_id).first()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
