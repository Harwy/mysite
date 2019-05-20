from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.paginator import Paginator
from django.conf import settings
from django.db.models import Count
from .models import Blog, BlogType

'''阅读计数APP引用utils工具'''
from read_statistics.utils import read_statistics_once_read


'''共同代码段'''
def get_blog_list_common_data(request, blogs_all_list):
    paginator = Paginator(blogs_all_list, settings.EACH_PAGE_BLOG_NUMBER)  # 每页文章分页数
    page_num = request.GET.get('page', 1)  # 获取页码参数（GET请求）
    page_of_blogs = paginator.get_page(page_num)
    currentr_page_num = page_of_blogs.number  # 获取当前页码
    # 获取当前页码前后各3页的页码范围
    page_range = list(range(max(currentr_page_num - 3, 1), currentr_page_num)) + \
                 list(range(currentr_page_num, min(currentr_page_num + 3, paginator.num_pages) + 1))
                 # python3 range得到的是生成器，需要list化。。。而python2 range得到的list
    # 加上省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    # 获取博客分类对应的博客数量(annotate:拓展查询字段)
    blog_with_type_all = BlogType.objects.annotate(blog_count=Count('blog'))

    # 获取日期归档对应的博客数量
    blog_dates = Blog.objects.dates('created_time', 'month', order="DESC")
    blog_dates_dict = {}
    for blog_date in blog_dates:
        blog_count = Blog.objects.filter(created_time__year=blog_date.year,
                            created_time__month=blog_date.month).count()
        # blog_date为键值，对应blog_count
        blog_dates_dict[blog_date] = blog_count

    context = {}
    context['blogs'] = page_of_blogs.object_list  # 当前页对象列表（方便前端书写）
    context['page_of_blogs'] = page_of_blogs  # 当前页对象
    context['page_range'] = page_range
    # context['blogs_count'] = Blog.objects.all().count() # 统计博客
    context['blog_types'] = blog_with_type_all
    context['blog_dates'] = blog_dates_dict
    return context


'''访问博客列表'''
def blog_list(request):
    blogs_all_list = Blog.objects.all()
    context = get_blog_list_common_data(request, blogs_all_list)
    return render(request, 'blog/blog_list.html', context)


'''单类型博客'''
def blogs_with_type(request, blog_type_pk):
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    blogs_all_list = Blog.objects.filter(blog_type=blog_type)
    context = get_blog_list_common_data(request, blogs_all_list)
    context['blog_type'] = blog_type
    return render(request, 'blog/blogs_with_type.html', context)


'''按日期分类的博客'''
def blogs_with_date(request, year, month):
    blogs_all_list = Blog.objects.filter(created_time__year=year, created_time__month=month)
    context = get_blog_list_common_data(request, blogs_all_list)
    context['blogs_with_date'] = "%s年%s月" % (year, month)
    return render(request, 'blog/blogs_with_date.html', context)


'''单篇博客'''
def blog_detail(request, blog_pk):
    blog = get_object_or_404(Blog, pk=blog_pk)
    read_cookie_key = read_statistics_once_read(request, blog)  # read_statistics模块阅读计数方法

    context = {}
    context['previous_blog'] = Blog.objects.filter(created_time__gt=blog.created_time).last()
    context['next_blog'] = Blog.objects.filter(created_time__lt=blog.created_time).first()
    context['blog'] = blog
    response = render(request, 'blog/blog_detail.html', context)  # 响应
    response.set_cookie(read_cookie_key, 'true')  # 阅读cookie标记
    return response


'''博客发表时间轴显示'''
def blog_timeline(request):
    context = {}
    blogs_all_list = Blog.objects.all()
    context['blogs'] = blogs_all_list
    return render(request, 'blog/timeline.html', context)
    