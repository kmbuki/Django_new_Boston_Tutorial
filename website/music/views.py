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
#     album = get_object_or_404(Album, pk=album_id)
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


from django.views import generic
from .models import Album
from music.profiler import profile
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'album_list'

    @profile
    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/details.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']
