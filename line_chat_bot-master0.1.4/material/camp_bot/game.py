#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#小遊戲imagemap
from linebot.models import (
    ImagemapArea, BaseSize, URIImagemapAction, MessageImagemapAction,ImagemapSendMessage
)

game_imagemap_message = ImagemapSendMessage(
    base_url='https://is.gd/b6IhTz',
    alt_text='小遊戲',
    base_size=BaseSize(height=624,width=1040)
     ,actions=[
        URIImagemapAction(
            link_uri="https://play.famobi.com/surfer-archers",
            area=ImagemapArea(x=4,y=4,width=341,height=312)
        ),
         URIImagemapAction(
            link_uri="https://play.famobi.com/highway-rider-extreme",
            area=ImagemapArea(x=347,y=0,width=341,height=312)
        ),
         URIImagemapAction(
            link_uri="https://play.famobi.com/high-hills",
            area=ImagemapArea(x=699,y=0,width=341,height=312)
        ),
         URIImagemapAction(
            link_uri="https://play.famobi.com/pizza-ninja-3",
            area=ImagemapArea(x=5,y=312,width=341,height=312)
        ),
         URIImagemapAction(
            link_uri="https://play.famobi.com/billiard-blitz-challenge",
            area=ImagemapArea(x=349,y=312,width=341,height=312)
        ),
         URIImagemapAction(
            link_uri="https://play.famobi.com/angry-flappy-wings",
            area=ImagemapArea(x=692,y=312,width=341,height=312)
        )
        
    ]
) 

