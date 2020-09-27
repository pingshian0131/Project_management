from datetime import datetime 

class task ():
    def __init__ (self, task_uid, task_name, is_finished, finished_persent, update):
        self.task_uid = task_uid
        self.task_name = task_name
        self.is_finished = is_finished 
        self.finished_persent = finished_persent 
        self.update = update 

class main_carousel ():
    def __init__ (self, cat_id, cat_name, tasks):
        self.cat_id = cat_id  ### dataType = list 
        self.cat_name = cat_name  ### dataType = list 
        self.tasks = tasks  ### dataType = list 
        self.header_color = ['#ff0000', '#ff9224', '#ffd306', '#00bb00', '#84c1ff']

    def make_task_box (self, card_num):
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
        for i in range (len(self.tasks[card_num])):
            print(self.tasks[card_num][i].task_name)
            print(len(self.tasks[card_num]))
            tmp = '''{
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [''' + is_finished_box[self.tasks[card_num][i].is_finished] + '''
                      {
                        "type": "text",
                        "text": "''' + str(i+1) + '''.",
                        "align": "center",
                        "flex": 1,
                        "gravity": "center"
                      },
                      {
                        "type": "text",
                        "text": "''' + self.tasks[card_num][i].task_name + '''",
                        "action": {
                          "type": "postback",
                          "label": "''' + self.tasks[card_num][i].task_name + '''",
                          "data": "cat_id=''' + str(self.cat_id[i]) + '''&task_id=''' + str(self.tasks[card_num][i].task_uid) + '''"
                        },
                        "color": "#0080FF",
                        "flex": 3
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
                        "text": "''' + str(self.tasks[card_num][i].finished_persent) + '''%",
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
                                "backgroundColor": "#FF359A",
                                "width": "''' + str(self.tasks[card_num][i].finished_persent) + '''%"
                              }
                            ],
                            "cornerRadius": "10px",
                            "backgroundColor": "#ff95ca",
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
                        "text": "Update: ''' + self.tasks[card_num][i].update + '''",
                        "gravity": "center",
                        "flex": 6,
                        "size": "xs",
                        "color": "#8c8c8c"
                      }
                    ]
                  }
                ],
                "spacing": "lg"
              }'''
            json += tmp
            if i != len(self.tasks[card_num])-1: json += ','
        return json 

    def make_bubble (self):
        json = ''
        for i in range (len(self.cat_id)):
            tmp = '''{
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
                "text": "Card ''' + str(self.cat_id[i]) + '''",
                "color": "#ffffff",
                "size": "xl",
                "weight": "bold"
              },
              {
                "type": "text",
                "text": "send_time: ''' + datetime.now().strftime("%Y/%m/%d %H:%M") + '''",
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
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "''' + self.cat_name[i] + '''",
                "gravity": "center",
                "size": "lg",
                "color": "#A6A6D2"
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [''' + self.make_task_box(i) + '''
            ],
            "spacing": "sm"
          },
          {
            "type": "text",
            "text": "共 ''' + str(len(self.tasks[i])) + ''' 個項目",
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
          "backgroundColor": "''' + self.header_color[i] + '''"
        },
        "body": {
          "backgroundColor": "#ecf5ff"
        }
      }
    }'''
            json += tmp
            if i != len(self.cat_id)-1: json += ','
        return json

    def make_json_data (self):

        data = '''{
  "type": "carousel",
  "contents": [''' + self.make_bubble() + '''
  ]
}'''
        return data
