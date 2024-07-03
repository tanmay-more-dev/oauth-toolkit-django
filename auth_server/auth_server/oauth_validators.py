from oauth2_provider.oauth2_validators import OAuth2Validator


class CustomOAuth2Validator(OAuth2Validator):
    """Custom OAuth 2.0 Validator to manipulate default behaviour
    of validator"""

    # To decide what claim to return on what scope.
    oidc_claim_scope = OAuth2Validator.oidc_claim_scope
    oidc_claim_scope.update({"foo": "bar"})  # {"claim": "scope"}

    # To add additional claims(data) to the token in response.
    def get_additional_claims(self):
        print('Running Custom OAuth Validator')
        return {
            "first_name": lambda request: request.user.first_name,
            "last_name": lambda request: request.user.last_name,
            "full_name": lambda request: " ".join(
                [request.user.first_name, request.user.last_name]
            ),
            "username": lambda request: request.user.username,
            "email": lambda request: request.user.email,
        }
