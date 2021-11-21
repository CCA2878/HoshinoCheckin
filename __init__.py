import requests
import time
import datetime
import os
import json

import hoshino
from hoshino.typing import CommandSession, CQHttpError
from hoshino import Service, priv
from hoshino import aiorequests
from hoshino.service import sucmd

checkinStr = '今日已打卡'






sv = Service(
    name = 'HoshinoCheckin',
    use_priv = priv.NORMAL,
    manage_priv = priv.ADMIN,
    enable_on_default = False,
    visible = True,
    help_ = 'Help先摸了',
    bundle = '通用'
)

bot = sv.bot()

# #管理
# @sucmd('checkinSet', aliases = ('打卡设置', '打卡选项'))
# async def checkinSet(session: CommandSession):
#     msg = session.current_arg'


@bot.on_message('private')
async def msgPrivate(ctx):
    type = ctx["sub_type"] # 事件子类型，依 detail_type 不同而不同，以 message.private 为例，有 friend、group、discuss、other 等。
    sid = int(ctx["self_id"]) # 机器人自身ID
    uid = int(ctx["sender"]["user_id"]) # 消息发送者ID
    if checkinStr in str(ctx['message']):
        
