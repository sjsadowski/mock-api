import falcon
from falcon import HTTPStatus

class DefaultResource:
    def on_get(self, req, resp):
        payload = {'status': '200 OK'}

        resp.media = payload


# These should be cleaned up for actual deployments; would be unsafe for
# production use
class HandleCORS(object):
    def process_request(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Methods', '*')
        resp.set_header('Access-Control-Allow-Headers', '*')
        resp.set_header('Access-Control-Max-Age', 1728000)  # 20 days
        if req.method == 'OPTIONS':
            raise HTTPStatus(falcon.HTTP_200, body='\n')

api = falcon.API(middleware=[HandleCORS()])
api.add_route('/', DefaultResource())