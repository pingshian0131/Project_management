import json

class bubble_json ():
    def __init__(self, **kwargs):
        print(kwargs)
        self.pic = kwargs['pic']
        self.title = kwargs['title']
        self.cat = kwargs['cat']
        self.desc = kwargs['desc']
        self.is_finished = kwargs['is_finished']  ### DataType = list
        self.dates = kwargs['dates']  ### DataType = list
        self.steps = kwargs['steps']  ### DataType = list
        self.color = ['#FFFFFF','#F9F900']
        count = 0
        total = len(kwargs['is_finished'])
        for i in range (total):
            count += int(kwargs['is_finished'][i])
        self.finished_persent = str(count/total*100) + '%'
    def make_line (self, color_type):
        json = '''
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "filler"
                          }
                        ],
                        "cornerRadius": "20px",
                        "borderWidth": "2px",
                        "borderColor": "''' + self.color[color_type] + '''",
                        "width": "2px"
                      },
                      {
                        "type": "filler",
                        "flex": 3
                      }
                    ],
                    "flex": 1
                  }'''
        return json

    def make_circle (self, color_type):
        json = '''
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "filler"
                          }
                        ],
                        "cornerRadius": "20px",
                        "height": "10px",
                        "width": "10px",
                        "borderColor": "''' + self.color[color_type] + '''",
                        "borderWidth": "2px"
                      },
                      {
                        "type": "filler",
                        "flex": 3
                      }
                    ]
                  }'''
        return json

    def make_timeline_box (self):

        json = ''
        json += self.make_line (1)
        json += ','
        for i in range (len(self.dates)):
            json += self.make_circle (self.is_finished[i])
            json += ','
            json += self.make_line (self.is_finished[i])
            if i != (len(self.dates)-1): json += ','
        return json 

    def make_steps_box (self):
        json = ''
        for i in range (len(self.steps)):
            #### if self.is_finished == 1: color = #F9F900
            #### else: color = #ffffff 
            tmp = '''
                  {
                    "type": "text",
                    "text": "''' + self.steps[i] + '''",
                    "color": "''' + self.color[self.is_finished[i]] + '''",
                    "size": "sm",
                    "wrap": true,
                    "flex": 1
                  }'''
            json += tmp
            json += ','
        return json

    def make_dates_box (self):
        json = ''
        for i in range (len(self.dates)):
            #### if self.is_finished == 1: color = #F9F900
            #### else: color = #ffffff 
            tmp = '''
                  {
                    "type": "text",
                    "text": "''' + self.dates[i] + '''",
                    "color": "''' + self.color[self.is_finished[i]] + '''",
                    "size": "sm",
                    "align": "start",
                    "flex": 1
                  }'''
            json += tmp
            json += ','
        return json

    def make_json_data (self):
        first = '''{
  "type": "bubble",
  "size": "mega",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "''' + self.pic + '''",
            "size": "full",
            "aspectMode": "cover"
          }
        ],
        "backgroundColor": "#ff0000",
        "height": "200px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
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
                    "text": "''' + self.cat + '''",
                    "color": "#ffffff",
                    "align": "end",
                    "size": "md",
                    "gravity": "center"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    "text": "''' + self.title + '''",
                    "color": "#ffffff",
                    "align": "start",
                    "size": "md",
                    "gravity": "center"
                  }
                ]
              },
              {
                "type": "text",
                "text": "''' + self.desc + '''",
                "color": "#f0f0f0",
                "size": "sm",
                "wrap": true
              },
              {
                "type": "text",
                "text": "''' + self.finished_persent + '''",
                "color": "#ffffff",
                "align": "end",
                "size": "xs",
                "gravity": "center"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "filler"
                      }
                    ],
                    "width": "'''+ self.finished_persent +'''",
                    "height": "10px",
                    "backgroundColor": "#ffd2d2"
                  }
                ],
                "backgroundColor": "#ffffff",
                "height": "10px",
                "margin": "sm",
                "cornerRadius": "10px"
              }
            ],
            "spacing": "md"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "filler",
                "flex": 1
              },
              {
                "type": "text",
                "text": "Time Line",
                "color": "#ffffff",
                "flex": 3
              },
              {
                "type": "filler",
                "flex": 3
              }
            ]
          },'''
        dates = '''
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },''' + self.make_dates_box() + '''
                  {
                    "type": "filler"
                  }
                ],
                "spacing": "sm",
                "flex": 2
              },'''
        timeline = '''
              {
                "type": "box",
                "layout": "vertical",
                "contents": [''' + self.make_timeline_box() + '''
                ],
                "flex": 4
              },'''
        steps = '''
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },''' + self.make_steps_box() + '''
                  {
                    "type": "filler"
                  }
                ],
                "flex": 2,
                "spacing": "sm"
              }
            ],
            "height": "150px"
          }'''
        last = '''
        ],
        "flex": 1,
        "backgroundColor": "#97cbff",
        "spacing": "md",
        "paddingAll": "20px"
      }
    ],
    "paddingAll": "0px"
  },
  "styles": {
    "footer": {
      "separator": false
    }
  }
}'''
        return first + dates + timeline + steps + last
