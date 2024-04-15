
# from . import db
# from .models import Transaction, User,Books,Late
# from datetime import datetime

# def create_late_table_entries():
#     current_date = datetime.now()

#     transactions = Transaction.query.filter(Transaction.return_date > current_date, Transaction.returned == False).all()


#     for transaction in transactions:
#         user = User.query.get(transaction.user_id)
#         book = Books.query.get(transaction.book_id)

#         late_entry = Late(
#             user_first_name=user.first_name,
#             user_last_name=user.last_name,
#             phone_number=user.phone_number,
#             book_title=book.title,
#             return_date=transaction.return_date
#         )

#         db.session.add(late_entry)

#     db.session.commit()


