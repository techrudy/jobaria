from api.models import Professional, Companies


def resolve_professionals(*_):
    professional_array = []
    for user in Professional.objects.all():
        professional_array.append(user)
    return professional_array


def resolve_professional(*_, user_id):
    user_checked = Professional.objects.filter(id=user_id)
    if len(user_checked) < 1:
        return {"error": "Ce professionnel n'existe pas."}
    else:
        user = Professional.objects.get(id=user_id)
        return {"success": user}


def resolve_create_professional(*_, username, password, email, firstname="", lastname="", company_id):
    user_email = Professional.objects.filter(email=email)
    user_username = Professional.objects.filter(username=username)
    company = Companies.objects.filter(id=company_id)
    if len(user_email) > 0:
        return {"error": "Cette email existe déja."}
    elif len(user_username) > 0:
        return {"error": "Cette username existe déja."}
    elif len(company) < 1:
        return {"error": "Cette entreprise n'existe pas."}
    else:
        Professional.objects.create_user(
            email=email,
            password=password,
            username=username,
            last_name=lastname,
            first_name=firstname,
            company_id=company_id
        )
        return {"success": "L'utilisateur %s a bien été créé" % username}


def resolve_delete_professional(*_, user_id):
    user = Professional.objects.get(id=user_id)
    user.delete()
    return {"success": "L'utilisateur %s a bien été supprimé" % user.username}


def resolve_update_professional(*_, user_id, email=None, password=None, username=None, firstname=None, lastname=None):
    user = Professional.objects.get(id=user_id)
    if email is None and password is None and username is None and firstname is None and lastname is None:
        return {"error": "Merci de selectionner une propriétée a modifier."}
    else:
        user.email = email or user.email
        user.password = password or user.password
        user.username = username or user.username
        user.first_name = firstname or user.first_name
        user.last_name = lastname or user.last_name
        user.save()
        return {"success": "L'utilisateur a bien été modifié."}

