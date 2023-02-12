from classifly.objects.utils.document_reference.decorators import convert_to_classifly_object
from classifly.objects.account.document.singular import Document

def convert_to_document(func):
    return convert_to_classifly_object(classifly_object_type=Document)(func)
