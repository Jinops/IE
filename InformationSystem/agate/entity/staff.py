from pydantic import BaseModel
from typing import Union
from enum import Enum
from . import utils

class Staff_grade(Enum):
    STAFF = 1
    CONTACT_STAFF = 2
    CAMPAIGN_STAFF = 3
    CAMPAIGN_MANAGER = 4
    ACCOUNTANT = 5

class Staff(BaseModel):
    id: Union[int, None]
    name: str
    tel_number: str
    grade: Staff_grade

db = []

def add(name, tel_number, grade):
  dict = {
    "id": utils.get_new_id(db),
    "name": name,
    "tel_number": tel_number,
    "grade": grade,
  }
  db.append(dict)
  return dict
  
def get(id: int):
  return utils.search(db, 'id', id)

def get_all():
  return db

def update(id, update_data):
  return utils.update(db, id, update_data)
