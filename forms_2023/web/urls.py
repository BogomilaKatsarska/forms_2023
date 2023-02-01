from django.urls import path

from forms_2023.web.views import index, index_modelform

urlpatterns = (
    path('', index, name='index'),
    path('modelform/', index_modelform, name='modelform'),
)
