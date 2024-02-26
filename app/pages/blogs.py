from __future__ import annotations as _annotations

from fastui import AnyComponent
from fastui import components as c
from fastui.events import GoToEvent

def template(func) -> list[AnyComponent]:
    func  = func()
    title = next(func)
    page = next(func)

    header = [
        c.PageTitle(text=f'My blog — {title}' if title else 'FastUI Demo'),
        c.Navbar(
            title='yuta519',
            title_event=GoToEvent(url='/'),
            start_links=[
                c.Link(
                    components=[c.Text(text='Components')],
                    on_click=GoToEvent(url='/components'),
                    active='startswith:/components',
                ),
                c.Link(
                    components=[c.Text(text='Tables')],
                    on_click=GoToEvent(url='/table/cities'),
                    active='startswith:/table',
                ),
                c.Link(
                    components=[c.Text(text='Auth')],
                    on_click=GoToEvent(url='/auth/login/password'),
                    active='startswith:/auth',
                ),
                c.Link(
                    components=[c.Text(text='Forms')],
                    on_click=GoToEvent(url='/forms/login'),
                    active='startswith:/forms',
                ),
            ],
        ),
    ]
    footer = [
        c.Footer(
            extra_text='yuta519',
            links=[
                c.Link(
                    components=[c.Text(text='Github')], on_click=GoToEvent(url='https://github.com/pydantic/FastUI')
                ),
                c.Link(components=[c.Text(text='PyPI')], on_click=GoToEvent(url='https://pypi.org/project/fastui/')),
                c.Link(components=[c.Text(text='NPM')], on_click=GoToEvent(url='https://www.npmjs.com/org/pydantic/')),
            ],
        ),
    ]
    return header + [page] + footer

@template
def blogs(*components: AnyComponent, title: str | None = None) -> list[AnyComponent]: # type: ignore
    title = 'blog'
    yield title
    yield c.PageTitle(text=f'My blog — {title}' if title else 'FastUI Demo')
