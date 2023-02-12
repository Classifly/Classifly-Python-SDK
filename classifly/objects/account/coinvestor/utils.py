from classifly.objects.utils.document_reference.decorators import convert_to_classifly_object
from classifly.objects.account.coinvestor.singular import CoInvestor

def convert_to_coinvestor(func):
    return convert_to_classifly_object(classifly_object_type=CoInvestor)(func)
