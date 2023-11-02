from django.shortcuts import render,HttpResponse, redirect
import random
from django.views.decorators.csrf import csrf_exempt # csrf skipping

NextId=4
topics = [
    {'id': 1,'title': 'routing','body':'routing is....'},
    {'id': 2,'title': 'view','body':'view is....'},
    {'id': 3,'title': 'model','body':'model is....'}
]

def HTMLTemplate(articleTag, id=None): # 기본적인 템플릿(홈)
    global topics
    contextUI =''
    if id != None:# delete 버튼이 게시물을 클릭했을때 나타나게끔하기(method='post')
        contextUI =f'''
            <li>
                <form action="/delete/" method="post">
                    <input type="hidden" name="id" value={id}>
                    <input type="submit" value="delete">
                </form>
            </li>
'''
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>' #포스트 로딩 및 버튼 생성
    return f'''
     <html>
     <body>
        <h1><a href="/">Django 픽미업</a></h1>
        <h2>POST</h2>
        <ul>
            {ol}
        </ul>
        <h2> </h2>
         {articleTag}

          <ul>
          <li><a href="/create/">create(type: post / id+1)</a></li>
           {contextUI}
          </ul>
     </body>
     </html>
    ''' 


def index(request): # -> HTMLTemplate(articleTag)
    article = '''
        <h2>Welcome</h2>
          Hello, Django'''

    return HttpResponse(HTMLTemplate(article)) 

def read(request,id): # 게시물을 읽는 기능
    global topics
    article ='' 
    for topic in topics:
        if topic['id'] == int(id): # api 번호가 일치하면 해당 id 값의 내용을 출력함
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'

    return HttpResponse(HTMLTemplate(article, id))


@csrf_exempt
def create(request): # 사용자의 데이터를 받아들이고 어떻게 사용할 것인가?
    # create : form 은 데이터를 전송해주고, input 태그로 게시글 정보를 받는다
    global NextId
    if request.method == 'GET':
        article = '''
        <form action = "/create/" method="post">
            <p><input type="text" name="title" placeholder="title"></p>
            <p><textarea name="body" placeholder="body"></textarea></p>
            <p><input type="submit"  ></p>
        </form>
    '''
        return HttpResponse(HTMLTemplate(article))
    
    elif request.method == 'POST': # 제출 버튼을 클릭하면 시행
        title = request.POST['title'] 
        body = request.POST['body']
        newtopic = {'id':NextId,'title': title, 'body': body}
       
        topics.append(newtopic)
        url = '/read/'+str(NextId)
        NextId +=1
        return redirect(url)

@csrf_exempt
def delete(request):
    global topics
    if request.method == 'POST':
        id = request.POST['id']
        newTopic =[]
        for topic in topics:
            if topic['id'] != int(id):
                newTopic.append(topic)
        topics = newTopic
        return redirect('/') #delete 버튼을 누르면 홈화면으로 바로이동