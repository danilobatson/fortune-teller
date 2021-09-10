from django.shortcuts import render
import random

# Create your views here.
def fortune(request):
  fortune = random.choice(fortuneList)
  context = {'fortune' : fortune}
  return render(request, 'randomfortune/fortune.html', context)

fortuneList = [
    "Like the cat who got its tail stuck in the meat grinder, 'It won't be long now'",
    "Sometimes you the bug, somtimes you the windshield",
    "Ain't nothing smooth to a can of oil",
    "Failing to prepare is preparing to fail",
    "A man will build his destiny on the very path he took to avoid it",
    "The road to hell is paved with good intentions.",
    "How you gon win when you ain't right within?"
]
