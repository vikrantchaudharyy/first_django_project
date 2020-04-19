from django.urls import path
from first_app import views

## for relative url injection in html templates
app_name = "first_app"

urlpatterns = [
        path('index/',views.index, name="index"),
        path('formpage/',views.form_name_view, name="form_name_view"),
        path(r'users/',views.users,name='users'),
        path(r'accessrecord/',views.accessRecord,name='users'),
        path(r'relative/',views.relative,name='relative'),
        path(r'other/',views.other,name='other'),

]
