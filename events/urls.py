from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from events.models import Event
from events.views import logout

urlpatterns = patterns(
    '',
    url(r'^events/$',
        ListView.as_view(
            queryset=Event.objects.order_by('-start_time')[:50],
            context_object_name='latest_events_list',
            template_name='events.html'),
        name='events'),
    url(r'^events/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Event,
            template_name='details.html'),
        name='detail'),
    url(r'^logout$', logout, name='logout'),
)
