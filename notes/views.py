from django.shortcuts import render, redirect, get_object_or_404
from .models import Box, Note

def home(request):
    boxes = Box.objects.all()
    return render(request, 'notes/home.html', {'boxes': boxes})

def create_box(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        topic = request.POST.get('topic')
        Box.objects.create(name=name, topic=topic)
        return redirect('home')
    return render(request, 'notes/create_box.html')

def view_box(request, box_id):
    box = get_object_or_404(Box, id=box_id)
    notes = Note.objects.filter(box=box)
    return render(request, 'notes/box.html', {'box': box, 'notes': notes})

def edit_box(request, box_id):
    box = get_object_or_404(Box, id=box_id)
    if request.method == 'POST':
        box.name = request.POST.get('name')
        box.topic = request.POST.get('topic')
        box.save()
        return redirect('home')
    return render(request, 'notes/edit_box.html', {'box': box})

def delete_box(request, box_id):
    box = get_object_or_404(Box, id=box_id)
    box.delete()
    return redirect('home')

def create_note(request, box_id):
    box = get_object_or_404(Box, id=box_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Note.objects.create(box=box, title=title, content=content)
        return redirect('view_box', box_id=box_id)
    return render(request, 'notes/create_note.html', {'box': box})

def view_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    return render(request, 'notes/view_note.html', {'note': note})

def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()
        return redirect('view_box', box_id=note.box.id)
    return render(request, 'notes/edit_note.html', {'note': note})

def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    box_id = note.box.id
    note.delete()
    return redirect('view_box', box_id=box_id)
