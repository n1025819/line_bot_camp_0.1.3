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
    alt_text = '?üÂú∞?úÂ?',
    template = ButtonsTemplate(
        title = '?üÂú∞?úÂ?',
        text = 'Ë´ãÈÅ∏?áÂú∞?ñÊ?Â∞ãorÊ¢ù‰ª∂?úÂ???,
        actions = [
          {
            "type": "uri",
            "label": "?∞Â??úÂ?",
            "uri": "https://is.gd/9yCgXX"
          },{
            "type": "postback",
            "label": "Ê¢ù‰ª∂?úÂ?",
            "text": "[::text:]Ê¢ù‰ª∂?úÂ?",
            "data": "Ë≥áÊ? 2"
          }
        ]
    )
)

from linebot.models import (
    ImagemapArea, BaseSize, URIImagemapAction, MessageImagemapAction,ImagemapSendMessage
)

camp_search_imagemap_message = ImagemapSendMessage(
    base_url='https://is.gd/VKXD9X',
    alt_text='?∏Ê?È°ûÂ?',
    base_size=BaseSize(height=1473,width=1040)
     ,actions=[
        MessageImagemapAction(
            text="[::text:]Ë¶™Â??åÊ?",
            area=ImagemapArea(x=7,y=271,width=513,height=128)
        ),
         MessageImagemapAction(
            text="[::text:]?ÉÂ??©Ê?",
            area=ImagemapArea(x=5,y=404,width=513,height=132)
        ),
         MessageImagemapAction(
            text="[::text:]ËßÄË≥ûÁ???,
            area=ImagemapArea(x=4,y=540,width=513,height=132)
        )
        
    ]
)


from linebot.models import (
    ImagemapArea, BaseSize, URIImagemapAction, MessageImagemapAction,ImagemapSendMessage
)

imagemap_message = ImagemapSendMessage(
    base_url='https://is.gd/ZzkWiv',
    alt_text='?∏Ê??Ä??,
    base_size=BaseSize(height=1364,width=1040)
     ,actions=[
        MessageImagemapAction(
            text="[::text:]?óÈÉ®?∞Â?",
            area=ImagemapArea(
                x=271,y=152,width=653,height=262
            )
        ),
         MessageImagemapAction(
            text="[::text:]‰∏≠ÈÉ®?∞Â?",
            area=ImagemapArea(
                x=45, y=426,width=598,height=366
            )
        ),
         MessageImagemapAction(
            text="[::text:]?óÈÉ®?∞Â?",
            area=ImagemapArea(
               x=16, y=812,width=504,height=511
            )
        ),
         MessageImagemapAction(
            text="[::text:]?±ÈÉ®?∞Â?",
            area=ImagemapArea(
                x=648, y=562,width=390,height=733
            )
        )
        
    ]
) 


