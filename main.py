from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from pydantic import BaseModel

from database import SessionLocal, engine
from models import Base, UserData
from transliterate import en_to_kn_open_source, en_to_kn_aws

Base.metadata.create_all(bind=engine)
app = FastAPI()
templates = Jinja2Templates(directory="templates")

class TransliterateRequest(BaseModel):
    text: str
    method: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
def form_page(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/submit")
def submit_form(
    name: str = Form(...),
    address: str = Form(...),
    name_kn: str = Form(...),
    address_kn: str = Form(...),
    db: Session = Depends(get_db)
):
    new_entry = UserData(
        name_en=name,
        name_kn=name_kn,
        address_en=address,
        address_kn=address_kn
    )
    db.add(new_entry)
    db.commit()
    return RedirectResponse("/", status_code=303)

@app.post("/transliterate")
async def transliterate_text(req: TransliterateRequest):
    text = req.text
    method = req.method
    if method == "open_source":
        translated = en_to_kn_open_source(text)
    else:
        translated = en_to_kn_aws(text)
    return JSONResponse(content={"translated": translated})
