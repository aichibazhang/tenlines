# 项目介绍
日常开发调试时，我们可以通过将线上的服务定位到内网或者本地服务。比如我们线上的服务器域名为 diaosi.love，而本地服务启动为 127.0.0.1；那么可以将所有域名 diaosi.love 的请求转发到本地服务 127.0.0.1，方便我们调试代码。
# 启动
1. 启动需要安装好 [mitmproxy](https://docs.mitmproxy.org/stable/)
2. 运行 ：`mitmweb -s joker.py`
#### 特别说明

使用 mitmweb 启动失败：端口被占用，找到占用 8080 端口应用修改即可。

![启动失败](https://images.gitbook.cn/0269e710-19d7-11eb-9bca-c9ae1597f687)