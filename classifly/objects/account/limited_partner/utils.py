from classifly.objects.utils.document_reference.decorators import convert_to_classifly_object
from classifly.objects.account.limited_partner.singular import LimitedPartner

def convert_to_limited_partner(func):
    return convert_to_classifly_object(classifly_object_type=LimitedPartner)(func)
