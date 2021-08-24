from eve import Eve
from eve.auth import BasicAuth




setting = {'DOMAIN': {'people': {}}}
app = Eve(settings=setting)  # Eve(settings=my_settings)


@app.route('/hello')
def hello_world():
    return 'hello world!'

if __name__ == '__main__':
    app.run()