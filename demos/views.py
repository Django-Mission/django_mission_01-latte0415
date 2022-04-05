from django.shortcuts import render
import random

# Create your views here.
def lotto_input(request):
    return render(request, "lotto_input.html")


def lotto_output(request):
    # 1. input
    num_game = int(request.GET.get("num_game"))

    # 2. process
    result = []
    for i in range(num_game):
        # result_i = []
        # for j in range(7):
        #    result_i.append(random.randint(1, 46))
        result_i = random.sample(range(1, 46), 7)
        result.append(result_i)

    return render(
        request, "lotto_output.html", {"num_game": num_game, "result": result}
    )
