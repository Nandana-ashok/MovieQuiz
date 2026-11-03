"""
URL configuration for MovieQuiz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movie import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("questions/",views.MovieQuestionListCreateView.as_view()),
    path("questions/<int:qid>/", views.MovieQuestionRetrieveUpdateDeleteView.as_view()),
    path("submissions/",views.MovieSubmissionCreateListView.as_view()),
    path("submissions/<int:sid>/",views.MovieSubmissionRetrieveUpdateDeleteView.as_view()),
    path("submissions/<int:sid>/evaluate/",views.EvaluateMovieSubmissionView.as_view()),
]
