import tkinter as tk
from tkinter import messagebox  # import this to fix messagebox error
import pickle
from PIL import ImageTk, Image
from qmatchq import match
from aIndex import addQA
from fcty import run1
from TFIDF import run2
# 创建主窗口
window = tk.Tk()
window.title('欢迎进入智能问答系统')
window.geometry('450x300')




canvas=tk.Canvas(window,height=300,bg='#B0C4DE',width=450)
#image=window_QA_canvas.create_image(200,150,image=photo)
canvas.pack(side='bottom')

# 用户信息
tk.Label(window, text='用户名:').place(x=100, y=150)  # 创建一个`label`名为`User name: `置于坐标（120,150）
tk.Label(window, text='密码:').place(x=100, y=190)
# 账号密码输入框
var_usr_name = tk.StringVar()  # 定义变量,用于输入用户名
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)  # 创建输入框
entry_usr_name.place(x=160, y=150)
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')  # `show`这个参数将输入的密码变为`***`的形式
entry_usr_pwd.place(x=160, y=190)

def QAsys():
    def inquiry():
        question=q_str.get()
        #print(question)
        (simi,astring)=match(question)
        if simi==-1:
            tk.messagebox.showinfo(title='Failed',message='找不到您需要的答案')
        else:
            mainanswer='匹配结果:\n'
            for i in range(0,len(simi)):
                mainanswer=mainanswer+astring[i]+'相似度:'+simi[i]+'\n'
                print(mainanswer)
            tk.messagebox.showinfo(title='answerList',message=mainanswer)
        #print(mainanswer)

    window_QA = tk.Toplevel(window)
    window_QA.geometry('450x300')
    window_QA.title('问答窗口')
    #背景图片
    window_QA_canvas=tk.Canvas(window_QA,height=300,bg='#B0C4DE',width=450)
    #image=window_QA_canvas.create_image(200,150,image=photo)
    window_QA_canvas.pack(side='bottom')

    q_str=tk.StringVar()
    tk.Label(window_QA,text='请输入您的问题：').place(x=10,y=150)
    tk.Entry(window_QA,textvariable=q_str).place(x=150,y=150)
    bt_confirm_sign_up=tk.Button(window_QA,text='查询',command=inquiry)
    bt_confirm_sign_up.place(x=360,y=150)

    def quit():
        window_QA.destroy()
    bt_quit=tk.Button(window_QA,text='退出登陆',command=quit)
    bt_quit.place(x=365,y=270)





##用户登录函数
def usr_log_in():
    #输入框获取用户名密码
    usr_name=var_usr_name.get()
    usr_pwd=var_usr_pwd.get()
    #从本地字典获取用户信息，如果没有则新建本地数据库
    try:
        with open('usr_info.pickle','rb') as usr_file:
            usrs_info=pickle.load(usr_file)
    except FileNotFoundError:
        with open('usr_info.pickle','wb') as usr_file:
            usrs_info={'admin':'admin'}
            pickle.dump(usrs_info,usr_file)
    #判断用户名和密码是否匹配
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title='welcome',
                                   message='欢迎您：'+usr_name)
            QAsys()
        else:
            tk.messagebox.showerror(message='密码错误')
    #用户名密码不能为空
    elif usr_name=='' or usr_pwd=='' :
        tk.messagebox.showerror(message='用户名或密码为空')
    #不在数据库中弹出是否注册的框
    else:
        is_signup=tk.messagebox.askyesno('欢迎','您还没有注册，是否现在注册')
        if is_signup:
            usr_sign_up()


