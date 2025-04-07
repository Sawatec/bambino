from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from dashboard.forms import NewsForm, CommentForm
from .models import News, Vote, Comment
from django.contrib.auth import logout


def showview(request):
    allnews = News.objects.all()
    if request.user.userprofile.is_aproved:
        template = "dashboard.html"
    else:
        logout(request)
        if request.user.is_authenticated:
            print("Logged in")
        else:
            print("Not logged in")
        template = "warning.html"
    context = {'all_the_news': allnews}
    return render(request, template, context)


class NewsCreateView(CreateView):
    model = News
    form_class = NewsForm
    template_name = 'news-create.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def vote(request, pk: str, up_or_down: str):
    that_one_news = News.objects.get(id=int(pk))
    voting_user = request.user
    if not Vote.objects.filter(news=that_one_news):
        print("list is empty")
        that_one_news.vote(voting_user, up_or_down)
    else:
        if Vote.objects.filter(news=that_one_news, user=voting_user).exists():
            vote = Vote.objects.filter(news=that_one_news, user=voting_user)[0]
            if vote.up_or_down != up_or_down:
                print("change " + vote.up_or_down + " to " + up_or_down)
                vote.up_or_down = up_or_down
                vote.save()
            else:
                None
            print("cant like more then one time")
        else:
            that_one_news.vote(voting_user, up_or_down)

    return redirect(request.META.get('HTTP_REFERER'))


def comment_news(request, **kwargs):
    news_id = kwargs['pk']
    news = News.objects.get(id=news_id)

    # Add comment
    if request.method == 'POST':
        form = CommentForm(request.POST)
        form.instance.user = request.user
        form.instance.news = news
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

    comments = Comment.objects.filter(news=news)
    context = {'that_one_news': news,
               'comments_for_that_one_news': comments,
               'upvotes': news.get_upvotes_count(),
               'downvotes': news.get_downvotes_count(),
               'comment_form': CommentForm}
    return render(request, 'news-detail.html', context)