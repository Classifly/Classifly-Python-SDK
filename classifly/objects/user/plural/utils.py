from classifly.objects.utils.document_reference.decorators import convert_to_classifly_object
from classifly.objects.user.singular import User

def convert_to_user(func):
    return convert_to_classifly_object(classifly_object_type=User)(func)
