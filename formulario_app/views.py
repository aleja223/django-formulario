from django.shortcuts import render


from formulario_app.forms import InputForm

def form_view(request):
    submitted_data = None
    success_message = None

    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            submitted_data = form.cleaned_data
            success_message = "ok ¡Formulario enviado con exito!"
            form = InputForm()

    else:
        form = InputForm()

    context= {
        "form":form,
        "submitted_data": submitted_data,
        "success_message": success_message,
        }
    return render(request, "home.html", context)
