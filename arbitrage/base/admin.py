from django.contrib import admin
from .models import Coin, Dex, CoinPair, DexPair, Result

admin.site.register(Coin)
admin.site.register(Dex)
admin.site.register(CoinPair)
admin.site.register(DexPair)


class ResultAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Result._meta.get_fields()]


admin.site.register(Result, ResultAdmin)
