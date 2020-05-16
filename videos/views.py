from django.views.generic.edit import FormView
from django.views.generic import DetailView
from django.core.urlresolvers import reverse


from .models import VideoCategory, Video
from .forms import UploadVideoForm


class HomeView(FormView):
    template_name = 'home.html'
    form_class = UploadVideoForm
    success_url = None

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['categories'] = VideoCategory.objects.all()
        return context

    def form_valid(self, form):
        self.object = form.save()
        slug = self.object.slug
        self.success_url = reverse('video_detail', kwargs={'slug': slug})
        return super(HomeView, self).form_valid(form)


class VideoCategoryDetailView(DetailView):
    model = VideoCategory
    fields = ('title', 'description', 'videos')
    context_object_name = 'category'
    template_name = 'video_category/detail.html'


class VideoDetailView(DetailView):
    model = Video
    fields = ('title', 'description', 'tags', 'categories', 'added_date')
    context_object_name = 'video'
    template_name = 'video/detail.html'
