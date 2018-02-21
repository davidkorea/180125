from django.shortcuts import render
from django_web.models import LogInfo
from django.core.paginator import Paginator

def index(request):
    limit = 10
    log_info = LogInfo.objects[:10]
    print(log_info)
    paginator = Paginator(log_info, limit)
    page = request.GET.get('page', 1)
    print(request)
    print(request.GET)
    print(page)
    loaded = paginator.page(page)
    print(loaded)
    context = {
        'LogInfo':loaded
    }
    return render(request, 'index.html', context)


def default(request):
    limit = 10
    log_info = LogInfo.objects
    paginator = Paginator(log_info, limit)
    page = request.GET.get('page', 1)
    loaded = paginator.page(page)
    context = {
        'LogInfo': loaded,
        'counts': log_info.count(),
        'last_time': log_info.order_by('-date').limit(1),
    }
    return render(request, 'default_data.html', context)

# ==========Data Generator==========

def topx_data_gen(date1, date2, member, limit):

    pipeline = [
        {'$match': {'$and': [{'date': {'$gte': date1, '$lte': date2}}, {'handle_by': member}]}},
        {'$group': {'_id': '$city', 'counts': {'$sum': 1}}},
        {'$sort': {'counts': -1}},
        {'$limit': limit}
    ]

    for i in LogInfo._get_collection().aggregate(pipeline):
        data = {
            'name': i['_id'],
            'data': [i['counts']],
            'type': 'column'
        }
        yield data

series_andy = [i for i in topx_data_gen('2017/01/01','2017/12/31','Andy Tsao',10) ]
series_david = [i for i in topx_data_gen('2017/01/01','2017/12/31','David Liu',10) ]


#============end===============
def charts(request):
    context = {
        'chart_andy': series_andy,
        'chart_david': series_david,
    }
    return render(request, 'default_charts.html', context)