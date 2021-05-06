from django.shortcuts import render, redirect
from .models import Dojo, Ninja

# Create your views here.
def index(request): 
    # for ninja in Ninja.objects.all():
    #     ninja.dojo_id.amount_of_ninjas = ninja.dojo_id.amount_of_ninjas + 1
    #     ninja.dojo_id.save()

    # three lines above launch only once to populate already created ninjas in the new field amount_of_ninjas
    context = {
		'all_the_dojos': Dojo.objects.all(),
		'all_the_ninjas': Ninja.objects.all(),
	}
    return render(request, "index.html", context)

def add_new_dojo(request):
    if request.method == "POST":
        name = request.POST["dojo_name"]
        city = request.POST["dojo_city"]
        state = request.POST["dojo_state"]
        new_dojo = Dojo.objects.create(name = name, city = city, state = state)
        new_dojo.save()
        return redirect('/')

def add_new_ninja(request):
    if request.method == "POST":
        first_name = request.POST["ninja_fname"]
        last_name = request.POST["ninja_lname"]
        dojo_id = request.POST["dojos_list"]
        dojo = Dojo.objects.all().get(id = dojo_id)
        new_ninja = Ninja.objects.create(first_name = first_name, last_name = last_name, dojo_id = dojo)
        new_ninja.save()
        dojo.amount_of_ninjas = dojo.amount_of_ninjas + 1
        dojo.save()
        return redirect('/')

def delete_dojo_and_all_its_ninjas(request, number):
    dojo_to_delete = Dojo.objects.get(id = number)
    dojo_to_delete.delete()
    # Dojo.objects.delete_dojo(number)  #don't know how it works
    return redirect('/')