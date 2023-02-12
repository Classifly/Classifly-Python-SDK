from classifly.objects.utils.document_reference.decorators import convert_to_classifly_object
from classifly.objects.account.report.recipient.singular import ReportRecipient

def convert_to_report_recipient(func):
    return convert_to_classifly_object(classifly_object_type=ReportRecipient)(func)