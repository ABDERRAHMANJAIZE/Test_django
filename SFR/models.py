from django.db import models


class SearchHistory(models.Model):
    title = models.CharField(max_length=255)
    is_series = models.BooleanField()
    searched_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ordonner les résultats par date de recherche, du plus récent au plus ancien
        ordering = ['-searched_at']

    def __str__(self):
        return self.title
