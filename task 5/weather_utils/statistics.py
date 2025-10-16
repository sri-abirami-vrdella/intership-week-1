import statistics
def average_temperature(data):
    return statistics.mean(data)
def max_temperature(data):
    return max(data)
def min_temperature(data):
    return min(data)

city={
    "trichy":[32,34,28],
    "pudukottai":[33,34,30],
    "dindigul":[33,31,37],
    "palani":[28,29,30],
    "coimbatore":[35,29,30],
    "salem":[29,30,33]
}
def get_cities():
    return city.keys()
def get_temp():
    return city