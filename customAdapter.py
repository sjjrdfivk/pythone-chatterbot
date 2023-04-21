from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
import random


class CustomAdapter(LogicAdapter):
    def can_process(self, statement):
        return True

    def process(self, input_statement, conversation):
        input_text = input_statement.text

        # 根据输入文本生成回复
        if "你好" in input_text:
            response_text = "你好，我是REX。"
        elif "天气" in input_text:
            response_text = "不提供天气信息。"
        elif "百度" in input_text:
            response_text = "https://www.baidu.com/"
        else:
            # 如果无法处理输入，返回默认回复
            default_responses = ["很抱歉，我无法理解您的意思。",
                                 "我不知道该怎么回答这个问题。",
                                 "对不起，我不能回答这个问题。"]
            response_text = random.choice(default_responses)

        # 返回回复语句
        response = response = Statement(response_text)
        return response