from io import BytesIO

import requests

from app.core.config import settings

class BucketService:
    def __init__(self, url):
        self.url = url

    def post(self, file: BytesIO):
        headers = {'accept': 'application/json'}
        files = {'file': ('factura.pdf', file, 'application/pdf')}
        response = requests.post(self.url, headers=headers, files=files)
        return response.json()
    

bucket_service = BucketService(settings.DATABASE_URL + '/bucket/')