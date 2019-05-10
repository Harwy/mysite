import datetime
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from .models import ReadNum, ReadDetail

'''
阅读计数模块方法
输入：request对象 | 对应model
操作：未有cookie键值时对应model阅读计数+1
返回：cookie操作键值
'''
def read_statistics_once_read(request, obj):
    ct = ContentType.objects.get_for_model(obj)
    key = '%s_%s_read' % (ct.model, obj.pk)

    if not request.COOKIES.get(key):
        # 总阅读数+1
        readnum, created = ReadNum.objects.get_or_create(content_type=ct, object_id=obj.pk)
        readnum.read_num += 1
        readnum.save()

        # 当天阅读数+1
        date = timezone.now().date()
        readDetail, created = ReadDetail.objects.get_or_create(content_type=ct, object_id=obj.pk, date=date)
        readDetail.read_num += 1
        readDetail.save()
    return key


'''
7日阅读量方法
输入：content_type(用法：ContentType.objects.get_for_model(Blog))
操作：通过输入模型返回前7日read_num以及对应日期
返回：元组(日期， 阅读量)
'''
def get_seven_days_read_data(content_type):
    today = timezone.now().date()
    read_nums = []
    dates = []
    for i in range(7, 0, -1):
        date = today - datetime.timedelta(days=i)
        dates.append(date.strftime('%m/%d'))
        read_details = ReadDetail.objects.filter(content_type=content_type, date=date)
        result = read_details.aggregate(read_num_sum=Sum('read_num'))  # 针对阅读数数据库聚合
        read_nums.append(result['read_num_sum'] or 0)
    return dates, read_nums


'''今日最火博客'''
def get_today_hot_data(content_type):
    today = timezone.now().date()
    read_details = ReadDetail.objects.filter(content_type=content_type, date=today).order_by('-read_num')  # 对查询结果重新排序
    return read_details[:7]


'''昨日最火博客'''
def get_yesterday_hot_data(content_type):
    today = timezone.now().date()
    yesterday = today - datetime.timedelta(days=1)
    read_details = ReadDetail.objects.filter(content_type=content_type, date=yesterday).order_by('-read_num')  # 对查询结果重新排序
    return read_details[:7]


'''七日内最火博客(在mysite/views.py下实现)'''
'''def get_seven_days_hot_data(content_type):
    today = timezone.now().date()
    date = today - datetime.timedelta(days=7)
    read_details = ReadDetail.objects \
                            .filter(content_type=content_type, date__lt=today, date__gte=date) \
                            .values('content_type', 'object_id') \
                            .annotate(read_num_sum=Sum('read_num')) \
                            .order_by('-read_num_sum')
    return read_details[:7]'''


