This will be the root directory for the API

## Run Flask
### Run flask for develop
```
$ python webapp/run.py
```
In flask, Default port is `5000`

Swagger document page:  `http://127.0.0.1:5000/swagger`

### Run flask for production

** Run with gunicorn **

In  api/

```
$ gunicorn -w 4 -b 127.0.0.1:5000 helpdeskapp

```

* -w : number of worker
* -b : Socket to bind


### Run with Docker

```
$ docker build -t helpdesk:v1 .

$ docker run -p 3030:3030 --name helpdesk helpdesk 
 
```