from django.db import models


class Coin(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    decimals = models.BigIntegerField()

    def __str__(self):
        return self.name


class Dex(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    abi = models.TextField()

    def __str__(self):
        return self.name


class CoinPair(models.Model):
    coin_1 = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name='coin_1', blank=True, null=True)
    coin_2 = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name='coin_2', blank=True, null=True)

    def __str__(self):
        return f"{self.coin_1} ---- {self.coin_2}"


class DexPair(models.Model):
    dex_1 = models.ForeignKey(Dex, on_delete=models.CASCADE, related_name='dex_1', blank=True, null=True)
    dex_2 = models.ForeignKey(Dex, on_delete=models.CASCADE, related_name='dex_2', blank=True, null=True)

    def __str__(self):
        return f"{self.dex_1} ---- {self.dex_2}"


class Result(models.Model):

    coin_pair = models.CharField(max_length=255)
    price_difference = models.CharField(max_length=255)
    dex_pair = models.CharField(max_length=255)
    percentage = models.FloatField()
    date = models.TextField(null=True,blank=True)
    dexes = models.CharField(max_length=255)