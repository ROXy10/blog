from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import CommetnForm
from .models import Comment


def comment_thread(request, id):
    obj = get_object_or_404(Comment, id=id)
    content_object = obj.content_object
    content_id = obj.content_object.id
    initial_data = {
        "content_type": obj.content_object,
        "object_id": obj.object_id,
    }

    form = CommetnForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        c_type = form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        object_id = form.cleaned_data.get("object_id")
        content_data = form.cleaned_data.get("content")
        parent_obj = None
        try:
            parent_id = int(request.POST.get('parent_id'))
        except:
            parent_id = None
        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists() and parent_qs.count() == 1:
                parent_obj = parent_qs.first()

        new_coment, created = Comment.objects.get_or_create(
            user=request.user,
            content_type=content_type,
            object_id=object_id,
            content=content_data,
            parent=parent_obj
        )
        return HttpResponseRedirect(new_coment.content_object.get_absolute_url())
    context = {
        "comment": obj,
        "from": form,
    }
    return render(request, "comment_thread.html", context)