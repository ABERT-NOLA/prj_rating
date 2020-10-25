from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormMixin
from django.contrib.auth.models import User
import math

# Create your views here.
def index(request):
    title = 'Home'
    all_posts = Post.get_all_posts()
    context = {
        'posts': all_posts,
    }
    return render(request, 'welcome.html', context)


@method_decorator(login_required, name='dispatch')
class PostDetailView(FormMixin, DetailView):
    model = Post
    template_name = 'projects/post_detail.html'
    form_class = RatingForm

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        ratings = Rating.get_all_ratings(self.get_object())
        design = 0
        content = 0
        usability = 0
        for rating in ratings:
            design += rating.design
            content += rating.content
            usability += rating.usability        
        
        try:
            context['design'] = math.ceil(design/len(ratings))
            context['usability'] = math.ceil(usability/len(ratings))
            context['content'] = math.ceil(content/len(ratings))
        except:
            context['design'] = design
            context['usability'] = usability
            context['content'] = content
        
        context['ratings'] = len(ratings)
        context['form'] = RatingForm(initial={'post': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.post = self.get_object()
        form.instance.user = self.request.user        
        form.save()
        
        return super(PostDetailView, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class PostCreateView(CreateView):
    model = Post
    fields = ['title','url','tech_used','desc', 'image_url']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','url','desc', 'image_url']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

@method_decorator(login_required, name='dispatch')
class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

@login_required
def add_comment(request, post_id):
    post = Post.objects.filter(pk=post_id)
    all_posts = Post.get_all_posts()   
    context = {
        'posts': all_posts,
    }
    if request.method == 'POST':
        content = request.POST.get('comment')
        comment_inst = Comment(content=content, post_id=post_id)      
        comment_inst.save()  
        return redirect('welcome')
        
    return render(request, 'index.html', context)
     