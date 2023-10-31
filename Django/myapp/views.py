from django.shortcuts import render,HttpResponse
import random


topics = [
    {'id': 1,'title': 'routing','body':'routing is....'},
    {'id': 2,'title': 'view','body':'view is....'},
    {'id': 3,'title': 'model','body':'model is....'}
]

def HTMLTemplate(articleTag):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
# 제목 부분
    return f'''
     <html>
     <body>
        <h1><a href="/">Django</a></h1> 
        <ul>
            {ol}
        </ul>   
          {articleTag}
     </body>
     </html>
    ''' 


def index(request):
    article = '''
        <h2>Welcome</h2>
          Hello, Django'''

    return HttpResponse(HTMLTemplate(article))

def read(request,id):
    global topics
    article =''
    for topic in topics:
        if topic['id'] == int(id): # api 번호가 일치하면 해당 id 값의 내용을 출력함
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'

    return HttpResponse(HTMLTemplate(article))



def create(request):
    return HttpResponse('Create!')
