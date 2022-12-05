from fastapi import FastAPI, Request
import uvicorn

from entity import staff
from entity import client
from entity import campaign
from entity import advert

tags_metadata = [
  {
    "name": "clients",
    "description": "Agate의 고객",
  },
  {
    "name": "campaigns",
    "description": "광고 활동의 집합",
  },
  {
    "name": "adverts",
    "description": "개별 광고",
  },
]  # https://ie.jinwoop.repl.co/docs
app = FastAPI(openapi_tags=tags_metadata)

@app.get("/")
async def main():
  return "OK"

## client

@app.get("/clients", tags=["clients"])
async def get_all_client():
  res = client.get_all()
  return res

@app.get("/clients/{id}", tags=["clients"])
async def get_client(id: int):
  res = client.get(id)
  return res

@app.post("/clients", tags=["clients"])
async def add_client(req: client.Client, ):
  res = client.add(req.staff_id, req.name, req.tel_number)
  return res

## campaign

@app.get("/campaigns", tags=["campaigns"])
async def get_all_campaign():
  res = campaign.get_all()
  return res

@app.get("/campaigns/{id}", tags=["campaigns"])
async def get_campaign(id: int):
  res = campaign.get(id)
  return res

@app.get("/campaigns/by_client/{client_id}", tags=["campaigns"])
async def get_campaign_by_client(client_id: int):
  res = campaign.get_list_by_client(client_id)
  return res

@app.post("/campaigns", tags=["campaigns"])
async def add_campaign(req: campaign.Campaign):
  res = campaign.add(req.client_id, req.title, req.start_date, req.end_date)
  return res

## advert

@app.get("/adverts", tags=["adverts"])
async def get_all_advert():
  res = advert.get_all()
  return res

@app.get("/adverts/{id}", tags=["adverts"])
async def get_advert(id: int):
  res = advert.get(id)
  return res

@app.patch("/adverts/{id}", tags=["adverts"])
async def update_advert(id: int, req: Request):
  res = advert.update(id, await req.json())
  return res

@app.post("/adverts", tags=["adverts"])
async def add_advert(req: advert.Advert):
  res = advert.add(req.campaign_id, req.title, req.content, req.progress, req.start_date, req.end_date)
  return res

@app.get("/adverts/by_campaign/{campaign_id}", tags=["adverts"])
async def get_advert_by_campaign(campaign_id: int):
  res = advert.get_list_by_campaign(campaign_id)
  return res

## test

@app.get("/test")
async def generate_test_data():
  staff.add("진우", "010-0000", staff.staff_grade.CAMPAIGN_STAFF)
  staff.add("혁중", "010-0000", staff.staff_grade.ACCOUNTANT)
  staff.add("도영", "010-0000", staff.staff_grade.CONTACT_STAFF)
  staff.add("채민", "010-0000", staff.staff_grade.STAFF)

  client.add(staff_id=1, name="오리온", tel_number="010-0000")
  client.add(staff_id=1, name="삼성", tel_number="010-0000")
  client.add(staff_id=1, name="LG", tel_number="010-0000")
  client.add(staff_id=1, name="롯데", tel_number="010-0000")
  client.add(staff_id=3, name="코카콜라", tel_number="010-0000")
  client.add(staff_id=3, name="카시오", tel_number="010-0000")
  client.add(staff_id=3, name="Apple", tel_number="010-0000")
  client.add(staff_id=3, name="수원시청", tel_number="010-0000")

  campaign.add(client_id=1, title="고전 캠페인", start_date="2019-01-01", end_date="2019-12-31")
  campaign.add(client_id=2, title="12월 연휴 캠페인", start_date="2022-12-01", end_date="")

  advert.add(2, "TV 광고", "방송 3사 광고", "1.기획\n2.집행", "2022-01-01", "2022-05-05")
  advert.add(2, "Youtube 광고", "유튜브 인플루은서 광고", "1.컨텍 준비", "2022-04-03", "")

  return "OK"

uvicorn.run(app, host="0.0.0.0", port="8000")
