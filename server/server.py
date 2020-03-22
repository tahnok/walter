import asyncio
import time

from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from starlette.responses import FileResponse

import weather

templates = Jinja2Templates(directory="templates")


async def homepage(request):
    return templates.TemplateResponse(
        "index.html.jinja",
        {"request": request, "weather": weather.fetch(), "generated_at": time.strftime("%H:%M", time.localtime()),},
    )

async def snapshot(request):
    cmd = "firefox --headless --screenshot static/out.png --window-size 600,800 http://127.0.0.1:8000"
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    await proc.communicate()
    return FileResponse("static/out.png")



routes = [
    Route("/", endpoint=homepage),
    Route("/snapshot", endpoint=snapshot),
    Mount("/static", StaticFiles(directory="static"), name="static"),
]

app = Starlette(debug=True, routes=routes)
