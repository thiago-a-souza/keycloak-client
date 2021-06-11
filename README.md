# keycloak-client
Sample protected Flask webapp using Keycloak


# Pre-requisites
- Docker 
- Python 3.7
- Pip

# Install

## Python dependencies

```
pip install -r requirements.txt
```
  
## Run Keycloak

```
docker run -p 8080:8080 -e KEYCLOAK_USER=admin -e KEYCLOAK_PASSWORD=admin quay.io/keycloak/keycloak:13.0.1
```

## Configure Keycloak

1. Open Keycloak at http://localhost:8080/auth/admin
2. Use the credentials *admin/admin* to log in
3. Create a new realm named *sample-realm*
4. Create a new client named *sample-client* using the *openid-connect* protocol
5. Make sure that the client has the access type set to ___public___. 
   - **public:** used by client-side clients that are accessing the application via a browser.
   - **confidential:** used by server-side clients that need to access the applicaton via a browser, and it requires a secret to turn an access code into an access token.
   - **bearer-only:** accepts only bearer tokens, so a browser login is not possible.
6. Use a star wildcard to allow redirecting to all endpoints in the *Valid Redirect URIs* field
7. Create a new user and set the username and email
8. Set the password in the credentials tab

# Running the application

1. Run the python application `python app.py`
2. Open the browser at http://localhost:5000
3. Log in using the username/password created for the user in Keycloak
