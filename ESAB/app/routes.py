from flask import render_template,redirect,url_for,request,abort
from . import app
from .form import * 
from .models import *
from datetime import date, timedelta
from flask_login import login_user,logout_user,login_required,current_user



@app.route('/',methods=["POST","GET"])
def login():
    form = Login()
    if form.validate_on_submit():
        username = form.data.get('username')
        password = form.data.get('password')
        admin_user = AdminUser.query.filter_by(username=username).first()

        if admin_user and admin_user.check_password(password):
            login_user(admin_user)
            return redirect('/admin')
        else:
            return "Invalid username or password"

    return render_template('index.html', form=form)


@app.route('/logout',methods=['POST','GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))




@app.route('/user_qrscan_borrow', methods=["POST","GET"])
def user_qrscan_borrow():
    form=UserQrScan()
    if form.validate_on_submit():
        user = User.query.filter_by(
            qr=form.data.get('qr')
        ).first()
        if user is None:
            return "Invalid QR"
        
        return redirect(url_for('book_qrscan_borrow',userid=user.id))
    return render_template('user_qr_borrow.html',form=form)


@app.route('/book_qrscan_borrow', methods=["POST","GET"])
def book_qrscan_borrow():
    form=BookQrScan()
    message=''
    user_id = request.args.get('userid')
    transaction_id = None
    if user_id is None:
        message= 'No User ID Present'
        transaction_id=None
        return redirect(url_for('borrow_landing',message=message,transaction_id=transaction_id))
    
    if form.validate_on_submit():
        book_qr = form.data.get("qr")

        user = User.query.filter_by(
            id = user_id
        ).first()

        book = Books.query.filter_by(
            qr = book_qr
        ).first()

        if user is None or book is None:
            message= 'Error'
            transaction_id=None
            return redirect(url_for('borrow_landing',message=message,transaction_id=transaction_id))
        
        if book.issue:
            message = 'Book Already Issued'
            transaction_id=None
            return redirect(url_for('borrow_landing',message=message,transaction_id=transaction_id))
        
        trans = Transaction()
        trans.user_id = user.id
        trans.book_id = book.id
        book.issue=True

        db.session.add(trans)
        db.session.commit()

        message="Issued"
        transaction_id=trans.id
        return redirect(url_for('borrow_landing',message=message,transaction_id=transaction_id))
    
    return render_template('book_qr_borrow.html',form=form,userid=user_id,message=message,transaction_id=transaction_id)

@app.route('/borrow_landing',methods=["POST","GET"])
def borrow_landing():
    message = request.args.get('message')
    transaction_id = request.args.get('transaction_id')
    return render_template('borrow_landing.html',message=message,transaction_id=transaction_id)


# <----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->


@app.route('/user_qrscan_return', methods=["POST","GET"])
def user_qrscan_return():
    form=UserQrScan()
    if form.validate_on_submit():
        user = User.query.filter_by(
            qr=form.data.get('qr')
        ).first()
        if user is None:
            return "Invalid QR"
        
        return redirect(url_for('book_qrscan_return',userid=user.id))
    return render_template('user_qr_return.html',form=form)


@app.route('/book_qrscan_return', methods=["POST","GET"])
def book_qrscan_return():
    form=BookQrScan()
    message=''
    user_id = request.args.get('userid')
    if user_id is None:
        message="No User ID Present"
        return redirect(url_for("return_landing",message=message))  
    
    if form.validate_on_submit():
        book_qr = form.data.get("qr")

        user = User.query.filter_by(
            id = user_id
        ).first()

        book = Books.query.filter_by(
            qr = book_qr
        ).first()

        if user is None or book is None:
            message = "Error User or Book not found"
            return redirect(url_for("return_landing",message=message))  
        
        if not book.issue:
            message="Book Already Returned"
            return redirect(url_for("return_landing",message=message))  
        
        trans=Transaction.query.filter_by(user_id=user.id,book_id=book.id,return_date=None).first()
        if trans:
            trans.return_date = date.today()
            trans.returned=True
            book.issue=False
            db.session.add(trans)
            db.session.commit()
            message= "Returned"
            return redirect(url_for("return_landing",message=message))  
        
        else:
            message= "No Transaction Found"
            return redirect(url_for("return_landing",message=message))  
    
    return render_template('book_qr_return.html',form=form,userid=user_id)

@app.route("/return_landing",methods=["GET","POST"])
def return_landing():
    message=request.args.get('message')
    return render_template('return_landing.html',message=message)

# <-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->



@app.route('/user_qrscan_info', methods=["POST","GET"])
def user_qrscan_info():
    form=UserQrScan()
    if form.validate_on_submit():
        user = User.query.filter_by(
            qr=form.data.get('qr')
        ).first()
        if user is None:
            return "Invalid QR"

        return redirect(url_for("user_info_table",userid=user.id))    
    return render_template('user_qr_info.html',form=form)

@app.route('/user_info_table', methods=["POST","GET"])
def user_info_table():
    user_id = request.args.get('userid')
    if user_id is None:
        return "Error"
    user = User.query.get(user_id)
    transactions = Transaction.query.filter_by(user_id=user_id).all()

    
    book_ids_taken = [transaction.book_id for transaction in transactions]

    
    books_taken = Books.query.filter(Books.id.in_(book_ids_taken)).all()

    
    book_id_to_title = {book.id: book.title for book in books_taken}

    books_returned = Transaction.query.filter_by(user_id=user_id).count()
    books_not_returned = Transaction.query.filter_by(user_id=user_id, return_date=None).count()
    return render_template('user_table_view_info.html', user=user, transactions=transactions,book_id_to_title=book_id_to_title,books_returned=books_returned,books_not_returned=books_not_returned)
    




