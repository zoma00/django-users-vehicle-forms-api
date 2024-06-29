import secrets
from rest_framework.authentication import BaseAuthentication 
import os
from rest_framework.authtoken.models import Token

class ManualTokenAuthentication(BaseAuthentication):
    """
    **Warning:** This example demonstrates educational purposes only.
    Do not use this in production, as DRF TokenAuthentication is recommended.
    """

    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header or not auth_header.startswith('Bearer '):
            return None

        # Extract token from Authorization header
        provided_token = auth_header.split()[1]

        try:
            # Use DRF TokenAuthentication model to validate securely
            token = Token.objects.get(key=provided_token)
            # Access user information from token.user if needed
            return token.user, None
        except Token.DoesNotExist:
            return None  # Invalid token



def generate_manual_token(token_length=32):
  """
  Generates a random alphanumeric string of specified length.

  Args:
      token_length (int): Optional. Length of the token to generate. Defaults to 32.

  Returns:
      str: The generated random token string.
  """
  # Use secrets.token_bytes to generate cryptographically secure random bytes
  random_bytes = secrets.token_bytes(token_length // 2)
  # Convert bytes to a hex string (alphanumeric)
  token = random_bytes.hex()
  return token
