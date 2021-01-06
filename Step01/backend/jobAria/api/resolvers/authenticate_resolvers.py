from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from api.models import Professional, Candidate
import jwt


def resolve_login_user(*_, username, password):
    try:
        user = authenticate(username=username, password=password)
        if user is not None:
            encoded_jwt = jwt.encode({'user_id': user.id}, 'JobAria', algorithm='HS256')
            return {"success": {"msg": "Connecté.", "token": encoded_jwt.decode()}}
        else:
            return {"error": "Username ou mot de passe incorrect."}
    except ValueError:
        return ValueError


def resolve_check_auth(_, info):
    try:
        request = info.context.get('request')
        token = request.headers.get('Authorization').split()[1]
        decode_jwt = jwt.decode(token, 'JobAria', algorithms='HS256')
        user_checked = User.objects.filter(id=decode_jwt.get("user_id"))
        if len(user_checked) < 1:
            return {"error": "Cet utilisateur n'éxiste pas."}
        else:
            user = User.objects.get(id=decode_jwt.get("user_id"))
            professional_checked = Professional.objects.filter(id=user.id)
            if len(professional_checked) > 0:
                professional = Professional.objects.get(id=user.id)
                return {"success": {"msg": "Access Success", "user": professional}}
            else:
                candidate = Candidate.objects.get(id=user.id)
                return {"success": {"msg": "Access Success", "user": candidate}}
    except ValueError:
        return ValueError
