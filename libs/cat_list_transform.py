from models import Tasks, Steps, Categorys, steps_tasks_table 
from datetime import datetime
from json_data import Category_list 

def main ():
    cat_data = Categorys.query.all()
    title, cat_id, remain = [], [], []
    for item in cat_data:
        title.append(item.name)
        cat_id.append(item.uid)
        task_data = Tasks.query.filter(Tasks.categorys.has(Tasks.cat_id==item.uid)).all()
        count = 0
        for task in task_data:
            if task.is_finished == False:
                count += 1
        remain.append(count)

    bubble = Category_list.bubble_json(
        title = title,
        cat_id = cat_id,
        remain = remain,
    )
    return bubble.make_json_data()

if __name__ == '__main__':
    main()
