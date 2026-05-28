from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.note import Note
from app.schemas.note import NoteCreate, NoteResponse
from typing import List
from fastapi import HTTPException




from app.auth.dependencies import get_current_user
from app.models.user import User


router = APIRouter()


@router.post("/notes", response_model=NoteResponse)
def create_note(
    note: NoteCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    new_note = Note(
    title=note.title,
    content=note.content,
    user_id=current_user.id
)

    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note







@router.get("/notes", response_model=List[NoteResponse])
def get_notes(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    notes = db.query(Note).filter(
        Note.user_id == current_user.id
    ).all()

    return notes




@router.put("/notes/{note_id}", response_model=NoteResponse)
def update_note(note_id: int, updated_note: NoteCreate, db: Session = Depends(get_db)):

    note = db.query(Note).filter(Note.id == note_id).first()

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    note.title = updated_note.title
    note.content = updated_note.content

    db.commit()
    db.refresh(note)

    return note




@router.delete("/notes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):

    note = db.query(Note).filter(Note.id == note_id).first()

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    db.delete(note)
    db.commit()

    return {"message": "Note deleted successfully"}