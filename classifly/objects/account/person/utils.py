from classifly.objects.utils.document_reference.decorators import convert_to_classifly_object
from classifly.objects.account.person.singular import Person

def convert_to_person(func):
    return convert_to_classifly_object(classifly_object_type=Person)(func)
