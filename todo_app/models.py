from django.db import models


# Create your models here.
from django.urls import reverse


class Tasks(models.Model):
    title = models.CharField(max_length=10)
    description = models.CharField(null=True, blank=True, max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=False)
    status = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.id)]
        )

    # def __str__(self):
    #     return f"{self.title}: due {self.due_date}"

    class Meta:
        ordering = ["due_date"]
