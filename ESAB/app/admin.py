from . import admin,db,login_manager
from flask_admin.base import BaseView,expose
from flask_admin.contrib.sqla import ModelView
from .models import *
from flask import redirect,url_for,request
from flask_login import current_user
from flask_admin import AdminIndexView
from flask_admin.menu import MenuLink
from sqlalchemy import func, join, Integer, String, Boolean, Date
from sqlalchemy.orm import aliased
from datetime import datetime
from .late import *

class LogoutMenuLink(MenuLink):
    def is_accessible(self):
        return current_user.is_authenticated 


class LoginMenuLink(MenuLink):
    def is_accessible(self):
        return not current_user.is_authenticated

class AdminView(ModelView):
    can_export = True
    def is_accessible(self):
        return current_user.is_authenticated

        
    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('login', next=request.url))
        
class TransactionView(ModelView):
    can_export = True
    # can_edit =False
    def is_accessible(self):
        return current_user.is_authenticated

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('login', next=request.url))
    
    column_list=['id','user_id','book_id','issue_date','due_date','return_date','returned']

class UserView(ModelView):
    can_export = True

    def is_accessible(self):
        return current_user.is_authenticated

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('login', next=request.url))
    
    column_list = ['id', 'first_name', 'last_name', 'qr', 'phone_number', 'active']
    column_searchable_list = ['id', 'first_name', 'last_name']


class BookView(ModelView):
    can_export = True
    # can_edit =False
    def is_accessible(self):
        return current_user.is_authenticated

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('login', next=request.url))
    
    column_list=['id','title','author','qr','issue']
    column_searchable_list = ['id', 'title', 'author']

class AvailBooks(ModelView):
    can_export = True
    can_edit = False
    can_create = False
    can_delete = False
    def is_accessible(self):
        return current_user.is_authenticated

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('login', next=request.url))
    def get_query(self):
        return self.session.query(self.model).filter(
          Books.issue==False)
    column_list=['id','title','author','qr','issue']
    column_searchable_list = ['id', 'title', 'author']
     

class LateView(ModelView):
    can_export = True
    can_edit = False
    can_create = False
    can_delete = False
    column_list=['id','user_id','book_id','issue_date','due_date','return_date','returned']
    def is_accessible(self):
        return current_user.is_authenticated

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('login', next=request.url))
        
    def get_query(self):
        

        query= self.session.query(self.model).filter(
          Transaction.due_date<=datetime.today()
        ).filter(
            Transaction.return_date==None
        ).filter(
            Transaction.returned==False
        )
        return query
    

    def get_count_query(self):
      return self.session.query(func.count('*')).filter(
          Transaction.due_date<=datetime.today()
        ).filter(
            Transaction.return_date==None
        ).filter(
            Transaction.returned==False)
    




admin.add_view(UserView(User, db.session))
admin.add_view(BookView(Books, db.session))
admin.add_view(AvailBooks(Books,db.session,endpoint='Available Books',name='Available Books'))
admin.add_view(TransactionView(Transaction, db.session))
admin.add_view(LateView(Transaction, db.session,endpoint='late',name='Late'))

admin.add_link(LoginMenuLink(name='Login', category='', url="/login"))
admin.add_link(LogoutMenuLink(name='Logout', category='', url="/logout"))

