from classifly.objects.utils.document_reference.decorators import convert_to_classifly_object
from classifly.objects.account.investment.singular import Investment

def convert_to_investment(func):
    return convert_to_classifly_object(classifly_object_type=Investment)(func)
