# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.conf import settings
from django.template import RequestContext
from django.template import Context
from models import Book
from models import Author
#settings.configure()

def search_form(request):
    '''
    ��ʾ��ѯ����
    '''
    return render_to_response('search_form.html')
    
def search(request):
    '''
    ��ʾ��ѯ���
    '''
   if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        try:   
            AuthorID = Author.objects.get(Name=q)
            books = Book.objects.filter(AuthorID = AuthorID)
            return render_to_response('result.html',
                {'books': books, 'query': q})
        except Author.DoesNotExist:
            return HttpResponse("Unexisted author!Please turn back to submit a correct name!")
   else:
        return HttpResponse("Please submit a search term.")

def show(request):
     '''
    ��ʾ����ͼ����Ϣ
    '''
    if request:
        book_list = Book.objects.all()
        c = Context({"book_list":book_list})
        return render_to_response("table.html",c)

def showauthor(request):
    '''
    ��ʾ�������ߵ���Ϣ
    '''
     if request:
        author_list = Author.objects.all()
        c = Context({"author_list":author_list})
        return render_to_response("showauthor.html",c)


def delete(request):
    '''
    ɾ��ĳ����
    '''
    if request:
        a = request.GET["ISBN"]
        b = Book.objects.get(ISBN=a)
        b.delete()
        book_list = Book.objects.all()
        c = Context({"book_list":book_list})
        return render_to_response("table.html", c)
        
def book_author(request):
    '''
    ��ʾĳ��ͼ�����ϸ��Ϣ
    '''
    if request:
        a = request.GET["ISBN"]
        b = Book.objects.get(ISBN=a)
        authorid = b.AuthorID
        q = Author.objects.get(AuthorID = authorid)
        return render_to_response('book_author.html',
                                  {'book':b,'author':q})
                                  
def begin(request):
    '''
    ��ӭʹ�ý���
    '''
       return render_to_response('welcome.html')
        
        
def bookinsert(request):
    '''
    ͼ�����
    '''
    if request.POST:
        post = request.POST
        new_book = Book(
            ISBN = post["ISBN"],
            Title = post["Title"],
            AuthorID= post["AuthorID"],
            Publisher = post["Publisher"],
            PublishDate = post["PublishDate"],
            Price = post["Price"])
        new_book.save()
    return render_to_response('add.html',context_instance=RequestContext(request))

def bookmodify(request):
    '''
    ͼ����Ϣ�޸�
    '''
     if "ISBN" in request.GET and request.POST:
         post=request.POST
         n=request.GET["ISBN"]
         Book.objects.filter(ISBN=n).update(
            AuthorID = post["AuthorID"],
            Publisher = post["Publisher"],
            PublishDate = post["PublishDate"],
            Price = post["Price"]) 
     return render_to_response('book_modify.html')
     
def authormodify(request):
    '''
    ������Ϣ�޸�
    '''
    if "AuthorID" in request.GET and request.POST:
        post = request.POST
        n = request.GET["AuthorID"]
        Author.objects.filter(AuthorID = n).update(
            Country = post["Country"],
            Age = post["Age"],
            Name = post["Name"])
    return render_to_response('author_modify.html')
    
def authorinsert(request):
    '''
    ��������
    '''
    if request.POST:
        post = request.POST
        new_author = Author(
            AuthorID= post["AuthorID"],
            Name = post["Name"],
            Country = post["Country"],
            Age = post["Age"])
        new_author.save()
    return render_to_response('add_author.html',context_instance=RequestContext(request))

def add_ask(request):
    '''
    �����ĳ����֮ǰ����ѯ�������Ƿ�û�г��������ݿ��й�
    '''
    if request:
        return render_to_response('ask.html',context_instance=RequestContext(request))
