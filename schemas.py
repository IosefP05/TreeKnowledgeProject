from pydantic import BaseModel

class tree(BaseModel):
    tree_name:str
    tree_species: str
    tree_height:int