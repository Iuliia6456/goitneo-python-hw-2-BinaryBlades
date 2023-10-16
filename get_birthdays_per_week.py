from datetime import datetime
from collections import defaultdict

def get_birthdays_per_week(users):
    today = datetime.today().date()
    next_week_birthdays = defaultdict(list)
    
    for i in users:
        name = i["name"]
        birthday = i["birthday"].date()
        this_year_birthdays = birthday.replace(year=today.year)

        if this_year_birthdays < today:
            this_year_birthdays = this_year_birthdays.replace(year=today.year + 1)
            
        delta_days = (this_year_birthdays - today).days
        weekdays = this_year_birthdays.strftime("%A")
        
        if delta_days <= 7 and weekdays == "Saturday" or weekdays == "Sunday":
            weekdays = "Monday"            
            next_week_birthdays[weekdays].append(name)
        elif delta_days <= 7 and weekdays in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
            next_week_birthdays[weekdays].append(name)
    
    result = ''
    for weekdays, names in next_week_birthdays.items():
        result += f"{weekdays}: {', '.join(names)}\n"

    return result
                                   
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
    {"name": "Steve Jobs", "birthday": datetime(1955, 2, 24)},
    {"name": "Pavlo Borshch", "birthday": datetime(1955, 9, 28)},
    {"name": "Monica Us", "birthday": datetime(1965, 10, 19)},
    {"name": "Ivan Kim", "birthday": datetime(1985, 10, 21)},
    {"name": "Mariia Smidth", "birthday": datetime(1995, 10, 18)}]

all_birthdays = get_birthdays_per_week(users)
print(all_birthdays)

