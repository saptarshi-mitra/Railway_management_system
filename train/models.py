from django.db import models


class Train(models.Model):
    train_no = models.IntegerField(default=None, blank=True, null=True)
    train_name = models.CharField(max_length=50)

    def __str__(self):
        return self.train_name


class Station(models.Model):
    station_id = models.IntegerField(default=None, blank=True, null=True)
    station_name = models.CharField(max_length=50, blank=True)
    train_no = models.ForeignKey(Train, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.station_name
