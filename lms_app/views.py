from django.shortcuts import render,redirect,get_object_or_404
from lms_app.models import author, book, loan, member
from lms_app.forms import AuthorForm
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import author
from .serializers import AuthorSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@login_required
def authordata(request):
    authors = author.objects.all()
    authorDict = {'authors':authors}
    return render(request, 'lms_app/authors.html', authorDict)

@login_required
def bookdata(request):
    books = book.objects.all()
    bookDict = {'books':books}
    return render(request, 'lms_app/books.html', bookDict)

@login_required
def loandata(request):
    loans = loan.objects.all()
    loanDict = {'loans':loans}
    return render(request, 'lms_app/loans.html', loanDict)

@login_required
def memberdata(request):
    members = member.objects.all()
    memberDict = {'members':members}
    return render(request, 'lms_app/members.html', memberDict)

@login_required
def getAuthors(request):
    authors = author.objects.all()
    return render(request, 'lms_app/index.html',{'authors': authors})

@login_required
def createAuthor(request):
    form = AuthorForm()
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'lms_app/create.html',{'form': form})

@login_required
@permission_required('lms_app.delete_author', raise_exception=True)
def deleteAuthor(request, id):
    Author = author.objects.get(id=id)
    Author.delete()
    return redirect('/')

@login_required
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

class AuthorList(APIView):
    def get(self, request):
        Authors = author.objects.all()
        serializer = AuthorSerializer(Authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = author.objects.all()  
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]
    