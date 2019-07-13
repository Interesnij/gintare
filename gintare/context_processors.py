from .forms import FeedbackForm

def form1(request):
    return {'form1': FeedbackForm}
