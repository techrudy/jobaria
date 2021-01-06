from api.models import Companies, Professional
import jwt


def resolve_companies(*_):
    try:
        companies_array = []
        for user in Companies.objects.all():
            companies_array.append(user)
        return companies_array
    except ValueError:
        return ValueError


def resolve_company(*_, company_id):
    try:
        company_checked = Companies.objects.filter(id=company_id)
        if len(company_checked) < 1:
            return {"error": "Cette entreprise n'existe pas."}
        else:
            company = Companies.objects.get(id=company_id)
            return {"success": company}
    except ValueError:
        return ValueError


def resolve_create_company(*_, name, description):
    try:
        company = Companies.objects.filter(name=name)
        if len(company) > 0:
            return {"error": "Ce nom d'entreprise existe déja."}
        else:
            company = Companies.objects.create(name=name, description=description)
            return {"success": {"msg": "L'entreprise %s a bien été créée" % name, "company": company}}
    except ValueError:
        return ValueError


def resolve_update_company(_, info, company_id, name=None, description=None):
    try:
        if name is None and description is None:
            return {"error": "Merci de selectionner une propriétée a modifier."}
        else:
            request = info.context.get('request')
            token = request.headers.get('Authorization').split()[1]
            decode_jwt = jwt.decode(token, 'JobAria', algorithms='HS256')
            professional = Professional.objects.get(id=decode_jwt.get("user_id"))
            company = Companies.objects.get(id=company_id)
            if company.id != professional.company_id:
                return {"error": "Accès refusé."}
            else:
                company.name = name or company.name
                company.description = description or company.description
                company.save()
                return {"success": "Votre entreprise a bien été modifiée."}
    except ValueError:
        return ValueError


def resolve_delete_company(_, info, company_id):
    try:
        request = info.context.get('request')
        token = request.headers.get('Authorization').split()[1]
        decode_jwt = jwt.decode(token, 'JobAria', algorithms='HS256')
        professional = Professional.objects.get(id=decode_jwt.get("user_id"))
        company = Companies.objects.get(id=company_id)
        if company.id != professional.company_id:
            return {"error": "Accès refusé."}
        else:
            company.delete()
            return {"success": "Votre Entreprise a été supprimée."}
    except ValueError:
        return ValueError