#注册函数
def usr_sign_up():
    #确认注册时的相应函数
    def signtowcg():
        #获取输入框内的内容
        nn=new_name.get()
        np=new_pwd.get()
        npf=new_pwd_confirm.get()
 
        #本地加载已有用户信息,如果没有则已有用户信息为空
        try:
            with open('usr_info.pickle','rb') as usr_file:
                exist_usr_info=pickle.load(usr_file)
        except FileNotFoundError:
            exist_usr_info={}           
            
        #检查用户名存在、密码为空、密码前后不一致
        if nn in exist_usr_info:
            tk.messagebox.showerror('错误','用户名已存在')
        elif np =='' or nn=='':
            tk.messagebox.showerror('错误','用户名或密码为空')
        elif np !=npf:
            tk.messagebox.showerror('错误','密码前后不一致')
        #注册信息没有问题则将用户名密码写入数据库
        else:
            exist_usr_info[nn]=np
            with open('usr_info.pickle','wb') as usr_file:
                pickle.dump(exist_usr_info,usr_file)
            tk.messagebox.showinfo('欢迎','注册成功')
            #注册成功关闭注册框
            window_sign_up.destroy()

    # 这里就是在主体窗口的window上创建一个Sign up window窗口

    #新建注册界面
    window_sign_up=tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('注册')

    window_sign_up_canvas=tk.Canvas(window_sign_up,height=200,bg='#B0C4DE',width=350)
    #image=window_sign_up_canvas.create_image(200,150,image=photo)
    window_sign_up_canvas.pack(side='bottom')

    #用户名变量及标签、输入框
    new_name=tk.StringVar()
    tk.Label(window_sign_up,text='用户名：').place(x=10,y=10)
    tk.Entry(window_sign_up,textvariable=new_name).place(x=150,y=10)
    #密码变量及标签、输入框
    new_pwd=tk.StringVar()
    tk.Label(window_sign_up,text='请输入密码：').place(x=10,y=50)
    tk.Entry(window_sign_up,textvariable=new_pwd,show='*').place(x=150,y=50)    
    #重复密码变量及标签、输入框
    new_pwd_confirm=tk.StringVar()
    tk.Label(window_sign_up,text='请再次输入密码：').place(x=10,y=90)
    tk.Entry(window_sign_up,textvariable=new_pwd_confirm,show='*').place(x=150,y=90)    
    #确认注册按钮及位置
    bt_confirm_sign_up=tk.Button(window_sign_up,text='确认注册',
                                 command=signtowcg)
    bt_confirm_sign_up.place(x=150,y=130)
    def quit():
        window_sign_up.destroy()
    bt_signup_quit=tk.Button(window_sign_up,text='返回',command=quit)
    bt_signup_quit.place(x=300,y=170)

def Admin():
    window_Admin = tk.Toplevel(window)
    window_Admin.geometry('450x300')
    window_Admin.title('管理员窗口')
    #背景图片
    window_Admin_canvas=tk.Canvas(window_Admin,height=300,bg='#B0C4DE',width=450)
    #image=window_Admin_canvas.create_image(200,150,image=photo)
    window_Admin_canvas.pack(side='bottom')
    def add():

        window_add=tk.Toplevel(window_Admin)
        window_add.geometry('350x200')
        window_add.title('添加问答对')

        window_add_canvas=tk.Canvas(window_add,height=200,bg='#B0C4DE',width=350)
        #image=window_add_canvas.create_image(200,150,image=photo)
        window_add_canvas.pack(side='bottom')

        #用户名变量及标签、输入框
        question=tk.StringVar()
        tk.Label(window_add,text='请输入问题：').place(x=10,y=10)
        tk.Entry(window_add,textvariable=question).place(x=150,y=10)
        #密码变量及标签、输入框
        answer=tk.StringVar()
        tk.Label(window_add,text='请输入对应答案：').place(x=10,y=50)
        tk.Entry(window_add,textvariable=answer).place(x=150,y=50)    
        def confirm_add():
            a_question=question.get()
            a_answer=answer.get()
            result=addQA(a_question,a_answer)
            if result ==1:
                tk.messagebox.showinfo(title='Success for adding',
                                       message='添加成功!\n question:'+a_question+'\n answer'+a_answer+'\n\n正在更新语料库，请稍后')
                run1()
                run2()
                tk.messagebox.showinfo(title='Success for running',message='更新成功')
                window_add.destroy()
            else:
                tk.messagebox.showinfo(title='Fail for adding',
                                       message='添加失败请重试!\n '+a_question+'\n answer'+a_answer)

        #确认添加按钮及位置
        bt_confirm_sign_up=tk.Button(window_add,text='确认添加',
                                     command=confirm_add)
        bt_confirm_sign_up.place(x=150,y=130)
        def quit():
            window_add.destroy()
        window_add_quit=tk.Button(window_add,text='返回',command=quit)
        window_add_quit.place(x=300,y=170)



    bt_add=tk.Button(window_Admin,text='添加问题-答案',command=add)
    bt_add.place(x=120,y=150)

    def search():
        tk.messagebox.showinfo(title='building now',
                                       message='正在开发中，请等待')
    bt_add=tk.Button(window_Admin,text='模糊查找',command=search)
    bt_add.place(x=250,y=150)

    def quit():
        window_Admin.destroy()
    bt_quit=tk.Button(window_Admin,text='退出登陆',command=quit)
    bt_quit.place(x=390,y=270)

