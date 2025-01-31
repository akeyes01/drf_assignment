from django.shortcuts import render,redirect,get_object_or_404
from lms_app.models import author, book, loan, member
from lms_app.forms import AuthorForm

# Create your views here.
def authordata(request):
    authors = author.objects.all()
    authorDict = {'authors':authors}
    return render(request, 'lms_app/authors.html', authorDict)

def bookdata(request):
    books = book.objects.all()
    bookDict = {'books':books}
    return render(request, 'lms_app/books.html', bookDict)

def loandata(request):
    loans = loan.objects.all()
    loanDict = {'loans':loans}
    return render(request, 'lms_app/loans.html', loanDict)

def memberdata(request):
    members = member.objects.all()
    memberDict = {'members':members}
    return render(request, 'lms_app/members.html', memberDict)

def getAuthors(request):
    authors = author.objects.all()
    return render(request, 'lms_app/index.html',{'authors': authors})

def createAuthor(request):
    form = AuthorForm()
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'lms_app/create.html',{'form': form})

def deleteAuthor(request, id):
    Author = author.objects.get(id=id)
    Author.delete()
    return redirect('/')

def updateAuthor(request,id):
    Author = author.objects.get(id=id)
    form = AuthorForm(instance=Author)
    if request.method == 'POST':
        #form = AuthorForm(request.POST,instance=author)
        form = AuthorForm(request.POST,instance=Author)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'lms_app/update.html',{'form':form})

'''
def updateAuthor(request,id):
    Author = author.objects.get(id=id)
    #Author = AuthorForm(instance=author)
    if request.method == 'POST':
        #form = AuthorForm(request.POST,instance=author)
        form = AuthorForm(request.POST,instance=Author)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'lms_app/update.html',{'author':Author})
'''