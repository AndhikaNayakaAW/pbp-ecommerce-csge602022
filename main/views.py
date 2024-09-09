from django.shortcuts import render

# Create your views here.
def index(request):
    # Prepare the context with basic information
    context = {
        'app_name': 'E-Commerce Application',
        'student_name': 'Andhika Nayaka Arya Wibowo',  
        'student_id': '2306174135',
        'class_name': 'CSGE602022 Platform-Based Programming',
    }
    return render(request, 'main/index.html', context)
