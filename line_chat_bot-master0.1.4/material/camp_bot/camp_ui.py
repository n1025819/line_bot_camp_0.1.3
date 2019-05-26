#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 載入json處理套件
import json

# 載入基礎設定檔
secretFileContentJson=json.load(open("./line_secret_key",'r'))
server_url = secretFileContentJson.get("server_url")



'''
偏好調查(Carousel Flex)
'''


from linebot.models import(
    FlexSendMessage, CarouselContainer
)

survey_flexCarouselContainerJsonDict ="""
{
    "type": "carousel",
    "contents": [
      {
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": "#img_url_001#",
          "size": "full",
          "aspectMode": "fit"
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "text",
              "text": "【 填寫問卷】喜歡的就請按，可重複，推薦請按GO",
              "size": "sm",
              "weight": "bold",
              "wrap": true
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "沙坑(請按我)",
                "data": "survey_like=沙坑"
              },
              "style": "primary"
            },
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "購物(請按我)",
                "data": "survey_like=購物"
              },
              "style": "primary"
            },
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "雲海(請按我)",
                "data": "survey_like=雲海"
              },
              "style": "primary"
            },
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "螢火蟲(請按我)",
                "data": "survey_like=螢火蟲"
              },
              "style": "primary"
            }
          ]
        }
      },{
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": "#img_url_002#",
          "size": "full",
          "aspectMode": "fit"
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "text",
              "text": "【 填寫問卷】喜歡的就請按，可重複，推薦請按GO",
              "size": "sm",
              "weight": "bold",
              "wrap": true
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "落雨松(請按我)",
                "data": "survey_like=落雨松"
              },
              "style": "primary"
            },
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "美食(請按我)",
                "data": "survey_like=美食"
              },
              "style": "primary"
            },
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "小溪(請按我)",
                "data": "survey_like=小溪"
              },
              "style": "primary"
            },
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "櫻花(請按我)",
                "data": "survey_like=櫻花"
              },
              "style": "primary"
            }
          ]
        }
      },{
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": "#img_url_003#",
          "size": "full",
          "aspectMode": "fit"
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "text",
              "text": "【 填寫問卷】喜歡的就請按，可重複，推薦請按GO",
              "size": "sm",
              "weight": "bold",
              "wrap": true
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "溜滑梯(請按我)",
                "data": "survey_like=溜滑梯"
              },
              "style": "primary"
            },
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "山景(請按我)",
                "data": "survey_like=山景"
              },
              "style": "primary"
            },
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "海景(請按我)",
                "data": "survey_like=海景"
              },
              "style": "primary"
            },
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "油桐花(請按我)",
                "data": "survey_like=油桐花"
              },
              "style": "primary"
            }
          ]
        }
      },{
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": "#img_url_004#",
          "size": "full",
          "aspectMode": "fit"
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "text",
              "text": "【 填寫問卷】喜歡的就請按，可重複，推薦請按GO",
              "size": "sm",
              "weight": "bold",
              "wrap": true
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "湖景(請按我)",
                "data": "survey_like=湖景"
              },
              "style": "primary"
            },
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "昆蟲(請按我)",
                "data": "survey_like=昆蟲"
              },
              "style": "primary"
            },
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "遮雨棚(請按我)",
                "data": "survey_like=遮雨棚"
              },
              "style": "primary"
            },
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "古道(請按我)",
                "data": "survey_like=古道"
              },
              "style": "primary"
            }
          ]
        }
      },{
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": "#img_url_005#",
          "size": "full",
          "aspectMode": "fit"
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "text",
              "text": "【 填寫問卷】喜歡的就請按，可重複，推薦請按GO",
              "size": "sm",
              "weight": "bold",
              "wrap": true
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "高海拔(請按我)",
                "data": "survey_like=高海拔"
              },
              "style": "primary"
            },
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "星空(請按我)",
                "data": "survey_like=星空"
              },
              "style": "primary"
            },
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "老街(請按我)",
                "data": "survey_like=老街"
              },
              "style": "primary"
            },
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "水池(請按我)",
                "data": "survey_like=水池"
              },
              "style": "primary"
            }
          ]
        }
      },
      {
        "type": "bubble",
        "direction": "ltr",
        "hero": {
          "type": "image",
          "url": "#img_url_006#",
          "size": "full",
          "aspectMode": "fit"
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "營地推薦",
              "align": "center"
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
           "spacing": "sm",
          "contents": [
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "GO",
                "text": "[::text:]GO",
                "data": "recommend_site"
              },
              "style": "primary"
            },{
              "type": "button",
              "action": {
                "type": "postback",
                "label": "查看點選清單",
                "text": "查看點選清單",
                 "data": "like_site"
              },
              "style": "primary"
            },{
              "type": "button",
              "action": {
                "type": "postback",
                "label": "清空點選清單",
                "text": "清空點選清單",
                "data": "clean_site"
              },
              "style": "primary"
            }
          ]
        }
      }
    ]
}
"""


survey_flexCarouselContainerJsonDict = survey_flexCarouselContainerJsonDict.replace("#img_url_001#", ('https://%s/images/0001.jpg' % server_url))
survey_flexCarouselContainerJsonDict = survey_flexCarouselContainerJsonDict.replace("#img_url_002#", ('https://%s/images/0002.jpg' % server_url))
survey_flexCarouselContainerJsonDict = survey_flexCarouselContainerJsonDict.replace("#img_url_003#", ('https://%s/images/0003.jpg' % server_url))
survey_flexCarouselContainerJsonDict = survey_flexCarouselContainerJsonDict.replace("#img_url_004#", ('https://%s/images/0004.jpg' % server_url))
survey_flexCarouselContainerJsonDict = survey_flexCarouselContainerJsonDict.replace("#img_url_005#", ('https://%s/images/0005.jpg' % server_url))
survey_flexCarouselContainerJsonDict = survey_flexCarouselContainerJsonDict.replace("#img_url_006#", ('https://%s/images/0006.jpg' % server_url))
# print(type(survey_flexCarouselContainerJsonDict))
# print(survey_flexCarouselContainerJsonDict)

'''
將carousel類型的json 進行轉換變成 Python可理解之類型物件
將該物件封裝進 Flex Message中
'''
survey_carouselContent = CarouselContainer.new_from_json_dict(json.loads(survey_flexCarouselContainerJsonDict))
survey_flexCarouselSendMeesage = FlexSendMessage(alt_text="偏好調查", contents=survey_carouselContent)

