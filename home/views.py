from django.shortcuts import render

def home(request):
    peoples = [
        {"name": 'Amjad', 'age' : 28},
        {"name": 'Asad', 'age' : 29},
        {"name": 'Arshad', 'age' : 30},
        {"name": 'Kashif', 'age' : 31},
    ]
    vegetables = ['Tomato', 'Potato', 'Onion', 'Cabbage']
    return render(request, 'home/index.html', context={'peoples':peoples, 'vegetables':vegetables})