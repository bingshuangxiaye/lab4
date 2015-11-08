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
    显示查询界面
    '''
    return render_to_response('search_form.html')
    
def search(request):
    '''
    显示查询结果
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
    显示所有图书信息
    '''
    if request:
        book_list = Book.objects.all()
        c = Context({"book_list":book_list})
        return render_to_response("table.html",c)

def showauthor(request):
    '''
    显示所有作者的信息
    '''
     if request:
        author_list = Author.objects.all()
        c = Context({"author_list":author_list})
        return render_to_response("showauthor.html",c)


def delete(request):
    '''
    删除某本书
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
    显示某本图书的详细信息
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
    欢迎使用界面
    '''
       return render_to_response('welcome.html')
        
        
def bookinsert(request):
    '''
    图书添加
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
    图书信息修改
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
    作者信息修改
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
    新增作者
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
    在添加某本书之前用于询问作者是否没有出现在数据库中过
    '''
    if request:
        return render_to_response('ask.html',context_instance=RequestContext(request))
