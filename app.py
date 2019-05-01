from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('bOa6YldERV0fFojkZtHxF9VaH6qY+KkE3K60FksWVNri8ZSNUzvwwoFaUCVH56epO+BEnM3EsaTR06mxM1zbP+K7KxgIKkm4e7DLnHTl6TQvRdiDSm5CUENlnqnDAy237endHe7L4MEeBmuRbs0jbQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('f38302aa27ce3b69be8fbf8d6c91c495')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(FollowEvent)
def handle_follow(event):
    default = """Hello! I'm the Intro Bot! 🙂
I can provide you with more information about Erica Huang. 
Use these commands to control me:
⚫ /self-intro
⚫ /education
⚫ /graduate_research
⚫ /internship
⚫ /course_project
⚫ /skills
⚫ /links
⚫ /help
Or you can click the below template and menu."""

    button_template_message =ButtonsTemplate(
        thumbnail_image_url="https://i.imgur.com/opFDSNo.png",
        title='My name is Erica Huang...', 
        text='Click me click, click me! 😆😆😆',
        image_size="cover",
        actions=[
        MessageTemplateAction(
            label='Graduate Research', text='/graduate_research'
        ),
        MessageTemplateAction(
            label='Internship', text='/internship'
        ),
        MessageTemplateAction(
            label='Course Project', text='/course_project'
        ),
        MessageTemplateAction(
            label='Skills', text='/skills'   
        ),
        ]
    )


    rich_menu_to_create = RichMenu(
        size=RichMenuSize(width=2500, height=1686),
        selected=True,
        name="Controller",
        chat_bar_text="Tap here!",
        areas=[RichMenuArea(
            bounds=RichMenuBounds(x=0, y=0, width=2500, height=1686),
            action=URIAction(label='Go to line.me', uri='https://line.me'))]
    )
    rich_menu_id = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)
    rich_menu = line_bot_api.get_rich_menu(rich_menu_id)


    line_bot_api.reply_message(
        event.reply_token,[
        TextSendMessage(text=default),
        TemplateSendMessage(alt_text = "Cannot display",template=button_template_message), 
    ])


