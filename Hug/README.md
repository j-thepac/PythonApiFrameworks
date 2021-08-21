# HUG

## Installation

```shell
pip install hug
pip install uwsgi
#or
pip install gunicorn
```
## Run
- Start Server

		Using uwsgi:`uwsgi --http 0.0.0.0:8000 --wsgi-file HugApp.py --callable __hug_wsgi__`
		Using gunicorn:`gunicorn HugApp:__hug_wsgi__`
- open link http://0.0.0.0:8000/happy_birthday?name=Timothy&age=26

## cli
`python HugApp.py Timothhy 27`

## Document
http://0.0.0.0:8000/