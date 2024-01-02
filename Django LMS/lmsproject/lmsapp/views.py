from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .models import Book, BookIssue
from .forms import BookIssueForm


# Create your views here.

def HelloLMS(request):
    books=Book.objects.all()
    return render(request, "view_book.html", {"books":books})


def AddbookView(request):
    return render(request, "add_book.html")

def Adddata(request):
    if request.method=="POST":
        t = request.POST["title"]
        c = request.POST["category"]
        print(t, c)
        book=Book()
        book.title=t
        book.cateogry=c
        book.save()
        return HttpResponseRedirect("/")
    

def Editbook(request):
    if request.method=="POST":
        t = request.POST["title"]
        c = request.POST["category"]
        
        book=Book.objects.get(id=request.POST['bid'])
        book.title=t
        book.cateogry=c
        book.save()
        return HttpResponseRedirect("/")



def EditbookView(request):
    book=Book.objects.get(id=request.GET['bookid'])
    
    return render(request,"edit_book.html", {"book":book})

def DeletebookView(request):
    book=Book.objects.get(id=request.GET['bookid'])
    book.delete()
    return HttpResponseRedirect("/")





def issue_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'GET':
        user = form.cleaned_data['user']
        book_issue = BookIssue.objects.create(book=book, user=user)
        return redirect('/', book_id=book_id) 
    else:
        form = BookIssueForm()
    return render(request, 'issue_book.html', {'form': form, 'book': book})




