import zhipuai
from http import HTTPStatus
import wenxin_get_access_token
import dashscope
from dotenv import load_dotenv
from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage
import zhuanhuan
from openai import OpenAI
import requests
import time
import hashlib
import json
from volcenginesdkarkruntime import Ark

clientark = Ark(ak="*",
                sk="*")

client = OpenAI(
    api_key="*",
    base_url="https://api.moonshot.cn/v1",
)
dashscope.api_key = "*"
load_dotenv()
spark = ChatSparkLLM(
    spark_api_url="wss://spark-api.xf-yun.com/v3.5/chat",
    spark_app_id="*",
    spark_api_key="*",
    spark_api_secret="*",
    spark_llm_domain="generalv3.5",
    streaming=False,
)
chat = zhipuai.ZhipuAI(api_key="*")
lis_tongyi = []
lis_wenxin = []
lis_xunfei = []
lis_zhipu = []
lis_moonshot = []
lis_tiangong = []
lis_huoshan = []

url = 'https://api-maas.singularity-ai.com/sky-work/api/v1/chat'
app_key = '*'
app_secret = '*'
timestamp = str(int(time.time()))
sign_content = app_key + app_secret + timestamp
sign_result = hashlib.md5(sign_content.encode('utf-8')).hexdigest()


def call_with_messages_with_kimi(inputcontent):
    global lis_moonshot
    print("正在思考中……", end="")
    messages1 = [{"role": 'system',
                  "content": '你是一个助手，输出中禁止出现违法内容，一定要非常非常非常简短，不准超过400字'}] + lis_moonshot + [
                    {"role": "user", "content": inputcontent}]
    lis_moonshot.append({"role": "user", "content": inputcontent})
    response = client.chat.completions.create(
        model="moonshot-v1-8k",
        messages=messages1,
        temperature=0.3)

    print("\r" + (response.choices[0].message.content))
    lis_moonshot.append({"role": "assistant", "content": response.choices[0].message.content})
    if len(lis_moonshot) >= 16:
        lis_moonshot = lis_moonshot[2:]


def call_with_messages_with_xinhuo(inputcontent):
    global lis_xunfei
    print("正在思考中……", end="")
    messages = [ChatMessage(role='system',
                            content='你是一个助手，输出中禁止出现违法内容，一定要非常非常非常简短，不准超过400字'),
                ] + lis_xunfei + [ChatMessage(role='user', content=inputcontent)]
    lis_xunfei.append(ChatMessage(role="user", content=inputcontent))
    handler = ChunkPrintHandler()
    a = spark.generate([messages], callbacks=[handler])
    try:
        print("\r" + a.generations[0][0].message.content)
        lis_xunfei.append(ChatMessage(role="assistant", content=a.generations[0][0].message.content))
    except:
        print("\r出错了", a)
        lis_xunfei.pop()
    if len(lis_xunfei) >= 8:
        lis_xunfei = lis_xunfei[2:]


def call_with_messages_with_qwen(inputcontent):
    global lis_tongyi
    print("正在思考中……", end="")
    messages1 = [{"role": 'system',
                  "content": '你是一个助手，输出中禁止出现违法内容，一定要非常非常非常简短，不准超过400字'}] + lis_tongyi + [
                    {"role": "user", "content": inputcontent}]
    lis_tongyi.append({"role": "user", "content": inputcontent})
    response = dashscope.Generation.call(
        "qwen2-7b-instruct",
        messages=messages1,
        result_format='message',  # set the result to be "message" format.
    )
    if response.status_code == HTTPStatus.OK:
        print("\r" + response["output"]["choices"][0]["message"]["content"])
        lis_tongyi.append({"role": "assistant", "content": response["output"]["choices"][0]["message"]["content"]})
    else:
        print("\r出错了", response)
        lis_tongyi.pop()
    if len(lis_tongyi) >= 16:
        lis_tongyi = lis_tongyi[2:]


