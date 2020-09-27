from models import Tasks, Steps, Categorys, steps_tasks_table, db
from datetime import datetime
import re
from json_data import Category
from sqlalchemy import desc
from linebot import utils 

def main (cat_id):
    cat_data = Categorys.query.filter(Categorys.uid==cat_id).first()
    cat_name = cat_data.name 
    task_data = Tasks.query.filter(Tasks.categorys.has(Tasks.cat_id==cat_id)).all()
    tasks, tasks_id, is_finished, finished_persent = [], [], [], []
    dates, update = [], []
    for item in task_data:
        tasks.append(item.name)
        tasks_id.append(item.uid)
        steps_data = Steps.query.filter(Steps.tasks.any(Tasks.uid==item.uid)).all()

        count = 0
        finished = 1
        for step in steps_data:
            dates.append(step.update_time)
            if step.is_finished == False:
                finished = 0
                count += 1
        update.append(max(dates).strftime('%Y/%m/%d'))
        is_finished.append(finished)
        if count == len(steps_data):
            finished_persent.append(0)
        else:
            finished_persent.append((len(steps_data)-count)/len(steps_data)*100)

    bubble = Category.bubble_json(
        cat_name = cat_name,
        tasks = tasks,
        tasks_id = tasks_id,
        is_finished = is_finished,
        finished_persent = finished_persent,
        update = update
    )
    return bubble.make_json_data()

if __name__ == '__main__':
    cat_id = 1
    main(cat_id)
