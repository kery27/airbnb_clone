from django.utils import timezone
from django.views.generic import ListView
from . import models

"""
# Create your views here.
# def all_rooms(request):
    # print(vars(request))
    # 안에 많은 정보가 있다 httpsrequest 에 대한 응답을 우리는 반환해야된다
    # 뷰에서반환할건 리스폰스다

    # 페이지의 정보를 가져온다
    # 페이지 정보를 페이지 사이즈만큼 곱해서 최대 리밋을 구하고 -10한 만큼의 룸정보를
    # 들고온다. 범위를 제한한는 쿼리는 동시에 발생한다. 가져와서 필터링 하는게 아님.
    # Built-in template tags and filters를 참고해서 만든다
    
    page = request.GET.get("page", 1)
    page = int(page or 1)
    page_size = 10
    limit = page_size * page
    offset = limit - page_size

    all_rooms = models.Room.objects.all()[offset:limit]
    page_count = ceil(models.Room.objects.count() / page_size)
    return render(
        request,
        "rooms/home.html",
        context={
            "potato": all_rooms,
            "page": page,
            "page_count": page_count,
            "page_range": range(1, page_count),
        },
    )
    """
"""
    # 장고 api를 써서
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)

    try:
        rooms = paginator.page(int(page))
        return render(request, "rooms/home.html", {"rooms": rooms})
    except EmptyPage:
        return redirect("/")
    # print(vars(rooms))
"""


class HomeView(ListView):
    model = models.Room
    paginate_by = 10
    paginate_orphans = 4
    ordering = "update"
    # page_kwarg = "potato"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context
