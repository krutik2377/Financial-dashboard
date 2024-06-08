from djongo import models

class FinancialRecord(models.Model):
    title = models.CharField(max_length=100)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
