from pydantic import BaseModel
from typing import Union
from . import utils

class Campaign(BaseModel):
  id: Union[int, None]
  client_id: int
  title: str
  start_date: str = utils.get_today()
  end_date: str = utils.get_day_after(7)

db = []

def add(client_id, title, start_date=None, end_date=None):
  dict = {
    "id": utils.get_new_id(db),
    "client_id": client_id,
    "title": title,
    "start_date": start_date,
    "end_date": end_date,
  }
  db.append(dict)
  return dict

def get(id: int):
  return utils.search(db, 'id', id)

def get_list_by_client(client_id: int):
  return utils.searches(db, 'client_id', client_id)

def get_all():
  return db
  
def update(id, update_data):
  return utils.update(db, id, update_data)
