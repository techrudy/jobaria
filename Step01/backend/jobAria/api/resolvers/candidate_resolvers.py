from api.models import Candidate
import jwt


def resolve_candidates(*_):
    try:
        candidates_array = []
        for user in Candidate.objects.all():
            candidates_array.append(user)
        return candidates_array
    except ValueError:
        return ValueError


def resolve_candidate(_, info):
    try:
        request = info.context.get('request')
        token = request.headers.get('Authorization').split()[1]
        decode_jwt = jwt.decode(token, 'JobAria', algorithms='HS256')
        user_checked = Candidate.objects.filter(id=decode_jwt.get("user_id"))
        if len(user_checked) < 1:
            return {"error": "Ce candidat n'existe pas."}
        else:
            user = Candidate.objects.get(id=decode_jwt.get("user_id"))
            return {"success": user}
    except ValueError:
        return ValueError


def resolve_create_candidate(*_, username, password, email, firstname="", lastname=""):
    try:
        user_email = Candidate.objects.filter(email=email)
        user_username = Candidate.objects.filter(username=username)
        if len(user_email) > 0:
            return {"error": "Cette email existe déja."}
        elif len(user_username) > 0:
            return {"error": "Cette username existe déja."}
        else:
            Candidate.objects.create_user(
                email=email,
                password=password,
                username=username,
                last_name=lastname,
                first_name=firstname
            )
            return {"success": "L'utilisateur %s a bien été créé" % username}
    except ValueError:
        return ValueError


def resolve_delete_candidate(*_,  user_id):
    try:
        user = Candidate.objects.get(id=user_id)
        user.delete()
        return {"success": "Le candidat %s a bien été supprimé" % user.username}
    except ValueError:
        return ValueError


def resolve_update_candidate(_, info, user_id, email=None, password=None, username=None, firstname=None, lastname=None):
    try:
        if email is None and password is None and username is None and firstname is None and lastname is None:
            return {"error": "Merci de selectionner une propriété a modifier."}
        else:
            request = info.context.get('request')
            token = request.headers.get('Authorization').split()[1]
            decode_jwt = jwt.decode(token, 'JobAria', algorithms='HS256')
            candidate_token = Candidate.objects.get(id=decode_jwt.get("user_id"))
            candidate = Candidate.objects.get(id=user_id)
            if candidate_token.id != candidate.id:
                return {"error": "Acces refusé"}
            else:
                candidate.email = email or candidate.email
                candidate.password = password or candidate.password
                candidate.username = username or candidate.username
                candidate.first_name = firstname or candidate.first_name
                candidate.last_name = lastname or candidate.last_name
                candidate.save()
            return {"success": "L'utilisateur a bien été modifié."}
    except ValueError:
        return ValueError
