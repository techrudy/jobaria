from api.models import JobOffers, Professional, Candidate
import jwt


def resolve_job_offers(*_):
    try:
        job_offers_array = []
        for job_offer in JobOffers.objects.all():
            job_offers_array.append(job_offer)
        return job_offers_array
    except ValueError:
        return ValueError


def resolve_job_offer(*_, job_offer_id):
    try:
        job_offer_checked = JobOffers.objects.filter(id=job_offer_id)
        if len(job_offer_checked) < 1:
            return {"error": "Cette offre d'emploi n'existe pas."}
        else:
            job_offer = JobOffers.objects.get(id=job_offer_id)
            return {"success": job_offer}
    except ValueError:
        return ValueError


def resolve_create_job_offer(*_, title, description, company_id):
    try:
        JobOffers.objects.create(
            title=title,
            description=description,
            company_id=company_id,
        )
        return {"success": "Votre offre d'emploi a bien été créée."}
    except ValueError:
        return ValueError


def resolve_update_job_offer(_, info, job_offer_id, title=None, description=None):
    try:
        if title is None and description is None:
            return {"error": "Merci de selectionner une propriétée a modifier."}
        else:
            request = info.context.get('request')
            token = request.headers.get('Authorization').split()[1]
            decode_jwt = jwt.decode(token, 'JobAria', algorithms='HS256')
            professional = Professional.objects.get(id=decode_jwt.get("user_id"))
            job_offer = JobOffers.objects.get(id=job_offer_id)
            if job_offer.company_id != professional.company_id:
                return {"error": "Acces refusé"}
            else:
                job_offer.title = title or job_offer.title
                job_offer.description = description or job_offer.description
                job_offer.save()
                return {"success": "Votre offre d'emploi a bien été modifiée."}
    except ValueError:
        return ValueError


def resolve_delete_job_offer(_, info, job_offer_id):
    try:
        request = info.context.get('request')
        token = request.headers.get('Authorization').split()[1]
        decode_jwt = jwt.decode(token, 'JobAria', algorithms='HS256')
        professional = Professional.objects.get(id=decode_jwt.get("user_id"))
        job_offer = JobOffers.objects.get(id=job_offer_id)
        if job_offer.company_id != professional.company_id:
            return {"error": "Acces refusé"}
        else:
            job_offer = JobOffers.objects.get(id=job_offer_id)
            job_offer.delete()
            return {"success": "L'offre d'emploi %s a bien été supprimé" % job_offer.title}
    except ValueError:
        return ValueError


def resolve_apply_job_offer(_, info, job_offer_id):
    try:
        request = info.context.get('request')
        token = request.headers.get('Authorization').split()[1]
        decode_jwt = jwt.decode(token, 'JobAria', algorithms='HS256')
        user = Candidate.objects.get(id=decode_jwt.get("user_id"))
        job_offer_checked = JobOffers.objects.filter(id=job_offer_id)
        if len(job_offer_checked) < 1:
            return {"error": "Cette offre d'emploi n'existe pas."}
        else:
            job_offer = JobOffers.objects.get(id=job_offer_id)
            candidate_checked = job_offer.candidate.filter(id__contains=user.id)
            if len(candidate_checked) > 0:
                return {"error": "Vous avez deja candidaté pour cette offre d'emploie."}
            else:
                job_offer.candidate.add(user)
                job_offer.save()
                return {"success": "Félicitation vous avez candidaté"}
    except ValueError:
        return ValueError


def resolve_remove_apply_job_offer(_, info, job_offer_id):
    try:
        request = info.context.get('request')
        token = request.headers.get('Authorization').split()[1]
        decode_jwt = jwt.decode(token, 'JobAria', algorithms='HS256')
        user = Candidate.objects.get(id=decode_jwt.get("user_id"))
        job_offer_checked = JobOffers.objects.filter(id=job_offer_id)
        if len(job_offer_checked) < 1:
            return {"error": "Cette offre d'emploi n'existe pas."}
        else:
            job_offer = JobOffers.objects.get(id=job_offer_id)
            candidate_checked = job_offer.candidate.filter(id__contains=user.id)
            if len(candidate_checked) < 1:
                return {"error": "Vous n'avez pas candidaté pour cette offre d'emploie."}
            else:
                job_offer.candidate.remove(user)
                job_offer.save()
                return {"success": "Votre candidature a été supprimée."}
    except ValueError:
        return ValueError
