from django.shortcuts import render
import time

def test2(request):
    if request.method == 'POST':
        start = time.time()
        nth=request.POST.get('number')
        input=nth
        nth=int(nth)
        print(nth)
        print(type(nth))
        n1 = 1
        n2 = 1
        arr = []
        # check if the number of terms is valid
        if nth <= 0:
            error_message="Please enter a positive integer"
            print("Please enter a positive integer")
            return render(request, 'Test.html',{"error_message":error_message})
        else:
            print("Fibonacci sequence upto", nth)
            for  i in range(nth):
                # print(n1, end=' , ')
                arr.append(n1)
                nth = n1 + n2
                # update values
                n1 = n2
                n2 = nth

        print(arr)
        nth_term=arr[len(arr)-1]
        print(nth_term)
        a=time.time() - start
        print(a)

        return render(request, 'Test.html', {'nth_term': nth_term,"input":input,"a":a})
    else:
        return render(request, 'Test.html', )


