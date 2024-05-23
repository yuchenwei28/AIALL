import requests
import json
from http import HTTPStatus
import wenxin_get_access_token
import dashscope
from dotenv import load_dotenv
from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage

import convert

dashscope.api_key = ""
load_dotenv()
spark = ChatSparkLLM(
    spark_api_url="wss://spark-api.xf-yun.com/v3.5/chat",
    spark_app_id="",
    spark_api_key="",
    spark_api_secret="",
    spark_llm_domain="generalv3.5",
    streaming=False,
)
lis_tongyi = []
lis_wenxin = []
lis_xunfei = []


def call_with_messages_with_xinhuo(inputcontent):
    global lis_xunfei
    print("Thinking about it", end="")
    messages = [ChatMessage(role='system', content='You are an assistant, and illegal content is prohibited in the output'),
                ] + lis_xunfei + [ChatMessage(role='user', content=inputcontent)]
    lis_xunfei.append(ChatMessage(role="user", content=inputcontent))
    handler = ChunkPrintHandler()
    a = spark.generate([messages], callbacks=[handler])
    try:
        print("\r" + a.generations[0][0].message.content)
        lis_xunfei.append(ChatMessage(role="assistant", content=a.generations[0][0].message.content))
    except:
        print("\rERROR!", a)
        lis_xunfei.pop()
    if len(lis_xunfei) >= 8:
        lis_xunfei = lis_xunfei[2:]


def call_with_messages_with_qwen(inputcontent):
    global lis_tongyi
    print("Thinking about it", end="")
    messages1 = [{"role": 'system',
                  "content": 'You are an assistant, and illegal content is prohibited in the output'}] + lis_tongyi + [
                    {"role": "user", "content": inputcontent}]
    lis_tongyi.append({"role": "user", "content": inputcontent})
    response = dashscope.Generation.call(
        "qwen1.5-110b-chat",
        messages=messages1,
        result_format='message',
    )
    if response.status_code == HTTPStatus.OK:
        print("\r" + response["output"]["choices"][0]["message"]["content"])
        lis_tongyi.append({"role": "assistant", "content": response["output"]["choices"][0]["message"]["content"]})
    else:
        print("\rERROR!", response)
        lis_tongyi.pop()
    if len(lis_tongyi) >= 16:
        lis_tongyi = lis_tongyi[2:]


def call_with_messages_with_ernie(inputcontent):
    global lis_wenxin
    print("Thinking about it", end="")
    messages = [{"role": 'user', "content": 'You are an assistant, and illegal content is prohibited in the output'},
                {"role": "assistant",
                 "content": 'Of course, as your assistant,'
                            ' I am fully aware of the importance of complying with legal '
                            'regulations and ethical standards. '
                            'My task is to provide you with accurate, '
                            'useful, and appropriate information and assistance within the scope of the law. '
                            'Please feel free to ask me any questions,'
                            ' and I will do my best to answer them to the best '
                            'of my ability and within the legal framework.'}] + lis_wenxin + [
                   {'role': 'user', 'content': inputcontent}]
    lis_wenxin.append({"role": "user", "content": inputcontent})
    url = ("https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-3.5-8k-0205?access_token=" +
           wenxin_get_access_token.get_access_token())

    payload = json.dumps({
        "messages": messages
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == HTTPStatus.OK:
        print("\r" + eval("True".join("False".join(response.text.split("false")).split("true")))["result"])
        lis_wenxin.append({"role": "assistant",
                           "content": eval("True".join("False".join(response.text.split("false")).split("true")))[
                               "result"]})
    else:
        print("\rERROR!", response)
        lis_wenxin.pop()
    if len(lis_wenxin) >= 8:
        lis_wenxin = lis_wenxin[2:]


if __name__ == '__main__':
    while True:
        inp = input("What to say (quit exit)")
        if ":wq" == inp or "退出" == inp or "exit" == inp or "quit" == inp:
            break
        if len(inp) > 100:
            print("Write it shorter!")
            continue
        model = input("model：通义千问(qwen)、文心一言(ernie)、讯飞星火(xinhuo)")
        if model == "qwen":
            call_with_messages_with_qwen(inp)
            lis_wenxin = zhuanhuan.t_to_w(lis_tongyi)
            lis_xunfei = zhuanhuan.t_to_x(lis_tongyi)
        elif model == "ernie":
            call_with_messages_with_ernie(inp)
            lis_tongyi = zhuanhuan.w_to_t(lis_wenxin)
            lis_xunfei = zhuanhuan.w_to_x(lis_wenxin)
        elif model == "xinhuo":
            call_with_messages_with_xinhuo(inp)
            lis_wenxin = zhuanhuan.x_to_w(lis_xunfei)
            lis_tongyi = zhuanhuan.x_to_t(lis_xunfei)
        else:
            print("暂不支持此模型")
            continue
    print("感谢使用")
