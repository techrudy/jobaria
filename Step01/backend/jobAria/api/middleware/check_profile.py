from django.contrib.auth.models import User
from api.models import Professional, Candidate
import jwt


def middleware_auth_professional(resolver):
    def middleware_check_auth_professional(_, info, **kwargs):
        try:
            request = info.context.get('request')
            token = request.headers.get('Authorization').split()[1]
            decode_jwt = jwt.decode(token, 'JobAria', algorithms='HS256')
            user_checked = Professional.objects.filter(id=decode_jwt.get("user_id"))
            if len(user_checked) < 1:
                return {"error": "Ce Professionnel n'éxiste pas."}
            else:
                return resolver(_, info, **kwargs)
        except:
            return {"error": "Accès refusé."}
    return middleware_check_auth_professional


def middleware_auth_candidate(resolver):
    def middleware_check_auth_candidate(_, info, **kwargs):
        try:
            request = info.context.get('request')
            token = request.headers.get('Authorization').split()[1]
            decode_jwt = jwt.decode(token, 'JobAria', algorithms='HS256')
            user_checked = Candidate.objects.filter(id=decode_jwt.get("user_id"))
            if len(user_checked) < 1:
                return {"error": "Ce Candidat n'éxiste pas."}
            else:
                return resolver(_, info, **kwargs)
        except:
            return {"error": "Accès refusé."}
    return middleware_check_auth_candidate


def middleware_auth_user(resolver):
    def middleware_check_auth_user(_, info, **kwargs):
        try:
            request = info.context.get('request')
            token = request.headers.get('Authorization').split()[1]
            decode_jwt = jwt.decode(token, 'JobAria', algorithms='HS256')
            user_checked = User.objects.filter(id=decode_jwt.get("user_id"))
            if len(user_checked) < 1:
                return {"error": "Cette utilisateur n'éxiste pas."}
            else:
                return resolver(_, info, **kwargs)
        except:
            return {"error": "Accès refusé."}
    return middleware_check_auth_user
