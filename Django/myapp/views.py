from django.shortcuts import render,HttpResponse, redirect
import random
from django.views.decorators.csrf import csrf_exempt # csrf skipping

NextId=4
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
          <ul>
          <li><a href="/create/">create</a></li>
          </ul>
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


@csrf_exempt
def create(request): # 사용자의 데이터를 받아들이고 어떻게 사용할 것인가?
    # create : form 은 데이터를 전송해주고, input 태그로 게시글 정보를 받는다
    global NextId
    if request.method == 'GET':
        article = '''
        <form action = "/create/" method="post">
            <p>  <input type="text" name="title" placeholder="title"> </p>
            <p><textarea name="body" placeholder="body"></textarea></p>
            <p><input type="submit"  ></p>
        </form>
    '''
        return HttpResponse(HTMLTemplate(article))
    
    elif request.method == 'POST': # 게시물을 등록하는 호출이면 다음값을 리턴
        title = request.POST['title'] 
        body = request.POST['body']
        newtopic = {'id':NextId,'title': title, 'body': body}
       
        topics.append(newtopic)
        url = '/read/'+str(NextId)
        NextId +=1
        return redirect(url)

