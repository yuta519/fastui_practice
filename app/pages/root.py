from __future__ import annotations as _annotations

from fastui import AnyComponent
from fastui import components as c

from app.shared import demo_page

def top() -> list[AnyComponent]:
    # language=markdown
    markdown = """\
This site provides a demo of [FastUI](https://github.com/pydantic/FastUI), the code for the demo
is [here](https://github.com/pydantic/FastUI/tree/main/demo).

The following components are demonstrated:

* `Markdown` — that's me :-)
* `Text`— example [here](/components#text)
* `Paragraph` — example [here](/components#paragraph)
* `PageTitle` — you'll see the title in the browser tab change when you navigate through the site
* `Heading` — example [here](/components#heading)
* `Code` — example [here](/components#code)
* `Button` — example [here](/components#button-and-modal)
* `Link` — example [here](/components#link-list)
* `LinkList` — example [here](/components#link-list)
* `Navbar` — see the top of this page
* `Footer` — see the bottom of this page
* `Modal` — static example [here](/components#button-and-modal), dynamic content example [here](/components#dynamic-modal)
* `ServerLoad` — see [dynamic modal example](/components#dynamic-modal) and [SSE example](/components#server-load-sse)
* `Image` - example [here](/components#image)
* `Iframe` - example [here](/components#iframe)
* `Video` - example [here](/components#video)
* `Table` — See [cities table](/table/cities) and [users table](/table/users)
* `Pagination` — See the bottom of the [cities table](/table/cities)
* `ModelForm` — See [forms](/forms/login)

Authentication is supported via:
* token based authentication — see [here](/auth/login/password) for an example of password authentication
* GitHub OAuth — see [here](/auth/login/github) for an example of GitHub OAuth login
"""
    return demo_page(c.Markdown(text=markdown))
