from rest_framework.generics import ListAPIView
from api_v1.serializers import CardSerializer
from webapp.models import CardGreeting

class CardListAPIView(ListAPIView):
    serializer_class = CardSerializer

    def get_queryset(self):
        return CardGreeting.objects.all()
