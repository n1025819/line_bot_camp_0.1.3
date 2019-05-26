#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 載入json處理套件
import json

# 載入基礎設定檔
secretFileContentJson=json.load(open("./line_secret_key",'r'))
server_url = secretFileContentJson.get("server_url")

'''
食譜推薦
'''

from linebot.models import(
    FlexSendMessage, CarouselContainer
)

survey_flexCarouselContainerJsonDict1 ="""
{
    "type": "carousel",
    "contents": [
          {
        "type": "bubble",
        "direction": "ltr",
        "hero": {
          "type": "image",
          "url": "#img_url_007#",
          "size": "full",
          "aspectMode": "fit"
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "【 填寫問卷】喜歡的就請按，可重複，推薦請按GO",
              "align": "center"
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "horizontal",
          "contents": [
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "豬肉",
                "text": "豬肉",
                "data": "food_like=豬肉"
              },
              "style": "primary"
            },{
              "type": "button",
              "action": {
                "type": "postback",
                "label": "雞肉",
                "text": "雞肉",
                "data": "food_like=雞肉"
              },
              "style": "primary"
            },{
              "type": "button",
              "action": {
                "type": "postback",
                "label": "牛肉",
                "text": "牛肉",
                "data": "food_like=牛肉"
              },
              "style": "primary"
            }
          ]
        }
      },{
        "type": "bubble",
        "direction": "ltr",
        "hero": {
          "type": "image",
          "url": "#img_url_008#",
          "size": "full",
          "aspectMode": "fit"
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "喜歡的就請按，可重複",
              "align": "center"
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "horizontal",
          "contents": [
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "番茄",
                "text": "番茄",
                "data": "food_like=番茄"
              },
              "style": "primary"
            },{
              "type": "button",
              "action": {
                "type": "postback",
                "label": "洋蔥",
                "text": "洋蔥",
                "data": "food_like=洋蔥"
              },
              "style": "primary"
            },{
              "type": "button",
              "action": {
                "type": "postback",
                "label": "紅蘿蔔",
                "text": "紅蘿蔔",
                "data": "food_like=紅蘿蔔"
              },
              "style": "primary"
            }
          ]
        }
      },      {
        "type": "bubble",
        "direction": "ltr",
        "hero": {
          "type": "image",
          "url": "#img_url_009#",
          "size": "full",
          "aspectMode": "fit"
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "喜歡的就請按，可重複",
              "align": "center"
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "horizontal",
          "contents": [
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "菇類",
                "text": "菇類",
                "data": "food_like=菇類"
              },
              "style": "primary"
            },{
              "type": "button",
              "action": {
                "type": "postback",
                "label": "高麗菜",
                "text": "高麗菜",
                "data": "food_like=高麗菜"
              },
              "style": "primary"
            },{
              "type": "button",
              "action": {
                "type": "postback",
                "label": "馬鈴薯",
                "text": "馬鈴薯",
                "data": "food_like=馬鈴薯"
              },
              "style": "primary"
            }
          ]
        }
      }, {
        "type": "bubble",
        "direction": "ltr",
        "hero": {
          "type": "image",
          "url": "#img_url_010#",
          "size": "full",
          "aspectMode": "fit"
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "食譜推薦",
              "align": "center"
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "horizontal",
          "contents": [
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "GO",
                "text": "GO",
                "data": "recommend_food"
              },
              "style": "primary"
            },{
              "type": "button",
              "action": {
                "type": "postback",
                "label": "查看",
                "text": "查看",
                "data": "like_food"
              },
              "style": "primary"
            },{
              "type": "button",
              "action": {
                "type": "postback",
                "label": "清空",
                "text": "清空",
                "data": "recommend_food"
              },
              "style": "primary"
            }
          ]
        }
      }
    
    ]
}
"""

survey_flexCarouselContainerJsonDict1 = survey_flexCarouselContainerJsonDict1.replace("#img_url_007#", ('https://%s/images/0007.jpg' % server_url))
survey_flexCarouselContainerJsonDict1 = survey_flexCarouselContainerJsonDict1.replace("#img_url_008#", ('https://%s/images/0008.jpg' % server_url))
survey_flexCarouselContainerJsonDict1 = survey_flexCarouselContainerJsonDict1.replace("#img_url_009#", ('https://%s/images/0009.jpg' % server_url))
survey_flexCarouselContainerJsonDict1 = survey_flexCarouselContainerJsonDict1.replace("#img_url_010#", ('https://%s/images/0006.jpg' % server_url))
# print(type(survey_flexCarouselContainerJsonDict))
# print(survey_flexCarouselContainerJsonDict)

'''
將carousel類型的json 進行轉換變成 Python可理解之類型物件
將該物件封裝進 Flex Message中
'''
survey_carouselContent1 = CarouselContainer.new_from_json_dict(json.loads(survey_flexCarouselContainerJsonDict1))
survey_flexCarouselSendMeesage1 = FlexSendMessage(alt_text="偏好調查", contents=survey_carouselContent1)

