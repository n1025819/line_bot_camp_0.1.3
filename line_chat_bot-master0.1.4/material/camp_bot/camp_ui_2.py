#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import json
from linebot.models import (
    ImageCarouselTemplate,PostbackTemplateAction,
    ImageCarouselColumn,TemplateSendMessage
)

secretFileContentJson=json.load(open("./line_secret_key",'r'))
server_url = secretFileContentJson.get("server_url")

survey_carousel_template_message1 = TemplateSendMessage(
    alt_text='ImageCarousel template',
    template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url='https://%s/images/like1.jpg' % server_url,
                action=PostbackTemplateAction(
                    label='喜歡請按我',
                    data='survey_like=購物'
                )
            ),
            ImageCarouselColumn(
                image_url='https://%s/images/like2.jpg' % server_url,
                action=PostbackTemplateAction(
                    label='喜歡請按我',
                    data='survey_like=雲海'
                )
            ),
            ImageCarouselColumn(
                image_url='https://%s/images/like3.jpg' % server_url,
                action=PostbackTemplateAction(
                    label='喜歡請按我',
                    data='survey_like=螢火蟲'
                )
            ),
            ImageCarouselColumn(
                image_url='https://%s/images/like4.jpg' % server_url,
                action=PostbackTemplateAction(
                    label='喜歡請按我',
                    data='survey_like=沙坑'
                )
            ),
            ImageCarouselColumn(
                image_url='https://%s/images/like5.jpg' % server_url,
                action=PostbackTemplateAction(
                    label='喜歡請按我',
                    data='survey_like=落雨松'
                )
            ),
            ImageCarouselColumn(
                image_url='https://%s/images/like6.jpg' % server_url,
                action=PostbackTemplateAction(
                    label='喜歡請按我',
                    data='survey_like=美食'
                )
            ),
            ImageCarouselColumn(
                image_url='https://%s/images/like7.jpg' % server_url,
                action=PostbackTemplateAction(
                    label='喜歡請按我',
                    data='survey_like=櫻花'
                )
            ),
            ImageCarouselColumn(
                image_url='https://%s/images/like8.jpg' % server_url,
                action=PostbackTemplateAction(
                    label='喜歡請按我',
                    data='survey_like=小溪'
                )
            ),
            ImageCarouselColumn(
                image_url='https://%s/images/like9.jpg' % server_url,
                action=PostbackTemplateAction(
                    label='喜歡請按我',
                    data='survey_like=油桐花'
                )
            ),
            ImageCarouselColumn(
                image_url='https://%s/images/like10.jpg' % server_url,
                action=PostbackTemplateAction(
                    label='喜歡請按我',
                    data='survey_like=海景'
                )
            )
        ]
    )
)
survey_carousel_template_message2 = TemplateSendMessage(
    alt_text='ImageCarousel template',
    template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url='https://%s/images/like11.jpg' % server_url,
                action=PostbackTemplateAction(
                    label='喜歡請按我',
                    data='survey_like=山景'
                )
            ),
            ImageCarouselColumn(
                image_url='https://%s/images/like12.jpg' % server_url,
                action=PostbackTemplateAction(
                    label='喜歡請按我',
                    data='survey_like=溜滑梯'
                )
            ),
            ImageCarouselColumn(
                image_url='https://%s/images/like13.jpg' % server_url,
                action=PostbackTemplateAction(
                    label='喜歡請按我',
                    data='survey_like=古道'
                )
            ),
            ImageCarouselColumn(
                image_url='https://%s/images/like14.jpg' % server_url,
                action=PostbackTemplateAction(
                    label='喜歡請按我',
                    data='survey_like=湖景'
                )
            ),
            ImageCarouselColumn(
                image_url='https://%s/images/like15.jpg' % server_url,
                action=PostbackTemplateAction(
                    label='喜歡請按我',
                    data='survey_like=昆蟲'
                )
            ),
            ImageCarouselColumn(
                image_url='https://%s/images/like16.jpg' % server_url,
                action=PostbackTemplateAction(
                    label='喜歡請按我',
                    data='survey_like=遮雨棚'
                )
            ),
            ImageCarouselColumn(
                image_url='https://%s/images/like17.jpg' % server_url,
                action=PostbackTemplateAction(
                    label='喜歡請按我',
                    data='survey_like=高海拔'
                )
            ),
            ImageCarouselColumn(
                image_url='https://%s/images/like18.jpg' % server_url,
                action=PostbackTemplateAction(
                    label='喜歡請按我',
                    data='survey_like=星空'
                )
            ),
            ImageCarouselColumn(
                image_url='https://%s/images/like19.jpg' % server_url,
                action=PostbackTemplateAction(
                    label='喜歡請按我',
                    data='survey_like=老街'
                )
            ),
            ImageCarouselColumn(
                image_url='https://%s/images/like20.jpg' % server_url,
                action=PostbackTemplateAction(
                    label='喜歡請按我',
                    data='survey_like=水池'
                )
            )
        ]
    )
)

