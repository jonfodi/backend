from database import engine, SessionLocal
import models

models.Base.metadata.create_all(bind=engine)

db = SessionLocal()
models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)

dietitians = [
    models.Dietitian(name="Alice Johnson"),
    models.Dietitian(name="Bob Smith"),
    models.Dietitian(name="Carol Davis"),
]

db.add_all(dietitians)
db.commit()
db.close()

print("✓ Test data added successfully")
