from django.shortcuts import render, redirect, HttpResponse
from .models import wishes
from apps.login_register.models import User
from django.contrib import messages
import datetime


def show_wishes(request):
    all_wishes = wishes.objects.all()
    user_wishes = wishes.objects.all().filter(wisher = request.session['user_id'] )
    wishes_granted = all_wishes.exclude(granted_at = None)
    not_granted = user_wishes.filter(granted_at = None)

    context = { 'wishes': not_granted,
                'granted' : wishes_granted,
    }



    return render(request, 'wishes/wishes.html', context)

def show_make_wish(request):

    return render(request, 'wishes/new_wish.html')

def create_wish(request):
    errors = wishes.objects.wish_validator(request.POST)
    print(errors)
    if errors != None:
        for tag, message in errors.items():
            messages.error(request, message)
        return redirect('/wishes/new')

    if errors == None:
        wishes.objects.create(item = request.POST['wish_item'], description = request.POST['wish_description'], wisher = User.objects.get(id = request.session['user_id']) )
        return redirect('/wishes')


def delete_wish(request, id):
    wish_id = int(id)

    wish = wishes.objects.get(id = wish_id)
    wish.delete()

    return redirect('/wishes')

def show_edit_wish(request, id):
    wish_id = int(id)

    wish = wishes.objects.get(id = wish_id)
    item = wish.item
    description = wish.description

    context= {
        'id': wish_id,
        'item': item,
        'description':description
    }
    return render(request, 'wishes/edit_wish.html', context)

def update_wish(request):
    wish_id = request.POST['wish_id']
    errors = wishes.objects.update_validator(request.POST)

    if errors != None:
        for tag, message in errors.items():
            messages.error(request, message)
        return redirect(f'/wishes/edit/{wish_id}')

    if errors == None:
        wish = wishes.objects.get(id = wish_id)
        wish.item = request.POST['update_item']
        wish.description = request.POST['update_description']

        wish.save()

    return redirect('/wishes')

def grant_wish(request, id):
    wish_granted = wishes.objects.get(id = int(id))
    wish_granted.granted_at = wish_granted.updated_at
    wish_granted.save()
    

    return redirect("/wishes")

def like_wish(request, id):
    wish_id = id
    wish = wishes.objects.get(id = wish_id)
    user = User.objects.get(id = request.session['user_id'])
    wish.likes.add(user)
    return redirect("/wishes")

def wish_stats(request):
    all_granted = wishes.objects.exclude(granted_at = None)
    user_wishes = wishes.objects.filter(wisher = request.session['user_id'])
    user_granted = user_wishes.exclude(granted_at = None)
    not_granted = user_wishes.filter(granted_at = None)

    context = {
        'all_granted_wishes': all_granted,
        'user_granted_wishes': user_granted, 
        'not_granted': not_granted,
    }



    return render(request, 'wishes/wishes_stats.html', context)

def logout(request):
    request.session.clear()

    return redirect('/')







