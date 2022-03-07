from flask import Flask,jsonify,render_template
from dbconn import connsql
app=Flask(__name__) #创建对象

dict={
    '题目1':{
        '题干':"hi would you know a,b,c",
        "选项A":"1",
        "选项B":"2",
        "选项C":"3",
        "选项D":"4",
        "选项E":"5"},
    '题目2':{
        '题干':"hi would you know a,b,c",
        "选项A":"1",
        "选项B":"2",
        "选项C":"3",
        "选项D":"4",
        "选项E":"5"}  }

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/detail/<int:qid>')
def detail(qid):
    if '题目'+str(qid) in dict:
        # context={'user':"wangjz"}
        context=dict['题目'+str(qid)]
        print(context)
        # return jsonify(dict['题目'+str(qid)])
        return render_template('detail.html',**context)  #传字典、列表、单个变量等等，还可以传函数，在模板中调用函数
    else:
        return "dont have题目"

# @app.route('/mod/',methods=['POST'])

@app.route('/practice/<int:textid>')
def practice(textid):
    sql=f'SELECT * FROM test.questions where qid>={20*(textid-1)+1} and qid<={textid*20}'
    dict={}
    data=connsql(sql) #元组
    context={'qs':data}

    sql=f'SELECT * FROM test.ans where id={textid};'
    data=connsql(sql)
    context['qa']=data
    print(context.keys())
    return render_template('practice.html',**context)

# @app.route('/test/?<int:textid>')
# def test(textid):
#     sql=f'SELECT * FROM test.questions where qid>={20*(textid-1)+1} and qid<={textid*20}'
#     data=list(connsql(sql)) #元组
#     return render_template('text.html',**data)

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.config['JSON_AS_ASCII'] = False
    app.run()