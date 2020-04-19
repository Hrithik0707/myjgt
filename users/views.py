from django.shortcuts import render
from .forms import Detail_form
from .models import Form
# Create your views here.
def create_form(request):
    form = Detail_form()
    if request.method == 'POST':
        form = Detail_form(request.POST, request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.Todays_documents = request.FILES['Todays_documents']
            user_pr.save()
            return render(request, 'users/details.html', {'user_pr': user_pr})
    context = {"form": form,}
    return render(request, 'users/create.html', context)