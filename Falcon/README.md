# FALCON API FRAMEWORK

- ASGI stands for Asynchronous Server Gateway Interface. 
- In ASGI also you define your application as a callable which is asynchronous by default.
- As I mentioned ASGI is a successor of the successful WSGI
- You can run the ASGI version with uvicorn or any other ASGI 

## Install
```shell
$ pip install falcon uvicorn
```


## Run
```shell
uvicorn FalconApp:app
```

Then, in another terminal:
```shell
$ curl localhost:8000/
```
Or
open http://127.0.0.1:8000  in Browser or curl