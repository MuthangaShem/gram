from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import ProfileForm, profileEdit, ImageUpload
from django.contrib import messages
from .models import Image, Profile

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    posts = Image.objects.all()
    return render(request,'index.html',{'posts':posts})

@login_required(login_url='/accounts/login/')
def profile(request, user_id):
    posts = Image.objects.all()
    return render(request, 'profile.html', {'posts': posts})


@transaction.atomic
def profile_edit(request, user_id):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile', user_id)
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'edit-profile.html', {"profile_form": profile_form})

@login_required(login_url='/accounts/login/')
def post(request): 
    current_user = request.user
    if request.method == 'POST':
        form = ImageUpload(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = current_user
            photo.save()
            return redirect('index')
    else:
        form = ImageUpload()
    return render(request, 'post.html', {"form": form})


@login_required(login_url='/accounts/login')
def addComment(request,id):

    profile= request.user.profile

    form = CommentForm(request.POST)
    current_user = request.user
    if form.is_valid():
        try:
            current_user = request.user
            current_post = Image.objects.get(id=id)
            new_comment = request.POST['comment_content']
            profile = form.save(commit=False)
            profile.user = current_user
            profile.post = current_post
            profile.save()

        except ObjectDoesNotExist:
            raise Http404('Comment not found.')

        return HttpResponseRedirect(request.META['HTTP_REFERER'])

    if request.META['HTTP_REFERER']:
        return HttpResponseRedirect(request.META['HTTP_REFERER'], {"form": form, "current_user":current_user})

def deletePost(request,id):
    post = Image.objects.get(id=id).delete()
    current_user = request.user

    if request.META['HTTP_REFERER']:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

def deleteComment(request,id):
    post = Comment.objects.get(id=id).delete()
    current_user = request.user

    if request.META['HTTP_REFERER']:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


def search_results(request):
    search_term = request.GET.get('profile')
    results = Profile.get_Image_by_profile(search_term)
    print(results)
    return render(request, 'search.html', {"results":results})

# @csrf_exempt
# def search_image(request):

#     if request.method == "POST" and request.is_ajax():
#         term = request.POST['item']
#         result = Profile.objects.filter(profile_owner__username__icontains=term).all()
#         # for r in result:
#         #     # for a in r.image_set.all():
#         #     print(r.profile_owner)

#         return render_to_response('result.html', {'search_result': result})

#     return redirect(index)