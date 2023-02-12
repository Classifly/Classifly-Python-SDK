from google.cloud.firestore import FirestoreProperty

from classifly.objects.utils.document_reference.core import CoreClassiflyDocumentReference
# from quickbooks import QuickBooks

class QuickbooksIntegration(CoreClassiflyDocumentReference):
    """
        A Classifly QuickBooks Integration.
    """
    access_token: str = FirestoreProperty("access_token",str)
    refresh_token: str = FirestoreProperty("refresh_token",str)
    realm_id: str = FirestoreProperty("realm_id",str)

    gp_account: str = FirestoreProperty("gp_account",str)
    gp_contributions_account: str = FirestoreProperty("gp_contributions_account",str)
    gp_distributions_account: str = FirestoreProperty("gp_distributions_account",str)
    # ...

    def __init__(self, *args, quickbooks_integration_id: str=None) -> None:
        if len(args) == 1:
            super().__init__(*args)
        else:
            super().__init__(*["Integrations","Quickbooks","Entities",quickbooks_integration_id])
