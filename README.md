# DjangoBoxes
Django project to model "box" resource.

# APIs

### Login
Method: `POST`
URL: `http://localhost:8000/login/`

Form-Data:
```json
{
    "username": "your_username",
    "password": "your_password"
}
```

Response:

```json
Cookies are set to form the session.
csrftoken
sessionid
```

###### NOTE: For all further API calls, requests must have the CSRF token and session id in the headers.

```
headers = {
    "sessionid": "your_session_id",
    "X-CSRFToken": "your_csrf_token",
    "Content-Type": "application/json"   
} 
```


### Create Box
Method: `POST`
URL: `http://localhost:8000/create_box/`

Payload:
```json
{
	"breadth": 1, 
	"height": 2,
	"length": 333
}
```


### Update Box
Method: `PUT`
URL: `http://localhost:8000/update_box/`

Payload:
```json
{
	"breadth": 1, 
	"height": 2,
	"length": 333
}
```

### List Boxes
Method: `GET`
URL: `http://localhost:8000/boxes/`

Query Parameters:
1. min_length
2. max_length
3. min_breadth
4. max_breadth
5. min_height
6. max_height
7. min_area
8. max_area 
9. min_volume
10. max_volume
11. created_by
12. min_created_at
13. max_created_at

Payload:
```json
[
	{
		"length": 333,
		"breadth": 1,
		"height": 2,
		"id": 1,
		"created_by_id": 1,
		"updated_at": "2019-04-11T07:43:04.141468+00:00"
	},
	{
		"length": 333,
		"breadth": 1,
		"height": 2,
		"id": 2,
		"created_by_id": 2,
		"updated_at": "2019-04-11T07:44:46.841679+00:00"
	}
]
```
