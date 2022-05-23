from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,ListView
from django.contrib import messages
from user.models import UserRegistrationModel, UrlSummarization, DocumentUploadMOdel, DocumentSummarizationModel, \
    ImageDataExtractionModel
from user.summarize import sum_it_up
import requests
from django.core.files.storage import FileSystemStorage
from user.extract_image_data import ExtractsImagesData
from newspaper import Article
# for removing square brackets
import re

# Gensim summarizer
from gensim.summarization.summarizer import summarize

# For extracting the keywords
from gensim.summarization import keywords



class Admin_login(TemplateView):
    template_name = "admin_login.html"

class Admin_login_check(View):
    def post(self,requset):
        uname=requset.POST.get("uname")
        pword=requset.POST.get("pword")
        if uname=="admin" and pword=="admin":
            return render(requset,"admin_home.html")
        else:
            messages.success(requset,"Invalid Details")
            return redirect('admin_login')

class Admin_logout(View):
    def get(self,request):
        return redirect('main')

class User_login(TemplateView):
    template_name = "user_login.html"
    extra_context ={"data":"data"}
class User_details_save(View):
    def post(self,request):
        uname=request.POST.get("uname")
        pword=request.POST.get("pword")
        email=request.POST.get("email")
        address=request.POST.get("address")
        status="pending"
        UserRegistrationModel.objects.create(user_name=uname,email=email,password=pword,current_address=address,status=status)
        messages.success(request,"User Registered Successfully")
        return redirect('user_register')
class User_requests(ListView):
    model = UserRegistrationModel
    queryset = UserRegistrationModel.objects.filter(status="pending")
    template_name = 'admin_home.html'
    context_object_name ="Udata"
class Approve_user(View):
    def get(self,request,id):
        qs=UserRegistrationModel.objects.filter(idno=id)
        qs.update(status="approved")
        return render(request,"admin_home.html",{"data":"User Approved"})

class Decline_user(View):
    def get(self,request,id):
        qs=UserRegistrationModel.objects.filter(idno=id)
        qs.update(status="declined")
        return render(request,"admin_home.html",{"data":"User Declined"})

class User_Login_Validate(View):
    def post(self,request):
        uname=request.POST.get("uname")
        pword=request.POST.get("pword")
        qs=UserRegistrationModel.objects.filter(user_name=uname,password=pword)
        for x in qs:
            status=x.status
            mail=x.email
        if qs and status=="approved":
            request.session["mail"]=mail
            return render(request,"user_home.html",{"name":uname})
        elif qs and (status=="pending" or status=="declined"):
            messages.success(request, "Your details need to approve by admin..please wait until approve..!")
            return redirect('user_login')
        else:
            messages.success(request,"Invalid Details")
            return redirect('user_login')


class User_info(ListView):
    model = UserRegistrationModel
    template_name = 'admin_home.html'
    context_object_name ="uidata"

class User_logout(View):
    def get(self,request):
        messages.success(request, "Sucessfully Logged Out")
        return redirect('main')


class Textsumform(TemplateView):
    template_name = "textsumform.html"
    extra_context = {"my_data":"data"}


class Userhome(View):
    def get(self,req):
        mail=req.session["mail"]
        ob=UserRegistrationModel.objects.get(email=mail)
        return render(req,"user_home.html",{"name":ob.user_name})


class Getsummarize(View):
    def post(self,req):
        url=req.POST.get("link")
        url1=req.POST.get("link1")
        url2=req.POST.get("link2")
        mail=req.session["mail"]
        my=dict(req.POST)
        del my["csrfmiddlewaretoken"]
        print(my,"================================")
        m1=my['link']
        m2=my['link1']
        m3=my['link2']

        if m1[0] != '' and (m2[0] =='' and m3[0] == ''):
            print(url, "iam if")
            article = Article(url)
            article.download()
            # parses the downloaded html
            article.parse()
            content1 = article.text
            content=content1

        elif (m1[0] =='' and m2[0] =='') and m3[0] !='':
            print(url2, "iam first elif")
            article2 = Article(url2)
            article2.download()
            # parses the downloaded html
            article2.parse()
            content3 = article2.text
            content=content3

        elif (m1[0]=='' and m3[0] =='') and m2[0] !='':
            print(url1, "iam second elif")
            article1 = Article(url1)
            article1.download()
            # parses the downloaded html
            article1.parse()
            content2 = article1.text
            content=content2

        elif m1[0]!='' and m2[0]!='' and m3[0]!='':
            print(url, url1, url2, "iam third elif")

            article = Article(url)
            article.download()
            # parses the downloaded html
            article.parse()
            content1 = article.text

            article2 = Article(url2)
            article2.download()
            # parses the downloaded html
            article2.parse()
            content3 = article2.text

            article1 = Article(url1)
            article1.download()
            # parses the downloaded html
            article1.parse()
            content2 = article1.text
            content=content2+content3+content1


        elif ( m1[0]!='' and m2[0]!='') and m3[0] =='':
            print(url, url1, "iam fourth elif")
            article = Article(url)
            article.download()
            # parses the downloaded html
            article.parse()
            content1 = article.text

            article1 = Article(url1)
            article1.download()
            # parses the downloaded html
            article1.parse()
            content2 = article1.text
            content=content2+content1


        elif (m1[0] !='' and m3[0]!='') and m2[0]=='':
            print(url, url2, "iam fifth elif")
            article = Article(url)
            article.download()
            # parses the downloaded html
            article.parse()
            content1 = article.text

            article2 = Article(url2)
            article2.download()
            # parses the downloaded html
            article2.parse()
            content3 = article2.text
            content=content3+content1

        elif (m2[0] !='' and m3[0] !='') and m1[0] =='':
            print(url1, url2, "iam sixth elif")

            article1 = Article(url1)
            article1.download()
            # parses the downloaded html
            article1.parse()
            content2 = article1.text

            article2 = Article(url2)
            article2.download()
            # parses the downloaded html
            article2.parse()
            content3 = article2.text
            content=content2+content3

        else:
            return HttpResponse("<html><body><center><h1>Upload Atleast One URL Link</h1></center></body></html>")

        re.sub(r'\[.+\]', '', content)

        # finds a list of 10 important keywords, usses lemmetatization instead of stemming
        from gensim.summarization import keywords
        k = keywords(content, words=20, lemmatize=True).split('\n')
        keywords = ', '.join(k)
        text = summarize(content,0.2)
        len_content=str(content)
        len_content=len(len_content.split())
        text_len=str(text)
        text_len=len(text_len.split())
        UrlSummarization.objects.create(user_mail=mail,url_link=(url+' '+url1+' '+url2),summarized_content=text,content_keywords=keywords,len_total_content=len_content,len_summarized_content=text_len)
        return render(req,"textsumform.html",{"text":text,"key":keywords,"Bcontent":len_content,"Acontent":text_len})

