from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django.shortcuts import redirect

def contactList(request):
    contacts = Contact.objects.all()
    return render(request, 'contactList.html', {'contacts':contacts})  # renderujemy
                    # jeśli teraz uruchomimy serwer, to dostaniemu bląd, że nie mamy szablonu
                    # te nawiasy {}

def contactNew(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if (form.is_valid()):
            post = form.save(commit=False)      # zapisz, ale nic więcej nie rób
            post.save()
            return redirect('contactList')
    else:
        form = ContactForm()

    return render(request, 'contactNew.html', {'form':form})


# Create your views here.
