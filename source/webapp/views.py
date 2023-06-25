from django.views.generic import ListView, CreateView
from webapp.models import CardGreeting


class CardListView(ListView):
    model = CardGreeting
    template_name = 'index.html'
    context_object_name = 'cards'

class CardCreateView(CreateView):
    model = CardGreeting
    template_name = 'create_card.html'
    fields = ['name', 'city', 'username']
    success_url = '/'

    def form_valid(self, form):
        response = super().form_valid(form)
        return response
