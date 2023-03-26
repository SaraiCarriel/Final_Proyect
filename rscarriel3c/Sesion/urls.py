from django.urls import path, include
from Sesion import views
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static

urlpatterns = [
	path('',LoginView.as_view(template_name= 'login.html'), name="login"),
	path('',LogoutView.as_view(template_name= 'index.html'),name="logout"),
	path('signup/', views.signup, name='signup'),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)