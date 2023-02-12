from google.cloud.secretmanager import SecretManagerServiceClient

class ClassiflySecretManagerServiceClient(SecretManagerServiceClient):
    def access_secret_version(self, name: str):
        """
            To-Do
        """
        return super().access_secret_version(
            name=f"projects/205341574495/secrets/{name}/versions/latest"
        )
