# from django.shortcuts import render, get_object_or_404
# from .models import Album, Song

# # index view for albums
# def index(request):
#     get_all_albums = Album.objects.all()
#     context = {'get_all_albums': get_all_albums}
#     return render(request, 'music/index.html', context)

# # Detail view for a single album
# def detail_view(request, album_id):
#     # instead of using the try catch syntax album = Album.objects.get(pk=album_id)
#     album = get_object_or_404(Album, pk=album_id)
#     return render(request, 'music/details.html', {'album': album})

# def favorite_view(request, album_id):
#     album = get_oreversebject_or_404(Album, pk=album_id)
#     try:
#         selected_song = album.song_set.get(pk=request.POST['song'])
#     except(KeyError, Song.DoesNotExist):
#         return render(request, 'music/details.html', {
#             'album': album,
#             'error_message': "You did not select a valid song"
#         })
#     else:
#         selected_song.is_favorite = True
#         selected_song.save()
#         return render(request, 'music/details.html', {'album': album})


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
# from music.profiler import profile
from django.views.generic import View
from .models import Album
from .forms import UserForm

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'album_list'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/details.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']
    template_name = 'music/create_album.html'

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']
    template_name = 'music/create_album.html'

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'music/register.html'
    # Process form data
    def post(self, request):
        form = UserForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            # Cleaned / Normalized Data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            # returns User object if credentials supplied are correct
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    albums = Album.objects.filter(user=request.user)
                    return render(request, 'music/index.html', {'albums': albums})
            context = {
                "form": form,
            }
        return render(request, self.template_name, context)
