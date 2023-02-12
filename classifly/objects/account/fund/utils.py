from classifly.objects.utils.document_reference.decorators import convert_to_classifly_object
from classifly.objects.account.fund.singular import Fund

def convert_to_fund(func):
    return convert_to_classifly_object(classifly_object_type=Fund)(func)
