# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 10:57:12 2015

@author: Administrator
"""

from django.contrib import admin
from book.books.models import Book,Author

admin.site.register(Book)
admin.site.register(Author)