class Urlsearchsummarization(View):
    def get(self,req):
        mail=req.session["mail"]
        data = UrlSummarization.objects.filter(user_mail=mail)
        return render(req,"urlsearchsummarization.html",{"data":data})


class Url_delete(View):
    def get(self,req):
        sid=req.GET.get("id")
        UrlSummarization.objects.get(sid=sid).delete()
        return redirect('userhome')


class Docsumform(TemplateView):
    template_name = 'docsumform.html'
    extra_context = {"my_data": "data"}

import os
import random
class Getdocsummarize(View):
    def post(self,req):
        file=req.FILES["file"]
        file1=str(file)
        file1=file1.lower()
        if file1.endswith(".txt"):
            mail = req.session["mail"]
            dno=random.randint(999,999999999)
            DocumentUploadMOdel.objects.create(user_mail=mail,dno=dno,document=file)
            data = DocumentUploadMOdel.objects.filter(dno=dno)
            return render(req, "docsumform.html", {"text": data})
        else:
            messages.success(req,"Please Upload the documents in '.txt' format..!")
            return redirect('docsumform')


class Dataurl(View):
    def get(self,req):
        mail=req.session["mail"]
        data = DocumentUploadMOdel.objects.filter(user_mail=mail)
        return render(req,"docsumform.html",{"text":data})

from user.summarize_doc import sum_it_up
class Summarize_doc(View):
    def get(self,req):
        dno=req.GET.get("dno")
        data=DocumentUploadMOdel.objects.get(dno=dno)
        total_data=requests.get("http://127.0.0.1:8000/media/" + str(data.document))
        total_data=total_data.content
        total_data=total_data.decode("utf-8")
        text, keywords, len_content=sum_it_up(total_data)
        length =str(text)
        length=len(length.split())
        DocumentSummarizationModel.objects.create(dno=dno,document_link=data.document,user_mail=req.session["mail"],summarized_content=text,content_keywords=keywords,len_total_content=len_content,len_summarized_content=length)
        return render(req,"docsumform.html",{"summary":text,"key":keywords,"Bcontent":len_content,"Acontent":length})


class Documentsummarizationdata(View):
    def get(self,req):
        mail=req.session["mail"]
        data = DocumentSummarizationModel.objects.filter(user_mail=mail)
        return render(req,"Documentsummarizationdata.html",{"data":data})


class Deletedocumentdata(View):
    def get(self,req):
        sid=req.GET.get("id")
        DocumentSummarizationModel.objects.get(dno=sid).delete()
        return redirect('userhome')


class ImageUpload(TemplateView):
    template_name = 'imagedataform.html'
    extra_context = {"my_data": "data"}

class GetImageData(View):
    def post(self,req):
        file=req.FILES["file"]
        file1=str(file)
        file1=file1.lower()
        if file1.endswith(".jpg"):
            mail = req.session["mail"]
            ino=random.randint(999,999999999)
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            uploaded_file_url = fs.url(filename)
            ob=ExtractsImagesData()
            data=ob.extract_data(filename)
            original=str(data)
            original=len(original.split())
            content=str(data)
            re.sub(r'\[.+\]', '', content)
            data=summarize(content)
            k = keywords(content, words=20, lemmatize=True).split('\n')
            kwords = ', '.join(k)
            len_data=str(data)
            len_data=len(len_data.split())
            ImageDataExtractionModel.objects.create(ino=ino,user_mail=mail,image=file,content_keywords=kwords,len_total_content=original,data_extraction=data,len_extracted_data=len_data)
            return render(req, "imagedataform.html",{"summary":data,"key":kwords,"Bcontent":original,"Acontent":len_data})
        else:
            messages.success(req,"Please Upload The Images In '.jpg' Format..!")
            return redirect('ImageUpload')


class ImageExtractionData(View):
    def get(self,req):
        mail=req.session["mail"]
        data = ImageDataExtractionModel.objects.filter(user_mail=mail)
        return render(req,"ImageExtractionData.html",{"data":data})


class DeleteImageData(View):
    def get(self,req):
        sid=req.GET.get("id")
        ImageDataExtractionModel.objects.get(ino=sid).delete()
        return redirect('userhome')