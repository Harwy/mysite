import datetime
from django.shortcuts import render_to_response, render, redirect
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from django.core.cache import cache

from read_statistics.utils import get_seven_days_read_data, get_today_hot_data, get_yesterday_hot_data
from blog.models import Blog


'''七日内最火博客'''
def get_seven_days_hot_data():
    today = timezone.now().date()
    date = today - datetime.timedelta(days=7)
    blogs = Blog.objects \
                        .filter(read_detail__date__lt=today, read_detail__date__gte=date) \
                        .values('id', 'title') \
                        .annotate(read_num_sum=Sum('read_detail__read_num')) \
                        .order_by('-read_num_sum')
    return blogs[:7]


'''主页显示'''
def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = get_seven_days_read_data(blog_content_type)

    # 获取7天热门博客的缓存数据
    seven_hot_data = cache.get('seven_hot_data')
    if seven_hot_data is None:
        seven_hot_data = get_seven_days_hot_data()
        cache.set('seven_hot_data', seven_hot_data, 3600)

    context={}
    context['read_nums'] = read_nums
    context['today_hot_data'] = get_today_hot_data(blog_content_type)
    context['yesterday_hot_data'] = get_yesterday_hot_data(blog_content_type)
    context['seven_hot_data'] = seven_hot_data
    context['dates'] = dates
    return render(request, 'home.html', context)


