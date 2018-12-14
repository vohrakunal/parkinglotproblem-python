from django.shortcuts import render
from django.http import HttpResponse
from car.models import car,parking
from car.forms import NewCarForm, RemoveCarForm, SearchCarForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import logout
# Create your views here.

# def logout_view(request):
#     logout(request)

def index(request):
    # car_val = car.objects.order_by('-id')[:5]
    # car_val_in = car.objects.filter(status = 'in')
    parking_val = parking.objects.order_by('level')

    final_val = { 'parkval': parking_val,}
    return render(request, 'car/index.html', context= final_val)

    # return render(request, 'car/index.html', {'delform':delform})

def parkingfunc(request):
    error_msg = 0
    msg = 0
    delform = RemoveCarForm()
    car_val_in = car.objects.filter(status = 'in')
    if request.method == "POST":
        delform = RemoveCarForm(request.POST)
        if delform.is_valid():
            slot_val = 0
            level_val = 0
            formregno = delform.cleaned_data['regno']
            reg_car = car.objects.filter(regno = formregno, status = 'in')
            for regcar in reg_car:
                slot_val = regcar.slot
                level_val = regcar.level
            park_slot_query = parking.objects.filter(level = level_val)
            if slot_val == 1 :
                msg = 101
                park_slot_query.update(slot1 = 0)
            elif slot_val == 2:
                msg = 101
                park_slot_query.update(slot2 = 0)
            elif slot_val == 3:
                msg = 101
                park_slot_query.update(slot3 = 0)
            elif slot_val == 4:
                msg = 101
                park_slot_query.update(slot4 = 0)
            elif slot_val == 5:
                msg = 101
                park_slot_query.update(slot5 = 0)
            elif slot_val == 6:
                msg = 101
                park_slot_query.update(slot6 = 0)
            elif slot_val == 7:
                msg = 101
                park_slot_query.update(slot7 = 0)
            elif slot_val == 8:
                msg = 101
                park_slot_query.update(slot8 = 0)
            elif slot_val == 9:
                msg = 101
                park_slot_query.update(slot9 = 0)
            elif slot_val == 10:
                msg = 101
                park_slot_query.update(slot10 = 0)

            if msg == 101:
                reg_car.update(slot=999, level=999, status = 'out')
            else:
                error_msg = 101
            # return index(request)



    form = NewCarForm()
    park_val = parking.objects.order_by('level')
    if request.method == "POST":
        form = NewCarForm(request.POST)
        if form.is_valid():
            formregno = form.cleaned_data['regno']

            level = 1
            for park in park_val:
                parkslot = parking.objects.filter(level=level)
                if park.slot1 == 0:
                    form.save(commit=True)
                    parkslot.update(slot1 = 1)
                    car.objects.filter(regno=formregno).update(slot= 1, level=level)
                    msg = 100
                    break
                elif park.slot2 == 0:
                    form.save(commit=True)
                    parkslot.update(slot2 = 1)
                    car.objects.filter(regno=formregno).update(slot=2, level=level)
                    msg = 100
                    break
                elif park.slot3 == 0:
                    form.save(commit=True)
                    parkslot.update(slot3 = 1)
                    car.objects.filter(regno=formregno).update(slot = 3, level=level)
                    msg = 100
                    break
                elif park.slot4 == 0:
                    form.save(commit=True)
                    parkslot.update(slot4 = 1)
                    car.objects.filter(regno=formregno).update(slot = 4, level=level)
                    msg = 100
                    break
                elif park.slot5 == 0:
                    form.save(commit=True)
                    parkslot.update(slot5 = 1)
                    car.objects.filter(regno=formregno).update(slot = 5, level=level)
                    msg = 100
                    break
                elif park.slot6 == 0:
                    form.save(commit=True)
                    parkslot.update(slot6 = 1)
                    car.objects.filter(regno=formregno).update(slot = 6, level=level)
                    msg = 100
                    break
                elif park.slot7 == 0:
                    form.save(commit=True)
                    parkslot.update(slot7 = 1)
                    car.objects.filter(regno=formregno).update(slot = 7, level=level)
                    msg = 100
                    break
                elif park.slot8 == 0:
                    form.save(commit=True)
                    parkslot.update(slot8 = 1)
                    car.objects.filter(regno=formregno).update(slot = 8, level=level)
                    msg = 100
                    break
                elif park.slot9 == 0:
                    form.save(commit=True)
                    parkslot.update(slot9 = 1)
                    car.objects.filter(regno=formregno).update(slot = 9, level=level)
                    msg = 100
                    break
                elif park.slot10 == 0:
                    form.save(commit=True)
                    parkslot.update(slot10 = 1)
                    car.objects.filter(regno=formregno).update(slot =10, level=level)
                    msg = 100
                    break
                else:
                    level = level+1

            if msg != 100:
                error_msg = 100
            # return index(request)

    return render(request,'car/parking.html', {'form':form, 'delform':delform, 'carvalin':car_val_in, 'errormsg' : error_msg , 'msg' : msg})

@login_required
def searchfunc(request):
    final_val = {}
    searchform = SearchCarForm()
    if request.method == "GET":
        searchform = SearchCarForm(request.GET)
        if searchform.is_valid():
            search_val = searchform.cleaned_data['searchfield']

            color_search = car.objects.filter(color=search_val).order_by('-id')
            reg_no_search = car.objects.filter(regno=search_val).order_by('-id')
            for reg in reg_no_search:
                print (reg.color)
            final_val = { 'searchform':searchform,'reg_no_search':reg_no_search , 'color_search': color_search}
            print("final val")
            print (final_val)
    return render(request, 'car/search.html', context= final_val)
