from classifly.objects.utils.document_reference.decorators import convert_to_classifly_object
from classifly.objects.account.coinvestment.singular import CoInvestment

def convert_to_coinvestment(func):
    return convert_to_classifly_object(classifly_object_type=CoInvestment)(func)
