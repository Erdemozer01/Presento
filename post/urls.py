from django.urls import path
from post import views

app_name = 'post'

urlpatterns = [
    path('portfolio/', views.PortfolioListView.as_view(), name='portfolio'),
    path('portfolio/<pk>/<category>/<slug>/', views.PortfolioDetailView.as_view(), name='portfolio_details'),
    path('blog/', views.ArticleListView.as_view(), name='blog'),
    path('blog/<pk>/<slug>/', views.ArticleDetailView.as_view(), name='blog_details'),
    path('blog/<tags>-etiketi/', views.ArticleTagsListView.as_view(), name='tags_list'),
    path('blog/<title>-kategorisi/', views.ArticleCategoryListView.as_view(), name='category_list'),
    path('blog/<user>-Makaleleri/', views.ArticleAuthorListView.as_view(), name='author_list'),
    path('report-comment/<pk>/', views.comment_report_view, name='comment_report'),
    path('blog-<int:year>/ay-<str:month>-gönderileri/', views.MountArticleListView.as_view(), name='mount_list'),
]
