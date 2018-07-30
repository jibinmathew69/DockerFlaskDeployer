from sanic import Sanic
from sanic import response

def make_app():
    app = Sanic(__name__)

    url = "https://34.209.178.90:8001/db"

    @app.route('/')
    async def usersignup(request):
        import requests
        r = requests.get(url)
        return response.json(r.text)

    return app

if __name__ == '__main__':
    app = make_app()

    app.run(debug=True, host='0.0.0.0', port='8001')
