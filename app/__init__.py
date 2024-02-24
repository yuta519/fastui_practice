from __future__ import annotations as _annotations

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastui import prebuilt_html

from .root import router as root_router


app = FastAPI()
app.include_router(root_router, prefix='/api')

@app.get('/{path:path}')
async def html_landing() -> HTMLResponse:
    return HTMLResponse(prebuilt_html(title='FastUI Demo'))
