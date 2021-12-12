from django.forms import ModelForm
from .models import Ticket, Review

class CreateTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']

class CreateReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']        

class ResponseReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body', 'ticket']         