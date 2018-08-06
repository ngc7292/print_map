from django.test import TestCase

# Create your tests here.

from views import handle_citys

citys = ["日照","莒县","临沂"]

print(handle_citys(citys))