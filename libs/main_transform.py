from models import *
from json_data import Project_Menu

def main ():
    category = Categorys.query.all()
#    print(category)
    carousel = []
    cat_id, cat_name, cat_tasks = [], [], []
    for c in category:
#        print(c.uid)
#        print(c.name)
        item = Tasks.query.filter(Tasks.cat_id==c.uid).all()
        dates, update = [], []
        finished_persent = []
        tasks = []
        for i in item:
#            print(i.desc)
#            print(i.pic)
#            print(i.is_finished)
#            print(i.insert_time)
            steps = Steps.query.filter(Steps.tasks.any(Tasks.uid==i.uid)).all()
            count = 0
            finished = 1
            for step in steps:
                dates.append(step.update_time)
                if step.is_finished == False:
                    finished = 0
                    count += 1
            update = max(dates).strftime('%Y/%m/%d')
            if count == len(steps):
                finished_persent = 0
            else:
                finished_persent = (len(steps)-count)/len(steps)*100

            tt = Project_Menu.task(
                    i.uid,
                    i.name,
                    i.is_finished,
                    finished_persent,
                    update)
            tasks.append(tt)
        cat_tasks.append(tasks)
        cat_id.append(c.uid)
        cat_name.append(c.name)

    carousel_tmp = Project_Menu.main_carousel(cat_id, cat_name, cat_tasks)
    return carousel_tmp.make_json_data()



if __name__ == '__main__':
    main()
