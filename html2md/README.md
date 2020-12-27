# 项目介绍
自己在做笔记的时候，经常看到网上一些别人的言论又华丽又呼哨，想直接粘贴复制又因为太长导致格式出现误差，这个时候就需要一个小工具来自动完成该功能。
# 启动
1. pip install html2text
2. 运行 ：main 方法
#### 说明
目前方法为读取本地html，如果想要改为请求链接，则需要修改读取源：
```
 file_path = r'youhua.html'
    htmlfile = open(file_path, 'r', encoding='UTF-8')
    htmlpage = htmlfile.read()
```
============================>
```
   r=request.get(**)
   htmlpage=r.text 
```