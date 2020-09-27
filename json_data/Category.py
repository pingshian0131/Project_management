import json
from datetime import datetime

class bubble_json ():
    def __init__(self, cat_name, tasks, tasks_id, is_finished, finished_persent, update):
        self.cat_name = cat_name 
        self.tasks = tasks ### data_type = list 
        self.tasks_id = tasks_id ### data_type = list 
        self.is_finished = is_finished ### data_type = list 
        self.finished_persent = finished_persent ### data_type = list 
        self.update = update 

    def make_task_box (self):
        json = ''
        box_1 = '''
                  {
                    "type": "filler",
                    "flex": 1
                  },'''
        box_2 = '''
                  {
                    "type": "text",
                    "text": "✅",
                    "flex": 1,
                    "gravity": "center"
                  },'''
        is_finished_box = [box_1, box_2]
        for i in range (len(self.tasks)):
            tmp = '''
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [''' + is_finished_box[self.is_finished[i]] + '''
                  {
                    "type": "text",
                    "text": "''' + str(i+1) + '''.",
                    "align": "center",
                    "flex": 1,
                    "gravity": "center"
                  },
                  {
                    "type": "button",
                    "action": {
                      "type": "postback",
                      "label": "''' + self.tasks[i] + '''",
                      "data": "task_id=''' + str(self.tasks_id[i]) + '''"
                    },
                    "style": "link",
                    "height": "sm",
                    "flex": 6
                  }
                ]
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "filler",
                    "flex": 2
                  },
                  {
                    "type": "text",
                    "text": "''' + str(self.finished_persent[i]) + '''%",
                    "flex": 2,
                    "size": "xs",
                    "color": "#8c8c8c",
                    "gravity": "center"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "filler"
                              }
                            ],
                            "cornerRadius": "10px",
                            "backgroundColor": "#ff359a",
                            "width": "''' + str(self.finished_persent[i]) + '''%"
                          }
                        ],
                        "cornerRadius": "10px",
                        "backgroundColor": "#ffd9ec",
                        "height": "10px"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "flex": 4
                  }
                ]
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "filler",
                    "flex": 2
                  },
                  {
                    "type": "text",
                    "text": "Update: ''' + self.update[i] + '''",
                    "gravity": "center",
                    "flex": 6,
                    "size": "xs",
                    "color": "#8c8c8c"
                  }
                ]
              }
            ],
            "spacing": "xs"
          }'''
            json += tmp
            if i != len(self.tasks)-1: json += ','
        return json

    def make_json_data (self):
        data  = '''{
  "type": "bubble",
  "size": "mega",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "''' + self.cat_name + '''",
            "color": "#ffffff",
            "size": "xl",
            "weight": "bold"
          },
          {
            "type": "text",
            "text": "send_time: ''' + datetime.now().strftime('%Y/%m/%d %H:%M') + '''",
            "color": "#ecf5ff",
            "size": "sm",
            "align": "end"
          }
        ],
        "spacing": "md"
      }
    ]
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [''' + self.make_task_box() + '''
        ],
        "spacing": "sm"
      },
      {
        "type": "text",
        "text": "共 ''' + str(len(self.tasks)) + ''' 個項目",
        "color": "#b7b7b7",
        "align": "end",
        "size": "xs",
        "flex": 1,
        "gravity": "bottom"
      }
    ],
    "spacing": "lg"
  },
  "styles": {
    "header": {
      "backgroundColor": "#ff0000"
    },
    "body": {
      "backgroundColor": "#ecf5ff"
    }
  }
}'''

        return data
