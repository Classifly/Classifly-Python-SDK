from classifly.objects.utils.document_reference.decorators import convert_to_classifly_object
from classifly.objects.account.distribution.singular import Distribution

def convert_to_distribution(func):
    return convert_to_classifly_object(classifly_object_type=Distribution)(func)
