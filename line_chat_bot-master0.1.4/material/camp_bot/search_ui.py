#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from linebot.models import (
    TemplateSendMessage,
    CarouselTemplate, CarouselColumn,
    PostbackTemplateAction, MessageTemplateAction, URIAction,URITemplateAction
)


from linebot.models.template import(
    ButtonsTemplate
)
camp_search_buttons_template_message = TemplateSendMessage(
    alt_text = '?�地?��?',
    template = ButtonsTemplate(
        title = '?�地?��?',
        text = '請選?�地?��?尋or條件?��???,
        actions = [
          {
            "type": "uri",
            "label": "?��??��?",
            "uri": "https://is.gd/9yCgXX"
          },{
            "type": "postback",
            "label": "條件?��?",
            "text": "[::text:]條件?��?",
            "data": "資�? 2"
          }
        ]
    )
)

from linebot.models import (
    ImagemapArea, BaseSize, URIImagemapAction, MessageImagemapAction,ImagemapSendMessage
)

camp_search_imagemap_message = ImagemapSendMessage(
    base_url='https://is.gd/VKXD9X',
    alt_text='?��?類�?',
    base_size=BaseSize(height=1473,width=1040)
     ,actions=[
        MessageImagemapAction(
            text="[::text:]親�??��?",
            area=ImagemapArea(x=7,y=271,width=513,height=128)
        ),
         MessageImagemapAction(
            text="[::text:]?��??��?",
            area=ImagemapArea(x=5,y=404,width=513,height=132)
        ),
         MessageImagemapAction(
            text="[::text:]觀賞�???,
            area=ImagemapArea(x=4,y=540,width=513,height=132)
        )
        
    ]
)


from linebot.models import (
    ImagemapArea, BaseSize, URIImagemapAction, MessageImagemapAction,ImagemapSendMessage
)

imagemap_message = ImagemapSendMessage(
    base_url='https://is.gd/ZzkWiv',
    alt_text='?��??�??,
    base_size=BaseSize(height=1364,width=1040)
     ,actions=[
        MessageImagemapAction(
            text="[::text:]?�部?��?",
            area=ImagemapArea(
                x=271,y=152,width=653,height=262
            )
        ),
         MessageImagemapAction(
            text="[::text:]中部?��?",
            area=ImagemapArea(
                x=45, y=426,width=598,height=366
            )
        ),
         MessageImagemapAction(
            text="[::text:]?�部?��?",
            area=ImagemapArea(
               x=16, y=812,width=504,height=511
            )
        ),
         MessageImagemapAction(
            text="[::text:]?�部?��?",
            area=ImagemapArea(
                x=648, y=562,width=390,height=733
            )
        )
        
    ]
) 


