from flask import Blueprint, request, current_app, redirect, url_for, render_template
from datetime import datetime
from models import users, Categorys
from sqlalchemy import func , or_
from main import db, app
from line_bot_api import *
import libs.tasks_transform as t_trans
import libs.cat_list_transform as cl_trans
import libs.cat_transform as c_trans
import libs.main_transform as m_trans
import sqlite3
import json

STATUS = ''

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(FollowEvent)
def handle_follow(event):
    user_id = event.source.user_id
    if user_id != 'U1967dc58bc86ac7a20849717ea7c1b69':
        line_bot_api.reply_message (event.reply_token , TextSendMessage(text="您沒有權限喔！"))
        return 0
    profile = line_bot_api.get_profile(user_id) 
    print ("user_id = " + user_id) 
    print("======")
    newcoming_text = profile.display_name + " 請點選以下選單："
    insert_data = users(
            userid=user_id,
            display_name=profile.display_name)
    insert_data.new_user()    
    line_bot_api.link_rich_menu_to_user (user_id , "richmenu-6b0529a448d1c2ad93a5524161e70cd8") 

    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=newcoming_text))

@handler.add(PostbackEvent)
def handle_post_message(event):
    print ("event =" , event)
    if event.postback.data.find('&') != -1:
        cat_id, task_id = event.postback.data.split('&')
#        cat_id = cat_id.split('=')
        task_id , uid = task_id.split('=')
        flex = t_trans.main(uid)
#            with open ('tmp.txt', 'w', encoding='utf-8') as f:
#                f.write(flex)
        parsed_json = json.loads(flex)
        message = FlexSendMessage(
            alt_text='task',
            contents=parsed_json,
        )
        
    else:
        dataType, uid = event.postback.data.split('=')
        if dataType == 'cat_id':
            flex = c_trans.main(uid)
    #        with open ('tmp.txt', 'w', encoding='utf-8') as f:
    #            f.write(flex)
            parsed_json = json.loads(flex)
            message = FlexSendMessage(
                alt_text='cat',
                contents=parsed_json,
            )
        elif dataType == 'task_id':
            flex = t_trans.main(uid)
#            with open ('tmp.txt', 'w', encoding='utf-8') as f:
#                f.write(flex)
            parsed_json = json.loads(flex)
            message = FlexSendMessage(
                alt_text='task',
                contents=parsed_json,
            )

    line_bot_api.reply_message(event.reply_token, message)

#    if event.postback.data == 'type' or event.postback.data == 'ask':
#        text = emergency_postback(event.postback.data)
#    elif event.postback.data == 'church_send' or event.postback.data == 'church_fix':
#        text = ending_check (event , event.source.user_id)
# 
#    line_bot_api.reply_message(event.reply_token , text)

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    global STATUS
    user_id = event.source.user_id
    profile = line_bot_api.get_profile(user_id) 
    insert_data = users(userid=user_id, display_name=profile.display_name)
    insert_data.new_user()
   
    if event.message.text == '社工專用':
        text = "✴️ 查詢教會信件：請輸入'信件查詢A'\n✴️ 查詢教會帳號密碼：請輸入'帳號密碼'\n✴️ 查詢北區服務中心地址：請輸入'交通資訊'。\n✴️ 物資登記相關說明：請輸入'物資相關說明'"
        line_bot_api.reply_message (event.reply_token , TextSendMessage (text = text))
    elif event.message.text == 'Card':
        STATUS = event.message.text
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="請輸入您要查詢的Card_id:"))
#    elif event.message.text == 'Task':
#        flex = t_trans.main(task_id)
##        with open ('tmp.txt', 'w', encoding='utf-8') as f:
##            f.write(flex)
#        parsed_json = json.loads(flex)
#        message = FlexSendMessage(
#            alt_text='task_sample',
#            contents=parsed_json,
#        )
#        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text == 'Category':
        flex = cl_trans.main()
#        with open ('tmp.txt', 'w', encoding='utf-8') as f:
#            f.write(flex)
        parsed_json = json.loads(flex)
        message = FlexSendMessage(
            alt_text='cat',
            contents=parsed_json,
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text == 'Menu':
        flex = m_trans.main()
#        with open ('tmp.txt', 'w', encoding='utf-8') as f:
#            f.write(flex)
        parsed_json = json.loads(flex)
        message = FlexSendMessage(
            alt_text='cat',
            contents=parsed_json,
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text == '搜尋任務':
        pass
    else:
        if event.message.text.isdigit():
            if STATUS == 'Card':
                flex = c_trans.main(int(event.message.text))
#                with open ('tmp.txt', 'w', encoding='utf-8') as f:
#                    f.write(flex)
                parsed_json = json.loads(flex)
                message = FlexSendMessage(
                    alt_text='cat',
                    contents=parsed_json,
                )
                line_bot_api.reply_message(event.reply_token, message)
                STATUS = ''
           
