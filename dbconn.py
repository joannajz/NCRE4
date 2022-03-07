import pymysql
# 导入pymysql模块
import pymysql
# 连接database
def connsql(sql):
    conn = pymysql.connect(
        host='localhost', port=3306,user='root',password='ccb12345',database='test',charset='utf8')
    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()
    # 定义要执行的SQL语句
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交事务
        conn.commit()
        data=cursor.fetchall()
        return data
    except Exception as e:
        # 有异常，回滚事务
        # 关闭光标对象
        print('dberror')
        conn.rollback()
    else:
        print('db ok')
    cursor.close()
    # 关闭数据库连接
    conn.close()


if __name__ == "__main__":
    # data=connsql('SELECT * FROM test.questions where qid>=0 and qid<=20')
    # print(data,type(data))
    # ans='CDDAA,AAAAC,DAACB,BACDA'
    # ans1=ans.replace(',','')

    dict={}
    with open('tt.txt','r',encoding='utf-8') as f:
        for line in f.readlines():
            line=line.replace('\n','')
            if line =='':
                continue
            elif line[0]=='第':
                
                dict[line]=0
                key=line
            else:
                dict[key]=line
    print(dict)
    for key,val in dict.items():
       sql=f"insert into test.ans(aid,ans20) values('{key}','{val}')"
       connsql(sql) 
