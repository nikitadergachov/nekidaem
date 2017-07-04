from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Case, When, BooleanField
from django.http import HttpResponseForbidden, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView
from blogs.models import Blog, Subscribe


class IndexView(View):
    template = 'blogs/index.html'

    def get(self, request):
        return render(request, self.template)


class BlogListView(ListView):
    model = Blog
    paginate_by = 5

    def get_queryset(self):
        if self.request.user.is_authenticated:

            blogs_ids = Subscribe.objects.filter(
                user=self.request.user
            ).values_list('blog', flat=True)

            queryset = self.model.objects.annotate(
                has_subscribed=Case(
                    When(pk__in=blogs_ids, then=True),
                    default=False,
                    output_field=BooleanField(),
                ),
            )
        else:
            queryset = self.model.objects.all()

        return queryset


class SubscribeView(CreateView):
    model = Subscribe
    fields = ['blog', 'user']
    success_url = reverse_lazy('blogs:blogs')
    template_name = 'blogs/blog_list.html'

    def dispatch(self, request, *args, **kwargs):
        self.blog = get_object_or_404(Blog, id=kwargs.get('pk'))
        return super(SubscribeView, self).dispatch(request, *args, **kwargs)


    def get_form_kwargs(self):
        kwargs = super(SubscribeView, self).get_form_kwargs()
        if self.request.method == 'POST':
            data = dict(kwargs['data'])
            data.update({
                'blog': self.blog.pk,
                'user': self.request.user.pk,
            })
            kwargs['data'] = data
        return kwargs

class UnSubscribeView(DeleteView):
    model = Subscribe
    success_url = reverse_lazy('blogs:blogs')
    template_name = 'blogs/blog_list.html'


    def dispatch(self, request, *args, **kwargs):
        self.blog = get_object_or_404(Blog, id=kwargs.get('pk'))
        return super(UnSubscribeView, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        qs = super(UnSubscribeView, self).get_queryset()
        obj = qs.filter(
            user=self.request.user,
            blog=self.blog
        ).first()
        if obj is None:
            raise Http404('Блог не найден')
        return obj

