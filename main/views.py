from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.db.models import F

from .models import Category, Post, Team, Feedback, Subscriptions
from .forms import FeedbackForm, SubscriptionViewForm


def index(request):
    category = Category.objects.all()
    post_favourites = Post.objects.filter(category_id=2)
    post_upcoming = Post.objects.filter(category_id=4)
    post_match = Post.objects.filter(category_id=3)[:1]
    coach = Team.objects.all()[:4]
    events = Post.objects.filter(category_id=4)[:3]
    football = Post.objects.filter(category_id=6)[:2]
    advertisement = Post.objects.filter(category_id=7)[:2]
    context = {'category': category, 'post_favourites': post_favourites, 'post_upcoming': post_upcoming,
               'post_match': post_match, 'coach': coach, 'events': events, 'football': football,
               'advertisement': advertisement}
    return render(request, 'index.html', context)


# def detail(request, slug):
#     category = Category.objects.all()
#     post_detail = get_object_or_404(Post, slug=slug)
#     post_widget = Post.objects.exclude(category_id=7)[:3]
#     galery = Post.objects.exclude(category_id=7)
#     context = {'post_detail': post_detail, 'post_widget': post_widget, 'galery': galery, 'category': category}
#     return render(request, 'detail.html', context)


class PostDetail(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['post_widget'] = Post.objects.exclude(category_id=7)[:3]
        context['galery'] = Post.objects.exclude(category_id=7)[:6]
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context



def news_all(reqest):
    category = Category.objects.all()
    news = Post.objects.exclude(category_id=7)
    paginator = Paginator(news, 5)
    page_number = reqest.GET.get('page')
    page_obj = paginator.get_page(page_number)
    post_widget = Post.objects.exclude(category_id=7)[:3]
    galery = Post.objects.exclude(category_id=7)
    context = {'post_widget': post_widget, 'galery': galery, 'category': category, 'page_obj': page_obj}
    return render(reqest, 'news_all.html', context)


# def contact(request):
#     category = Category.objects.all()
#     context = {'category': category}
#     return render(request, 'contact.html', context)

class ContactView(SuccessMessageMixin, CreateView, ListView):
    model = Feedback
    template_name = 'contact.html'
    form_class = FeedbackForm
    success_url = reverse_lazy('contact')
    success_message = 'Обратная связь отправлена. Спасибо за отзыв!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


class TeamDetail(DetailView):
    model = Team
    template_name = 'team_detail.html'
    context_object_name = 'team'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['post_widget'] = Post.objects.exclude(category_id=7)[:3]
        context['galery'] = Post.objects.exclude(category_id=7)
        return context


class TeamAll(ListView):
    model = Team
    template_name = 'team.html'
    context_object_name = 'team_all'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['post_widget'] = Post.objects.exclude(category_id=7)[:3]
        context['galery'] = Post.objects.exclude(category_id=7)[:6]
        return context


def club(request):
    category = Category.objects.all()
    galery = Post.objects.exclude(category_id=7)[:6]
    post_widget = Post.objects.exclude(category_id=7)[:3]
    context = {'galery': galery, 'post_widget': post_widget, 'category': category}
    return render(request, 'club.html', context)


class CategoryNews(ListView):
    template_name = 'category_news.html'
    context_object_name = 'category_news'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        context['category'] = Category.objects.all()
        context['post_widget'] = Post.objects.exclude(category_id=7)[:3]
        context['galery'] = Post.objects.exclude(category_id=7)[:6]
        return context


class Galery(ListView):
    template_name = 'galery.html'
    context_object_name = 'galery'

    def get_queryset(self):
        return Post.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['category'] = Category.objects.all()
        context['galery'] = Post.objects.exclude(category_id=7)
        return context


def subscription(request):
    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'subscription.html', context)


class SubscriptionView(SuccessMessageMixin, CreateView):
    template_name = 'subscription_buy.html'
    form_class = SubscriptionViewForm
    success_url = reverse_lazy('subscription')
    success_message = 'Ваша заявка отправленна! С вами свяжуться в ближайшее время.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


def locations(request):
    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'locations.html', context)
