from fastapi import FastAPI, HTTPException, Depends
from database import get_db
from database import engine
from sqlalchemy.orm import Session
from schemas import tree
from models import Trees
import models
from schemas import tree as TreeSchema

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/Trees")
def create_item(tree:tree, db: Session = Depends(get_db)):
    new_tree = Trees(**tree.dict())
    db.add(new_tree)
    db.commit()
    db.refresh(new_tree)
    return new_tree

@app.get("/Trees")
def read_all(db: Session=Depends(get_db)):
    all_trees = db.query(Trees).all()
    return all_trees

@app.get("/Trees/{id}")
def read_by_id(id:int, db:Session=Depends(get_db)):
    tree_by_id= db.query(Trees).filter(Trees.id == id).first()
    return tree_by_id

@app.delete("/Trees/{id}")
def delete_item(id:int, db: Session =Depends(get_db)):
    db.query(Trees).filter(Trees.id == id).delete(synchronize_session=False)
    db.commit()
    return {"Tree with ID: ", id ,"sucessfully deleted"}

@app.put("/Trees/{id}")
async def update_tree(id: int, tree: TreeSchema, db: Session = Depends(get_db)):
    existing_tree = db.query(Trees).filter(Trees.id == id).first()
    if existing_tree is None:
        raise HTTPException(status_code=404, detail="Tree not found")
    update_data = tree.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(existing_tree, key, value)
    db.commit()
    db.refresh(existing_tree)

    return existing_tree