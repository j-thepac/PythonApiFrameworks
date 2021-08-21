from eve import Eve
from eve.auth import BasicAuth


class MyBasicAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        if resource == 'hello' and method == 'POST':
            return username == 'admin' and password == 'password'
        else:
            return True

# my_settings = {
#     'MONGO_HOST': 'localhost',
#     'MONGO_PORT': 27017,
#     'MONGO_DBNAME': 'the_db_name',
#     'DOMAIN': {'contacts': {}}
# }

# settings = {'DOMAIN': {'people': {}}}
app = Eve(auth=MyBasicAuth)  # Eve(settings=my_settings)


@app.route('/hello')
def hello_world():
    return 'hello world!'

if __name__ == '__main__':
    app.run()