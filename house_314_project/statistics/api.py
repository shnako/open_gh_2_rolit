__author__ = 'VladIulian'
from django.views.decorators.csrf import csrf_exempt


# Gets the current global consumption from the pi.
def get_current_consumption(request):
    # TODO
    return None

# Gets the average consumption for the specified.
# Have START_DATE and END_DATE in the request.
def get_average_consumption(request):
    start_date = request.META['HTTP_START_DATE']
    end_date = request.META['HTTP_END_DATE']
    return None

# Gets the average consumption for the specified area. HARD CODE for demo.
# Have START_DATE and END_DATE in the request.
def get_area_average_consumption(request):
    start_date = request.META['HTTP_START_DATE']
    end_date = request.META['HTTP_END_DATE']
    return None

# Gets the average consumption for the specified.
# Have START_DATE and END_DATE in the request.
def get_city_average_consumption(request):
    start_date = request.META['HTTP_START_DATE']
    end_date = request.META['HTTP_END_DATE']
    return None