from weather_utils import statistics,formstter
from weather_utils import converter
a=0
while(a!=3):
    a=int(input("\nenter an action\n1.weather report\n2.converter\n3.exit\n"))
    if a==1:
        b=input(f"\nenter a city{statistics.get_cities()}\n")
        formstter.generate_report(b)
    elif a==2:
        c=int(input("\nenter a convterter\n1.c to f\n2.f to c\n3.km to miles\n4.miles to km\n5.m to ft\n6.ft to m"
                    "\n7.kmph to mph\n8.mph to kmph\n"))
        match c:
            case 1:
                d=float(input("enter celsius: "))
                print(f"{converter.celsius_to_fahrenheit(d)}\xb0F")
            case 2:
                d=float(input("enter fahrenheit: "))
                print(f"{converter.fahrenheit_to_celsius(d)}\xb0C")
            case 3:
                d=float(input("enter km: "))
                print(f"{converter.km_to_miles(d)}miles")
            case 4:
                d=float(input("enter miles: "))
                print(f"{converter.miles_to_km(d)}km")
            case 5:
                d=float(input("enter meter: "))
                print(f"{converter.meter_to_foot(d)}foot")
            case 6:
                d=float(input("enter ft: "))
                print(f"{converter.foot_to_meter(d)}m")
            case 7:
                d=float(input("enter kmph: "))
                print(f"{converter.kmph_to_mph(d)}mph")
            case 8:
                d=float(input("enter mph: "))
                print(f"{converter.mph_to_kmph(d)}kmph")

