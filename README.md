# MEGA-Server
Dockerized REST server for MEGA drive management

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
  

### PUT htt<span>p://localhost:<port>/login


### PUT htt<span>p://localhost:<port>/login


### PUT htt<span>p://localhost:<port>/login
