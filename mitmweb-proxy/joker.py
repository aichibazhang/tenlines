from mitmproxy import http


class Joker:
    def request(self, flow: http.HTTPFlow) -> None:
        # 需要被代理的远程服务地址及被代理的路由地址
        # if flow.request.url.startswith("http://172.18.30.61:9093/tps/web/mgr"):
        if flow.request.url.startswith("https://www.diaosi.love:8080"):
            # 设置本地ip端口
            flow.request.host = "127.0.0.1"
            flow.request.port = 8080

addons=[
    Joker()
]