# Deal with messages
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    msg = (event.message.text).lower()

    default = """Hello! I'm the Intro Bot! \U0001F604
I can provide you with more information about Erica Huang. 
Use these commands to control me:
⚫ /self-intro
⚫ /education
⚫ /graduate_research
⚫ /internship
⚫ /course_project
⚫ /skills
⚫ /links
⚫ /help
Or you can click the below template and menu."""

    intro = """Hi, my name is Erica Huang.
I'm a graduate student at present.
Currently I'm searching for a position as a software engineer intern, allowing me to utilize my knowledge and skills while gaining valuable work experience in a team-oriented environment.
It's nice to meet you!"""

    edu_1 = """National Taiwan University
2014 - Jun. 2018
Bachelor of Science in Engineering
⚫ ​Major: ​Electrical Engineering
⚫ ​Minor: ​Computer Science & Information Engineering"""

    edu_2 = """National Taiwan University
2018 - Expected Jun. 2020
Ｍaster of Science
⚫ ​Graduate Institute of Communication Engineering"""

    research = """Computer Vision
Sep. 2017 - Present
⚫ ​Work on the research project related to Multimedia Processing and Face Recognition under Prof. Homer H. Chen’s supervision."""

    internship_1 = """Vpon Data Scientist Intern
Aug. 2018 – Present
⚫ ​Develop user behavior predictive models with valuable findings from large-scale demographic datasets, especially in the field of traveling intent related problems gender prediction, and CTR.
⚫ ​Prototype and build machine learning pipelines to accelerate development life cycle
⚫ ​Demonstrate data visualizations with clear presentations of insights and business recommendations
⚫ ​Research machine learning techniques and optimization methods based on multi-source data to improve the quality of DMP product""" 

    internship_2 = """HP Inc. Intern
July. 2017 – July. 2018
⚫ ​Assisted with performance evaluation of SCCM deployment through switches and development of an internal web inventory management system based on Django framework.""" 

    course_project_1 = """Computer Networks & Web Programming 
Jan. 2017
Line-like System Implementation including server and client sides
⚫ Built a messaging system and implemented registration, messaging, file transfer and user interface.
Web Application for Personal Blog and Chat Room
⚫ Built a personal blog and a chat room including frontend and backend web development.""" 

    course_project_2 = """Digital Visual Effects 
June. 2017 
High Dynamic Range Imaging and Image Stitching Algorithms
⚫ Implemented systems of High Dynamic Range and Image Stitching using Microsoft Visual Studio.""" 

    course_project_3 = """Compiler Design 
Sep. 2017 - Jan. 2018 
C-- Compiler
⚫ Implemented a simple yet complete C-- compiler which generates real ISA (Instruction Set Architecture) code such as the ARMv8""" 

    course_project_4 = """Machine Learning and having it deep and structured 
Feb. 2018 - Jun. 2018 
Video Caption Generator & Chatbot & Text-to-Image Generator & Style Transfer system
⚫ Utilized deep learning methods (e.g. Seq2Seq model and GAN) to implement above mentioned systems."""

    course_project_5 = """Cognitive Computing 
Dec. 2018 - Jan. 2019 
Music style transfer system to turn genre of music from classical into jazz or from jazz into classical
⚫ Utilized deep learning methods (ex. Seq2Seq model and CycleGAN) to implement above mentioned systems."""

    link = """Github:
https://github.com/zeroHuang0516"""

    button_template_message =ButtonsTemplate(
        thumbnail_image_url="https://i.imgur.com/opFDSNo.png",
        title='My name is Erica Huang...', 
        text='Click me click, click me! 😆😆😆',
        image_size="cover",
        actions=[
        MessageTemplateAction(
            label='Graduate Research', text='/graduate_research'
        ),
        MessageTemplateAction(
            label='Internship', text='/internship'
        ),
        MessageTemplateAction(
            label='Course Project', text='/course_project'
        ),
        MessageTemplateAction(
            label='Skills', text='/skills'   
        ),
        ]
    )

    if '/self-intro' in msg :
        line_bot_api.reply_message(event.reply_token,[
            TextSendMessage(text=intro),
            StickerSendMessage(package_id=11537, sticker_id=52002739),])

    elif '/education' in msg :
        line_bot_api.reply_message(event.reply_token,[
            TextSendMessage(text=edu_1),
            TextSendMessage(text=edu_2),])

    elif '/graduate_research' in msg :
        line_bot_api.reply_message(event.reply_token,[
            TextSendMessage(text=research),])

    elif '/internship' in msg :
        line_bot_api.reply_message(event.reply_token,[
            ImageSendMessage(
                original_content_url='https://i.imgur.com/0h6ziaA.jpg',
                preview_image_url='https://i.imgur.com/0h6ziaA.jpg'),
            TextSendMessage(text=internship_2),
            ImageSendMessage(
                original_content_url='https://i.imgur.com/7lBrzw2.jpg',
                preview_image_url='https://i.imgur.com/7lBrzw2.jpg'),
            TextSendMessage(text=internship_1),])

    elif '/course_project' in msg :
        line_bot_api.reply_message(event.reply_token,[
            TextSendMessage(text=course_project_1),
            TextSendMessage(text=course_project_2),
            TextSendMessage(text=course_project_3),
            TextSendMessage(text=course_project_4),
            TextSendMessage(text=course_project_5),])

    elif '/skills' in msg :
        line_bot_api.reply_message(event.reply_token,[
            ImageSendMessage(
                original_content_url='https://i.imgur.com/SJw4qE9.png',
                preview_image_url='https://i.imgur.com/SJw4qE9.png'),])

    elif '/links' in msg :
        line_bot_api.reply_message(event.reply_token,[
            TextSendMessage(text=link),])

    else:
        line_bot_api.reply_message(
            event.reply_token,[
            TextSendMessage(text=default),
            TemplateSendMessage(alt_text=default,template=button_template_message), 
        ])

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
