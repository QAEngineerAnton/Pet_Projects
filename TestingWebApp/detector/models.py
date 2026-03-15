from django.db import models

class TextCheck(models.Model):
    input_text = models.CharField(max_length=500, verbose_name="Входная строка")
    detected_bugs = models.JSONField(default=list, verbose_name="Найденные баги")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Check {self.id}: {self.input_text[:20]}..."