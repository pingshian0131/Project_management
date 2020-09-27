import json
from datetime import datetime

class bubble_json ():
    def __init__(self, title, cat_id, remain):
        self.title = title 
        self.cat_id = cat_id 
        self.remain = remain 

    def make_cat_box (self):
        json = ''
        for i in range (len(self.title)):
            tmp = '''
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
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
                  "label": "''' + self.title[i] + '''",
                  "data": "cat_id=''' + str(self.cat_id[i]) + '''"
                },
                "style": "link",
                "height": "sm",
                "flex": 4
              },
              {
                "type": "filler",
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
                "flex": 3
              },
              {
                "type": "text",
                "text": "remain: ''' + str(self.remain[i]) + ''' items",
                "gravity": "center",
                "size": "xs",
                "color": "#8c8c8c",
                "flex": 2
              }
            ]
          }
        ]
      },'''
            json += tmp
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
            "text": "Category_list",
            "color": "#ffffff",
            "size": "xl",
            "weight": "bold"
          },
          {
            "type": "text",
            "text": "send_time: ''' + datetime.now().strftime('%Y/%m/%d/ %H:%M') + '''",
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
    "contents": [''' + self.make_cat_box() + '''
      {
        "type": "text",
        "text": "共 ''' + str(len(self.title)) + ''' 個項目",
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
      "backgroundColor": "#00bb00"
    },
    "body": {
      "backgroundColor": "#f0fff0"
    }
  }
}'''

        return data
