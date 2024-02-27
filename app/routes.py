from __future__ import annotations as _annotations

from fastapi import APIRouter
from fastui import AnyComponent, FastUI

from app.pages.blogs import blogs
from app.pages.root import top


router = APIRouter()

@router.get('/', response_model=FastUI, response_model_exclude_none=True)
def api_index() -> list[AnyComponent]:
    return top()

@router.get('/blogs', response_model=FastUI, response_model_exclude_none=True)
def blogs_index() -> list[AnyComponent]:
    return blogs()
