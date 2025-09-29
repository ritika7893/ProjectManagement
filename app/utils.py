import random
from datetime import datetime

def generate_user_id(prefix):
    year = datetime.now().year
    random_number = random.randint(100000, 999999)  # 6-digit random number
    return f"{prefix}/{year}/{random_number}"