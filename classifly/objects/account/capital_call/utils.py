from classifly.objects.utils.document_reference.decorators import convert_to_classifly_object
from classifly.objects.account.capital_call.singular import CapitalCall

def convert_to_capital_call(func):
    return convert_to_classifly_object(classifly_object_type=CapitalCall)(func)
