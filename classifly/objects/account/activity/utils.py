from classifly.objects.utils.document_reference.decorators import convert_to_classifly_object
from classifly.objects.account.activity.singular import Activity

def convert_to_activity(func):
    return convert_to_classifly_object(classifly_object_type=Activity)(func)
