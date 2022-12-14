from pydantic import BaseModel
from typing import Union
from . import utils

class Client(BaseModel):
  id: Union[int, None]
  staff_id: int
  name: str
  tel_number: str 

db = []  # dictionary list

def add(staff_id, name, tel_number):
  dict = {
    "id": utils.get_new_id(db),
    "staff_id": staff_id,
    "name": name,
    "tel_number": tel_number,
  }
  db.append(dict)
  return dict

def get(id: int):
  return utils.search(db, 'id', id)

def get_all():
  return db
  
def update(id, update_data):
  return utils.update(db, id, update_data)
