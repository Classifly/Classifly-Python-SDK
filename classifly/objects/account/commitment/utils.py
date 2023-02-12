from classifly.objects.utils.document_reference.decorators import convert_to_classifly_object
from classifly.objects.account.commitment.singular import Commitment

def convert_to_commitment(func):
    return convert_to_classifly_object(classifly_object_type=Commitment)(func)
