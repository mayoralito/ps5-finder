import os
from target import ps5_search_for_stock

email_to = os.environ.get('EMAIL_TO')
ps5_search_for_stock(email_to=email_to)