def call_with_messages_with_ernie(inputcontent):
    global lis_wenxin
    print("正在思考中……", end="")
    messages = [{"role": 'user', "content": '你是一个助手，输出中禁止出现违法内容，一定要非常非常非常简短，不准超过400字'},
                {"role": "assistant",
                 "content": '好的，我会尽量输出简短且不涉及违法内容的信息。请问有什么我可以帮助您的吗？'}] + lis_wenxin + [
                   {'role': 'user', 'content': inputcontent}]
    lis_wenxin.append({"role": "user", "content": inputcontent})
    urlb = ("https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-3.5-8k-0205?access_token=" +
           wenxin_get_access_token.get_access_token())

    payload = json.dumps({
        "messages": messages
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", urlb, headers=headers, data=payload)
    if response.status_code == HTTPStatus.OK:
        print("\r" + eval("True".join("False".join(response.text.split("false")).split("true")))["result"])
        lis_wenxin.append({"role": "assistant",
                           "content": eval("True".join("False".join(response.text.split("false")).split("true")))[
                               "result"]})
    else:
        print("\r出错了", response)
        lis_wenxin.pop()
    if len(lis_wenxin) >= 8:
        lis_wenxin = lis_wenxin[2:]


def call_with_messages_with_glm4(inputcontent):
    global lis_zhipu
    print("正在思考中……", end="")
    messages1 = [{"role": 'system',
                  "content": '你是一个助手，输出中禁止出现违法内容，一定要非常非常非常简短，不准超过400字'}] + lis_zhipu + [
                    {"role": "user", "content": inputcontent}]
    lis_zhipu.append({"role": "user", "content": inputcontent})
    response = chat.chat.completions.create(
        model="glm-4",
        messages=messages1
    )
    print("\r" + (response.choices[0].message.content))
    lis_zhipu.append({"role": "assistant", "content": response.choices[0].message.content})
    if len(lis_zhipu) >= 16:
        lis_zhipu = lis_zhipu[2:]


def call_with_messages_with_sky_chat(inputcontent):
    global lis_tiangong
    print("正在思考中……", end="")
    messages1 = [{"role": 'system',
                  "content": '你是一个助手，输出中禁止出现违法内容，一定要非常非常非常简短，不准超过400字'}] + lis_tiangong + [
                    {"role": "user", "content": inputcontent}]
    lis_tiangong.append({"role": "user", "content": inputcontent})
    # -*- coding: utf-8 -*-

    # 设置请求头，请求的数据格式为json
    headers = {
        "app_key": app_key,
        "timestamp": timestamp,
        "sign": sign_result,
        "Content-Type": "application/json",
    }

    # 设置请求URL和参数
    data = {
        "messages": messages1,
        "intent": "chat"
    }

    # 发起请求并获取响应
    response = requests.post(url, headers=headers, json=data, stream=False)
    if response.status_code == HTTPStatus.OK:
        h = ""
        for line in response.iter_lines():
            if line:
                if line.decode('utf-8') == "data: ":
                    continue
                try:
                    if eval(line.decode('utf-8')[6:])["type"] == "2":
                        continue
                except:
                    continue

                # 处理接收到的数据
                h += (eval(line.decode('utf-8')[6:])["arguments"][0]["messages"][0]["text"])
        print("\r" + h)
        lis_tiangong.append({"role": "bot", "content": h})
    else:
        print("\r出错了", response)
        lis_tiangong.pop()
    if len(lis_tiangong) >= 16:
        lis_tiangong = lis_tiangong[2:]


def call_with_messages_with_doubao(inputcontent):
    global lis_huoshan
    print("正在思考中……", end="")
    messages1 = [{"role": 'system',
                  "content": '你是一个助手，输出中禁止出现违法内容，一定要非常非常非常简短，不准超过400字'}] + lis_huoshan + [
                    {"role": "user", "content": inputcontent}]
    lis_huoshan.append({"role": "user", "content": inputcontent})
    response = clientark.chat.completions.create(
        model="ep-20240623034404-5qnqv",
        messages=messages1)
    print("\r" + response.choices[0].message.content)
    lis_huoshan.append({"role": "assistant", "content": response.choices[0].message.content})

    if len(lis_huoshan) >= 16:
        lis_huoshan = lis_huoshan[2:]


if __name__ == '__main__':
    while True:
        inp = input("说什么:")
        if ":wq" == inp or "退出" == inp or "exit" == inp or "quit" == inp:
            break
        if len(inp) > 100:
            print("哟，写小作文了，再写短一点！")
            continue
        model = input("请选择模型：1.通义千问、2.文心一言、3.讯飞星火、4.智谱清言、5.Kimi、6.天工、7.豆包:")
        if model == "通义千问" or model == "1":
            call_with_messages_with_qwen(inp)
            lis_wenxin = zhuanhuan.t_to_w(lis_tongyi)
            lis_xunfei = zhuanhuan.t_to_x(lis_tongyi)
            lis_zhipu = zhuanhuan.t_to_z(lis_tongyi)
            lis_moonshot = zhuanhuan.t_to_k(lis_tongyi)
            lis_tiangong = zhuanhuan.t_to_g(lis_tongyi)
        elif model == "文心一言" or model == "2":
            call_with_messages_with_ernie(inp)
            lis_tongyi = zhuanhuan.w_to_t(lis_wenxin)
            lis_xunfei = zhuanhuan.w_to_x(lis_wenxin)
            lis_zhipu = zhuanhuan.w_to_z(lis_wenxin)
            lis_moonshot = zhuanhuan.w_to_k(lis_wenxin)
            lis_tiangong = zhuanhuan.w_to_g(lis_wenxin)
        elif model == "讯飞星火" or model == "3":
            call_with_messages_with_xinhuo(inp)
            lis_wenxin = zhuanhuan.x_to_w(lis_xunfei)
            lis_tongyi = zhuanhuan.x_to_t(lis_xunfei)
            lis_zhipu = zhuanhuan.x_to_z(lis_xunfei)
            lis_moonshot = zhuanhuan.x_to_k(lis_xunfei)
            lis_tiangong = zhuanhuan.x_to_g(lis_xunfei)
            lis_huoshan = zhuanhuan.x_to_h(lis_xunfei)

        elif model == "智谱清言" or model == "4":
            call_with_messages_with_glm4(inp)
            lis_wenxin = zhuanhuan.z_to_w(lis_zhipu)
            lis_tongyi = zhuanhuan.z_to_t(lis_zhipu)
            lis_xunfei = zhuanhuan.z_to_x(lis_zhipu)
            lis_moonshot = zhuanhuan.z_to_k(lis_zhipu)
            lis_tiangong = zhuanhuan.z_to_g(lis_zhipu)
            lis_huoshan = zhuanhuan.z_to_h(lis_zhipu)
        elif model == "Kimi" or model == "5":
            call_with_messages_with_kimi(inp)
            lis_wenxin = zhuanhuan.k_to_w(lis_moonshot)
            lis_tongyi = zhuanhuan.k_to_t(lis_moonshot)
            lis_xunfei = zhuanhuan.k_to_x(lis_moonshot)
            lis_zhipu = zhuanhuan.k_to_z(lis_moonshot)
            lis_tiangong = zhuanhuan.k_to_g(lis_moonshot)
            lis_huoshan = zhuanhuan.k_to_h(lis_moonshot)
        elif model == "天工" or model == "6":
            call_with_messages_with_sky_chat(inp)
            lis_wenxin = zhuanhuan.g_to_w(lis_tiangong)
            lis_tongyi = zhuanhuan.g_to_t(lis_tiangong)
            lis_xunfei = zhuanhuan.g_to_x(lis_tiangong)
            lis_zhipu = zhuanhuan.g_to_z(lis_tiangong)
            lis_moonshot = zhuanhuan.g_to_k(lis_tiangong)
            lis_huoshan = zhuanhuan.g_to_h(lis_tiangong)
        elif model == "豆包" or model == "7":
            call_with_messages_with_doubao(inp)
            lis_wenxin = zhuanhuan.h_to_w(lis_huoshan)
            lis_tongyi = zhuanhuan.h_to_t(lis_huoshan)
            lis_xunfei = zhuanhuan.h_to_x(lis_huoshan)
            lis_zhipu = zhuanhuan.h_to_z(lis_huoshan)
            lis_moonshot = zhuanhuan.h_to_k(lis_huoshan)
            lis_tiangong = zhuanhuan.h_to_g(lis_huoshan)
        else:
            print("暂不支持此模型")
            continue
    print("感谢使用")
