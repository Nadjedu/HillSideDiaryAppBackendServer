### Authentication
Django uses sessions out-of-the-box but I decided to use jwt (token based authentication).
</br> JWT is a stateless authentication method and there are so many implementations out there.
</br> This server uses the rest_framework_simplejwt library.

### User Account Creation Flow
- Client sends a post request to `/accounts/users/` with required data.
- Server responds with user data and a key-value pair in headers containing token data.

#### NB:
- Access token expires in <b>1 hour.</b>
- Refresh token expires in <b>24 hours.</b>

#### What does this mean?
- Users will have to log in after 24 hours.
- Clients need to refresh access tokens every hour.

### Documentation Guides:
- [Django Rest Authentication](https://www.django-rest-framework.org/api-guide/authentication/)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [Web Authentication Methods](https://testdriven.io/blog/web-authentication-methods/)
