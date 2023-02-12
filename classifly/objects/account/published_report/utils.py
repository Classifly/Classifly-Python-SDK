from classifly.objects.utils.document_reference.decorators import convert_to_classifly_object
from classifly.objects.account.published_report.singular import PublishedReport

def convert_to_published_report(func):
    return convert_to_classifly_object(classifly_object_type=PublishedReport)(func)
