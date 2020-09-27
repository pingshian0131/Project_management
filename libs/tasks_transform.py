from models import Tasks, Steps, Categorys, steps_tasks_table 
from datetime import datetime
from json_data import Task 

def main (task_id):
    task_data = Tasks.query.filter(Tasks.steps.any(Tasks.uid==task_id)).one()
    steps_data = Steps.query.filter(Steps.tasks.any(Tasks.uid==task_id)).all()
    cat_data = Categorys.query.filter(Categorys.uid==task_data.cat_id).one()
#    message = []
#    message.append("專案類別：{}".format(c.name))
#    message.append("工作名稱：{}".format(a.name))
#    message.append("說明：{}".format(a.desc))
#    message.append("附圖：{}".format(a.pic))
#        print(a.uid, a.cat_id, a.name, a.desc, a.pic)
    is_finished, dates, steps = [], [], []
    for i, item in enumerate(steps_data):
        print(item.uid, item.name, item.time_1, item.time_2)
        steps.append(item.name)
        tmp1 = datetime.strptime(item.time_1, '%Y/%m/%d')
        tmp2 = datetime.strptime(item.time_2, '%Y/%m/%d')
        midpoint = tmp1 + (tmp2-tmp1)/2
        dates.append(midpoint.strftime ('%m/%d'))
        is_finished.append(item.is_finished)
#    message = '\n'.join(message)
#    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))

    bubble = Task.bubble_json(
        pic = task_data.pic,
        title = task_data.name,
        cat = cat_data.name,
        desc = task_data.desc,
        is_finished = is_finished,
        dates = dates,
        steps = steps  
    )
    return bubble.make_json_data()