def admin_login():
    window_admin_login=tk.Toplevel(window)
    window_admin_login.geometry('450x300')
    window_admin_login.title('管理员登陆')

    window_admin_login_canvas=tk.Canvas(window_admin_login,height=300,bg='#B0C4DE',width=450)
    #image=window_admin_login_canvas.create_image(200,150,image=photo)
    window_admin_login_canvas.pack(side='bottom')
    # 用户信息
    tk.Label(window_admin_login, text='管理员账号:').place(x=100, y=150)  # 创建一个`label`名为`User name: `置于坐标（120,150）
    tk.Label(window_admin_login, text='密码:').place(x=100, y=190)
    # 账号密码输入框
    var_admin_id = tk.StringVar()  # 定义变量,用于输入用户名
    entry_usr_name = tk.Entry(window_admin_login, textvariable=var_admin_id)  # 创建输入框
    entry_usr_name.place(x=170, y=150)
    var_admin_pwd = tk.StringVar()
    entry_usr_pwd = tk.Entry(window_admin_login, textvariable=var_admin_pwd, show='*')  # `show`这个参数将输入的密码变为`***`的形式
    entry_usr_pwd.place(x=170, y=190)
    def quit():
        window_admin_login.destroy()
    bt_login_quit=tk.Button(window_admin_login,text='返回',command=quit)
    bt_login_quit.place(x=410,y=265)

    ##管理员登录函数
    def admin_log_in():
        #输入框获取用户名密码
        usr_name=var_admin_id.get()
        usr_pwd=var_admin_pwd.get()
        #从本地字典获取用户信息，如果没有则新建本地数据库
        try:
            with open('admin_info.pickle','rb') as usr_file:
                usrs_info=pickle.load(usr_file)
        except FileNotFoundError:
            with open('admin_info.pickle','wb') as usr_file:
                usrs_info={'admin':'admin'}
                pickle.dump(usrs_info,usr_file)
        #判断用户名和密码是否匹配
        if usr_name in usrs_info:
            if usr_pwd == usrs_info[usr_name]:
                tk.messagebox.showinfo(title='welcome',
                                       message='欢迎您，管理员：'+usr_name)
                window_admin_login.destroy()
                Admin()
            else:
                tk.messagebox.showerror(message='密码错误')
        #用户名密码不能为空
        elif usr_name=='' or usr_pwd=='' :
            tk.messagebox.showerror(message='用户名或密码为空')
        #不在数据库中弹出是否注册的框

    bt_login=tk.Button(window_admin_login,text='登录',command=admin_log_in)
    bt_login.place(x=370,y=265)


#登录 注册按钮
bt_login=tk.Button(window,text='登录',command=usr_log_in)
bt_login.place(x=140,y=230)
#bt_login.pack()
bt_logup=tk.Button(window,text='注册',command=usr_sign_up)
bt_logup.place(x=210,y=230)
#bt_logup.pack()

#退出的函数
def usr_sign_quit():
    window.destroy()

bt_logquit=tk.Button(window,text='退出',command=usr_sign_quit)
bt_logquit.place(x=280,y=230)
#bt_logquit.pack()
bt_logquit=tk.Button(window,text='管理员模式',bg='#8DB6CD',command=admin_login)
bt_logquit.place(x=377,y=269)
#96CDCD
window.mainloop()
