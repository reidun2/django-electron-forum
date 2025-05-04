from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HomeView, add_category, category_detail, forum_detail, CategoryViewSet, LoginView, ProtectedView, DeleteMessageView, MessageViewSet, AdsViewSet, DeleteAdView
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'messages', MessageViewSet)
router.register(r'ads', AdsViewSet, basename='ads')

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add-category/', add_category, name='add-category'),
    path('forum/<int:global_id>/', forum_detail, name='forum-detail'),
    path('apil/', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('<slug:slug>/', category_detail, name='category-detail'),
    path('messages/<int:pk>/delete/', DeleteMessageView.as_view(), name='delete-message'),
    path('ads/<int:pk>/delete/', DeleteAdView.as_view(), name='delete-ad'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)