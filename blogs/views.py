from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Case, When, BooleanField
from django.http import HttpResponseForbidden, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from blogs.models import Blog, Subscribe, Post


class IndexView(View):
    template = 'blogs/index.html'

    def get(self, request):
        return render(request, self.template)


class BlogsListView(ListView):
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
    success_url = reverse_lazy('blogs:blog')
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


class PostCreateView(CreateView):
    model = Post
    template_name = 'blogs/post_form.html'
    fields = ['name', 'content']

    def dispatch(self, request, *args, **kwargs):
        self.blog = get_object_or_404(Blog, id=kwargs.get('pk'))
        return super(PostCreateView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('blogs:blog', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.blog = self.blog
        return super(PostCreateView, self).form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blogs/post_form.html'
    fields = ['name', 'content']

    def get_success_url(self):
        print(self.kwargs)
        return reverse('blogs:blog', kwargs={'pk': self.kwargs['pk'], })


class PostsListView(ListView):
    model = Post
    template_name = 'blogs/post_list.html'
    paginate_by = 5

    def get_queryset(self):
        return self.model.objects.select_related('blog').filter(blog=self.blog)

    def dispatch(self, request, *args, **kwargs):
        self.blog = get_object_or_404(Blog, id=kwargs.get('pk'))
        return super(PostsListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context_data = super(PostsListView, self).get_context_data(**kwargs)
        context_data['blog'] = self.blog
        return context_data
