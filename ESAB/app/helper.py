from datetime import date, timedelta

def due_date_calculator():
    return date.today() + timedelta(days=30)