from django.http import JsonResponse
from .models import Result
from .prices import sort_pair_price_result, get_percentage


def collect_data(*args, **kwargs):
    result = sort_pair_price_result()
    for index, row in result.iterrows():
        res = Result(coin_pair=row['coin_pair'],
                     price_difference=row['price_defference'],
                     dex_pair=row["dex_pair"],
                     percentage=get_percentage(),
                     date=row['date_added'],
                     dexes=list(row[4:])

                     )
        res.save()

    return JsonResponse({'message': 'success'})

# def clean_db():
#     delatable_objects = Result.objects.all()[0:500]
#     for m in delatable_objects:
#         m.delete()
#
#
# clean_db()
