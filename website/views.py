from django.shortcuts import render

from random import randint

def home(request):
    return render(request, 'home.html')

def calc(request, op):
    operation = op

    dict_operation = {
        'add' : '+' ,
        'subtract': '-' ,
        'multiply' : 'x',
        'divide' : '/'
    }

    num_1 = randint(0,9)
    num_2 = randint(1,9) if operation == 'divide' else randint(0,9)

    if request.method == 'POST':
        answer = request.POST['answer']
        
        old_num_1 = int(request.POST['old_num_1'])
        old_num_2 = int(request.POST['old_num_2'])

        # error handling in no form fillout
        if not answer:
            return render(request, 'calc.html', {
                'operation' : dict_operation[operation],
                'color' : 'warning',
                'message' : "You forgot to fill the form",
                'num_1' : old_num_1,
                'num_2' : old_num_2
            })
        if operation == 'add':
            correct_answer = old_num_1 + old_num_2
        if operation == 'subtract':
            correct_answer = old_num_1 - old_num_2
        if operation == 'multiply':
            correct_answer = old_num_1 * old_num_2
        if operation == 'divide':
            correct_answer = old_num_1 / old_num_2

        if float(answer) == correct_answer:
            color = 'success'
            message = f'Correct! {old_num_1} {dict_operation[operation]} {old_num_2} = {correct_answer}'
        else:
            color = 'danger'
            message = f'Incorrect! {old_num_1} {dict_operation[operation]} {old_num_2} is not {answer} but it is {correct_answer}'
        return render(request, 'calc.html', {
            'operation' : dict_operation[operation],
            'answer' : answer,
            'color' : color,
            'message' : message,
            'num_1' : num_1,
            'num_2' : num_2
        })
    return render(request, 'calc.html', {
        'operation' : dict_operation[operation],
        'num_1' : num_1,
        'num_2' : num_2
    })

# def add(request):
#     return render(request, 'add.html')

# def subtract(request):
#     return render(request, 'subtract.html')

# def multiply(request):
#     return render(request, 'multiply.html')

# def divide(request):
#     return render(request, 'divide.html')
