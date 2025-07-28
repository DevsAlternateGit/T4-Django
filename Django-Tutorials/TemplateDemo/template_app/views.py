from django.shortcuts import render

# Create your views here.
def demo(request):
    context = {
        'name': 'Rahul',
        'age': 25,
        'numbers': [1, 2, 3, 4, 5],
        'show_numbers': True
    }
    return render(request, 'template_app/demo.html', context)