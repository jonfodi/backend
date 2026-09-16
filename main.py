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

@app.get("/dietitians", response_model=list[schemas.DietitianResponse])
def get_dietitians(specialty: schemas.SpecialtyEnum = None, db: Session = Depends(get_db)):
    query = db.query(models.Dietitian)
    if specialty:
        query = query.filter(models.Dietitian.specialty == specialty)
    return query.all()
  
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
