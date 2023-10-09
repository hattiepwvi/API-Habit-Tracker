import requests
# 1、Post request: Create a User
    # token 就像是 API key, pixela 家的token 是自己编 [ -~]{8,128}; id 自己编的规则 ^[a-z][a-z0-9-]{1,16}
    # 发送的是 json data (string: string)
    # text 查看是否成功

USERNAME = "eta"
TOKEN = "suibianbiangejiuola"
ID = "suibianbiangejiuola"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# 2、Post Request: Create a Graph
   # HTTP header: 确保 API key 在 log 中不被别人看到（不用 HTTP header 的话幸好还是有 HTTPS 的 S 给它加密 encrypted, 但是别人可以在你浏览器上安装什么东西来偷窥）；header 类似于写信的信头, body 类似于正文
      # kwargs 或关键字参数之一：不会像 JSON 或者 URL 一样输入的时候显示出来
   # https://pixe.la/v1/users/eta/graphs/graph1.html

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": ID,
    "name": "Builder Graph",
    "unit": "Dora",
    "type": "int",
    "color": "sora",

}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# 3、Post Request: Post a pixel

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"

pixel_config = {
    "date": "20231009",
    "quantity": "10",
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)