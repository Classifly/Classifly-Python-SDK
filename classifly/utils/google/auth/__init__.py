from firebase_admin.auth import Client
from firebase_admin import App
from firebase_admin.credentials import ApplicationDefault

CLIENT = Client(
    app=App(
        name="Classifly",
        credential=ApplicationDefault(),
        options=None
    )
)
