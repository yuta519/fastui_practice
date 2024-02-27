from fastui import components as c
from fastui.events import GoToEvent

def footer() -> list[c.AnyComponent]:
    return [
        c.Footer(
            extra_text='yuta519',
            links=[
                c.Link(components=[c.Text(text='Github')], on_click=GoToEvent(url='https://github.com/pydantic/FastUI')),
                c.Link(components=[c.Text(text='PyPI')], on_click=GoToEvent(url='https://pypi.org/project/fastui/')),
                c.Link(components=[c.Text(text='NPM')], on_click=GoToEvent(url='https://www.npmjs.com/org/pydantic/')),
            ],
        ),
    ]
