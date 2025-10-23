from .statistics import average_temperature,max_temperature, min_temperature
from .statistics import get_temp
temp=get_temp()
def generate_report(city):
    print("\n-------weather report----------\n"
        f"city: {city}")
    print(f"Average temp:{average_temperature(temp[city]):.2f}\xb0C\nMax temp:{max_temperature(temp[city])}\xb0C\n"
          f"Min temp:{min_temperature(temp[city])}\xb0C"
          "\n-------------------------------")