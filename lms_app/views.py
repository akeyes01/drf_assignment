from django.shortcuts import render,redirect,get_object_or_404
from lms_app.models import Author, book, loan, member
from lms_app.forms import AuthorForm
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from .models import Author
from .serializers import AuthorSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from .permissions import IsOwnerOrReadOnly

# Create your views here.
@login_required
def authordata(request):
    authors = Author.objects.all()
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
    authors = Author.objects.all()
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
        form = AuthorForm(request.POST,instance=Author)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'lms_app/update.html',{'form':form})


class AuthorCustomPagination(PageNumberPagination):
    page_size = 2

class AuthorFilter(filters.FilterSet):
    author = filters.CharFilter(field_name='author', lookup_expr='icontains')
    id = filters.CharFilter(field_name='id', lookup_expr='exact')

    class Meta:
        model = Author
        fields = ['id', 'author']

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()  
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = AuthorFilter
    pagination_class = AuthorCustomPagination
    ordering_fields = ['id', 'author']
    # Permission class to be added
    permission_classes = [IsOwnerOrReadOnly]
    #permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Ensure that the owner is set to the current user
        #serializer.save(owner=self.request.user)
        serializer.save(owner=self.request.user)

    