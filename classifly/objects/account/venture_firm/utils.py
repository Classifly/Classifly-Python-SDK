from classifly.objects.utils.document_reference.decorators import convert_to_classifly_object
from classifly.objects.account.venture_firm.singular import VentureFirm

def convert_to_venture_firm(func):
    return convert_to_classifly_object(classifly_object_type=VentureFirm)(func)
