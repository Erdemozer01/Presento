from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from hitcount.views import HitCountDetailView

from .models import Portfolio, PortFolioAddContentModel, ArticleModel, ArticleTags, ArticleComment, ArticleCategory


class PortfolioListView(generic.ListView):
    model = Portfolio
    template_name = 'pages/portfolio.html'

    def get_context_data(self, *, object_list=..., **kwargs):
        context = super().get_context_data(**kwargs)
        context['portfolio_detail'] = PortFolioAddContentModel.objects.all()
        return context


class PortfolioDetailView(generic.ListView):
    model = PortFolioAddContentModel
    template_name = 'pages/portfolio-details.html'
    paginate_by = 1

    def get_queryset(self):
        return PortFolioAddContentModel.objects.filter(portfolio_id=self.kwargs['pk'])


class ArticleCategoryListView(generic.ListView):
    model = ArticleCategory
    template_name = 'pages/blog.html'
    paginate_by = 9

    def get_queryset(self):
        object_list = ArticleModel.objects.filter(status='PB', category__title=self.kwargs['title'])

        ara = self.request.GET.get('ara')
        if ara:
            object_list = object_list.filter(Q(title__icontains=ara) | Q(category__title__icontains=ara))
            messages.success(self.request, f'{len(object_list)} makale bulundu')
        return object_list


class ArticleListView(generic.ListView):
    model = ArticleModel
    template_name = 'pages/blog.html'
    paginate_by = 9

    def get_queryset(self):
        object_list = ArticleModel.objects.filter(status='PB')
        ara = self.request.GET.get('ara')
        if ara:
            object_list = object_list.filter(Q(title__icontains=ara) | Q(category__title__icontains=ara))
            messages.success(self.request, f'{len(object_list)} makale bulundu')
        return object_list


class ArticleDetailView(HitCountDetailView, generic.DetailView):
    model = ArticleModel
    template_name = 'pages/blog-details.html'
    count_hit = True

    def get(self, request, *args, **kwargs):
        yorum = request.GET.get('comment', None)
        if yorum:
            ArticleComment.objects.create(
                article_id=kwargs['pk'],
                comment=yorum,
                author=self.request.user,
            )
            messages.success(request, 'Yorumunuz eklenmiştir.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_post'] = ArticleModel.objects.filter(status='PB')[:10]
        return context


class ArticleTagsListView(generic.ListView):
    model = ArticleTags
    template_name = 'pages/blog.html'
    paginate_by = 9

    def get_queryset(self):
        object_list = ArticleModel.objects.filter(status='PB', article_tags__tags__icontains=self.kwargs['tags'])
        ara = self.request.GET.get('ara')
        if ara:
            object_list = object_list.filter(Q(title__icontains=ara) | Q(category__title__icontains=ara))
            messages.success(self.request, f'{len(object_list)} makale bulundu')
        return object_list


class ArticleAuthorListView(generic.ListView):
    model = ArticleModel
    template_name = 'pages/blog.html'
    paginate_by = 9

    def get_queryset(self):
        object_list = ArticleModel.objects.filter(status='PB', author__username=self.kwargs['user'])
        ara = self.request.GET.get('ara')
        if ara:
            object_list = object_list.filter(Q(title__icontains=ara) | Q(category__title__icontains=ara))
            messages.success(self.request, f'{len(object_list)} makale bulundu')
        return object_list


def comment_report_view(request, pk):
    obj = ArticleComment.objects.get(pk=pk)
    obj.report_count += 1
    obj.save()
    if obj.report_count > 10:
        obj.delete()
    messages.success(request, 'Yorum rapor edilmiştir.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class MountArticleListView(generic.MonthArchiveView):
    model = ArticleModel
    template_name = 'pages/blog.html'
    paginate_by = 9
    allow_future = True
    date_field = 'created_at'
    month_format = '%m'

    def get_queryset(self):
        object_list = ArticleModel.objects.filter(status='PB', created_at__month=self.kwargs['month'])
        ara = self.request.GET.get('ara')
        if ara:
            object_list = object_list.filter(Q(title__icontains=ara) | Q(category__title__icontains=ara))
            messages.success(self.request, f'{len(object_list)} makale bulundu')
        return object_list
