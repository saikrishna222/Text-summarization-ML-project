"""TextSummarizationAndKeywordExtraction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from  user import views
from TextSummarizationAndKeywordExtraction import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name="index.html"),name="main"),
    path('admin_login/',views.Admin_login.as_view(),name="admin_login"),
    path('admin_login_check/', views.Admin_login_check.as_view(), name='admin_login_check'),
    path('admin_logout/', views.Admin_logout.as_view(), name='admin_logout'),
    path('user_login/', views.User_login.as_view(), name='user_login'),
    path('user_register/', TemplateView.as_view(template_name="user_register.html"), name='user_register'),
    path('user_details_save/', views.User_details_save.as_view(), name='user_details_save'),
    path('user_requests/', views.User_requests.as_view(), name='user_requests'),
    path('approve_user<int:id>/', views.Approve_user.as_view(), name='approve_user'),
    path('decline_user<int:id>/', views.Decline_user.as_view(), name='decline_user'),
    path('login/', views.User_Login_Validate.as_view()),
    path('user_info/', views.User_info.as_view(), name='user_info'),
    path('user_logout/', views.User_logout.as_view(), name='user_logout'),
    path('textsumform/', views.Textsumform.as_view(), name='textsumform'),
    path('userhome/', views.Userhome.as_view(), name='userhome'),
    path('getsummarize/', views.Getsummarize.as_view(), name='getsummarize'),
    path('urlsearchsummarization/', views.Urlsearchsummarization.as_view(), name='urlsearchsummarization'),
    path('url_delete/', views.Url_delete.as_view(), name='url_delete'),
    path('docsumform/', views.Docsumform.as_view(), name='docsumform'),
    path('getdocsummarize/', views.Getdocsummarize.as_view(), name='getdocsummarize'),
    path('dataurl/', views.Dataurl.as_view(), name='dataurl'),
    path('summarize_doc/', views.Summarize_doc.as_view(), name='summarize_doc'),
    path('documentsummarizationdata/', views.Documentsummarizationdata.as_view(), name='documentsummarizationdata'),
    path('deletedocumentdata/', views.Deletedocumentdata.as_view(), name='deletedocumentdata'),
    path('ImageUpload/', views.ImageUpload.as_view(), name='ImageUpload'),
    path('GetImageData/', views.GetImageData.as_view(), name='GetImageData'),
    path('ImageExtractionData/', views.ImageExtractionData.as_view(), name='ImageExtractionData'),
    path('DeleteImageData/', views.DeleteImageData.as_view(), name='DeleteImageData'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
