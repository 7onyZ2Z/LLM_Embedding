import http.client
import json

def get_embedding(input_text, api_key):
    """
    调用 OpenAI 的 embedding 模型获取文本的 embedding。
    :param input_text: 输入文本
    :param api_key: OpenAI API 密钥
    :return: embedding 结果
    """
    conn = http.client.HTTPSConnection("yunwu.ai")
    payload = json.dumps({
        "model": "text-embedding-3-small",
        "input": input_text
    })
    headers = {
        'Authorization': api_key,
        'Content-Type': 'application/json'
    }
    try:
        conn.request("POST", "/v1/embeddings", payload, headers)
        res = conn.getresponse()
        data = res.read()
        # print(data)
        return json.loads(data.decode("utf-8"))
    except Exception as e:
        print(f"调用模型时发生错误: {e}")
        return None