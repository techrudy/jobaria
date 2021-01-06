from ariadne import QueryType, MutationType, make_executable_schema, load_schema_from_path
from ariadne.contrib.django.scalars import date_scalar, datetime_scalar

from .resolvers.candidate_resolvers import \
    resolve_candidates, \
    resolve_candidate,\
    resolve_create_candidate, \
    resolve_delete_candidate, \
    resolve_update_candidate

from .resolvers.professional_resolvers import \
    resolve_professionals, \
    resolve_professional,\
    resolve_create_professional,\
    resolve_update_professional,\
    resolve_delete_professional

from .resolvers.company_resolvers import \
    resolve_companies,\
    resolve_company,\
    resolve_create_company,\
    resolve_update_company,\
    resolve_delete_company

from .resolvers.authenticate_resolvers import \
    resolve_login_user,\
    resolve_check_auth

from .resolvers.job_offer_resolvers import \
    resolve_job_offers,\
    resolve_job_offer,\
    resolve_create_job_offer,\
    resolve_update_job_offer,\
    resolve_delete_job_offer,\
    resolve_apply_job_offer,\
    resolve_remove_apply_job_offer

from .middleware.check_profile import \
    middleware_auth_professional,\
    middleware_auth_candidate,\
    middleware_auth_user

type_defs = load_schema_from_path("./api/type_defs")

query = QueryType()
mutation = MutationType()

query.set_field("candidates", resolve_candidates)
query.set_field("candidate", resolve_candidate)
mutation.set_field("createCandidate", resolve_create_candidate)
mutation.set_field("deleteCandidate", middleware_auth_candidate(resolve_delete_candidate))
mutation.set_field("updateCandidate", middleware_auth_candidate(resolve_update_candidate))

query.set_field("professionals", resolve_professionals)
query.set_field("professional", resolve_professional)
mutation.set_field("createProfessional", resolve_create_professional)
mutation.set_field("deleteProfessional", middleware_auth_professional(resolve_delete_professional))
mutation.set_field("updateProfessional", middleware_auth_professional(resolve_update_professional))

query.set_field("companies", resolve_companies)
query.set_field("company", resolve_company)
mutation.set_field("createCompany", resolve_create_company)
mutation.set_field("updateCompany", middleware_auth_professional(resolve_update_company))
mutation.set_field("deleteCompany", middleware_auth_professional(resolve_delete_company))

mutation.set_field("loginUser", resolve_login_user)
query.set_field("checkAuth", middleware_auth_user(resolve_check_auth))

query.set_field("jobOffers", resolve_job_offers)
query.set_field("jobOffer", resolve_job_offer)
mutation.set_field("createJobOffer", middleware_auth_professional(resolve_create_job_offer))
mutation.set_field("updateJobOffer", middleware_auth_professional(resolve_update_job_offer))
mutation.set_field("deleteJobOffer", middleware_auth_professional(resolve_delete_job_offer))
mutation.set_field("applyJobOffer", middleware_auth_candidate(resolve_apply_job_offer))
mutation.set_field("removeApplyJobOffer", middleware_auth_candidate(resolve_remove_apply_job_offer))

schema = make_executable_schema(type_defs, [query, mutation, datetime_scalar, date_scalar])
