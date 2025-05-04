from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from .models import Category, Forum, Message, GlobalCounter, Moderator, Ad
from .forms import CategoryForm, ForumForm, MessageForm
from .serializers import CategorySerializer, MessageSerializer, AdsSerializer
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class HomeView(ListView):
    model = Category
    template_name = 'forums/base.html'
    context_object_name = 'categories'
    
    def get_queryset(self):
        return Category.objects.all()  

def home_view(request):
    categories_data = []
    for name, slug in categories_data:
        Category.objects.get_or_create(name=name, slug=slug)
    categories = Category.objects.all()
    return render(request, 'forums/category.html', {'categories': categories})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('category-list') 
    else:
        form = CategoryForm()

    return render(request, 'forums/add_category.html', {'form': form})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    forums = Forum.objects.filter(category=category).order_by('-id')
    if request.method == 'POST':
        form = ForumForm(request.POST, request.FILES)
        if form.is_valid():
            forum = form.save(commit=False)
            forum.category = category
            forum.global_id = GlobalCounter.get_next()
            forum.save()
            return redirect('forum-detail', global_id=forum.global_id)
    else:
        form = ForumForm()
    return render(request, 'forums/create_forum.html', {'form': form, 'category': category, 'forums': forums})

def forum_detail(request, global_id):
    forum = get_object_or_404(Forum, global_id=global_id)
    messages = forum.messages.order_by('created_at')
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.forum = forum
            message.global_id = GlobalCounter.get_next()
            message.save()
            return redirect('forum-detail', global_id=forum.global_id)
    else:
        form = MessageForm()
    return render(request, 'forums/forum_detail.html', {'forum': forum, 'messages': messages, 'form': form})

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class AdsViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdsSerializer

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):

    def get(self, request):
        return Response({'detail': 'CSRF cookie set'})

    def post(self, request, *args, **kwargs):

        username = request.data.get('username')
        password = request.data.get('password')

        try:
            mod = Moderator.objects.get(username=username, password=password)
            return Response({'token': 'dummy-token-123'}, status=status.HTTP_200_OK)
        except Moderator.DoesNotExist:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_403_FORBIDDEN)

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Access granted!"})

class DeleteMessageView(View):
    def post(self, request, pk):
        message = Message.objects.get(pk=pk)
        message.delete()
        return redirect('forum-detail')

class DeleteAdView(View):
    def post(self, request, pk):
        ad = Ad.objects.get(pk=pk)
        ad.delete()
        return redirect('home-view')