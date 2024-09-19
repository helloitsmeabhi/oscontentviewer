from django.urls import *
from .views import *

urlpatterns = [
    
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('mainpage/', mainpage, name='mainpage'),
    path('domain/',domain,name='domain'),
    path('eng/',eng,name="eng"),
    path('trig/',trig,name="trig"),
    path('calculus/',cal,name="cal"),
    path('ang/',angu,name="angu"),
    path('math/',math,name="math"),
    path('science/',science,name="science"),
    path('periodic/',per,name="per"),
    path('hindi/',hindi,name="hindi"),
    path('english/',english,name="english"),
    path('lang/',lang,name="lang"),
    path('gemini/',gemini,name="gem"),
    path('kannada/',kan,name="kan"),
    path('search/',search,name="search"),
    path('arith/',arith,name="arith"),
    path('alg/',alg,name="alg"),
    path('elec/',elec,name="elec"),
    path('bio/',bio,name="bio"),
    path('ml/',ml,name="ml"),
    path('dsa/',dsa,name="dsa")

]