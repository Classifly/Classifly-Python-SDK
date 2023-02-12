from classifly.objects.utils.document_reference.decorators import convert_to_classifly_object
from classifly.objects.account.report.singular import Report

def convert_to_report(func):
    return convert_to_classifly_object(classifly_object_type=Report)(func)
