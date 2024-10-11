from django.db import models


class WeatherData(models.Model):
    temperature = models.FloatField()  # Para armazenar a temperatura
    # Para armazenar o status da chuva
    rain_status = models.CharField(max_length=20)
    # Para armazenar o horário da leitura
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.timestamp}: {self.temperature}°C, {self.rain_status}"
