# MEGA-Server
Dockerized REST server for MEGA drive management

# Development
Currently this is low on my priority list and only minimal functionality is supported.

Thus, REST principles aren't really applied and all async calls to MEGA endpoints are blocked for.

# Auto-login
If you run the container with env variables `MEGA_EMAIL` and `MEGA_PASSWORD`, the app will log in to your account prior to starting the server, 
negating the need to call the login endpoint.


# Endpoints
- Flask listens on port 80. Forward whatever `port` you wish to that to communicate with it in docker.

### GET htt<span>p://localhost:`port`/login
Request Parameters: None

Response:
```json
{
  "loggedIn":  true,
  "loggingIn": false
}
```

### POST htt<span>p://localhost:<port>/login
* Logs you into your MEGA account

Form Data:
```json
  "email":    "username@provider.domain"
  "password": "secret"
```
Response:
```json
  "email":    "username@provider.domain"
  "password": "secret"
```
  

### GET htt<span>p://localhost:<port>/list_dir
#### Query Params
* path: path to mega folder.

Further documentation pending.
