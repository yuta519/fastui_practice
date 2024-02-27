from fastui import components as c
from fastui.events import GoToEvent

def navbar() -> list[c.AnyComponent]:
    return [
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
        )
    ]
