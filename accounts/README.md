### Authentication
Django uses sessions out-of-the-box but I decided to use jwt (token based authentication).
</br> JWT is a stateless authentication method and there are so many implementations out there.
</br> This server uses the rest_framework_simplejwt library.

### User Account Creation Flow
- Client sends a post request to `/accounts/users/` with required data.
- Server responds with user data and tokens in response headers.

### User login Flow
- Client sends a post request to `/accounts/token` with required data.
- Server responds with access token and refresh token in response body.

### Token Refresh
- Client sends a post request to `/accounts/refresh` with required data.
- Server responds with new access token in response body.

#### NB:
- Access token expires in <b>1 hour.</b>
- Refresh token expires in <b>24 hours.</b>
- There's no logout endpoint. Deleting tokens client side should be enough
- Getting a new token does not invalidate old tokens.
- User profile can be retrieved using the `/accounts/users/me` endpoint.

#### What does this mean?
- Users will have to log in after 24 hours.
- Clients need to refresh access tokens every hour.

### Documentation Guides:
- [Django Rest Authentication](https://www.django-rest-framework.org/api-guide/authentication/)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [Web Authentication Methods](https://testdriven.io/blog/web-authentication-methods/)
