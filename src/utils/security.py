import datetime
import jwt
import pytz
import os

class Security():
    secret = os.getenv('JWT_KEY')
    tz=pytz.timezone("America/Argentina/Buenos_Aires")

    @classmethod
    def generate_token(cls, authenticated_user):
        user_properties = authenticated_user[0]["properties"]
        payload = {
            'iat': datetime.datetime.now(tz=cls.tz),
            'exp': datetime.datetime.now(tz=cls.tz) + datetime.timedelta(minutes=30),
            'username': user_properties["Usuario"]["title"][0]["text"]["content"],
            'fullname': user_properties['Nombre Completo']['rich_text'][0]['text']['content']
            # 'roles': ['Administrator', 'Editor']
        }
        return jwt.encode(payload, cls.secret, algorithm="HS256")

    @classmethod
    def verify_token(cls, headers):
        if 'Authorization' in headers.keys():
            authorization = headers['Authorization']
            encoded_token = authorization.split(" ")[1]

            if (len(encoded_token) > 0):
                try:
                    payload = jwt.decode(encoded_token, cls.secret, algorithms=["HS256"])
                    # roles = list(payload['roles'])

                    # if 'Administrator' in roles:
                    #     return True
                    return True
                except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
                    return False

        return False