from rest_framework import viewsets
from .models import FinancialRecord
from .serializers import FinancialRecordSerializer
from loguru import logger
from django.conf import settings
import redis

# Configure Redis client
redis_client = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)

class FinancialRecordViewSet(viewsets.ModelViewSet):
    queryset = FinancialRecord.objects.all()
    serializer_class = FinancialRecordSerializer

    def list(self, request, *args, **kwargs):
        logger.info("Listing financial records")
        response = super().list(request, *args, **kwargs)
        redis_client.set("financial_records", response.data)
        return response

    def create(self, request, *args, **kwargs):
        logger.info("Creating new financial record")
        response = super().create(request, *args, **kwargs)
        redis_client.delete("financial_records")
        return response

    def retrieve(self, request, *args, **kwargs):
        logger.info("Retrieving financial record")
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        logger.info("Updating financial record")
        response = super().update(request, *args, **kwargs)
        redis_client.delete("financial_records")
        return response

    def destroy(self, request, *args, **kwargs):
        logger.info("Deleting financial record")
        response = super().destroy(request, *args, **kwargs)
        redis_client.delete("financial_records")
        return response
