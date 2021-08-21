

import falcon
import falcon.asgi

app = falcon.asgi.App()

class Test:
    async def on_get(self, req, resp):
        # resp.status = falcon.HTTP_200
        # resp.content_type = falcon.MEDIA_TEXT  # Default is JSON, so override
        resp.text = ('working')


app.add_route('/', Test())