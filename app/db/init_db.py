from app.db.db import engine
from app.models.memory import Base

Base.metadata.create_all(bind=engine)

print("Tabels Created")
