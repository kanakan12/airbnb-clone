# from math import ceil
# from django.shortcuts import render, redirect
# from django.core.paginator import Paginator, EmptyPage
# from django.utils import timezone
from django.views.generic import ListView, DetailView
# from django.http import Http404
# from django.shortcuts import render
from . import models
# Create your views here.

class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"

class RoomDetail(DetailView):

    """ RoomDetail Definition """

    model = models.Room

# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, "rooms/detail.html", {"room":room})
#     except models.Room.DoesNotExist:
#         raise Http404()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     now = timezone.now()
    #     context["now"] = now
    #     return context

# def all_rooms(request):
#     page = request.GET.get("page", 1)
#     room_list = models.Room.objects.all()
#     paginator = Paginator(room_list, 10, orphans=5)

#     try:
#         rooms = paginator.page(int(page))
#         return render(request, "rooms/home.html", {"rooms": rooms})
#     except EmptyPage:
#         return redirect("/")
