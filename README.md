# autosearch-grammarly-premium-cookie
免费白嫖使用Grammarly Premium高级版

> 如果运行完显示“cookie均已失效”，**过段时间再运行**就可以了！可能几分钟、几小时、几天。

- 文字教程：[【教程】5步免费白嫖使用Grammarly Premium高级版 [附脚本]](https://blog.csdn.net/sxf1061700625/article/details/128376313)    

- 视频教程：[5步白嫖免费使用Grammarly Premium高级版[附软件]](https://www.bilibili.com/video/BV1z3411d7C1/)    

- 网页版/通知订阅：http://xfxuezhang.cn/web/grammarly/

目前就爬取了3个网站，大家可以自行添加其他网站：
- linkstricks
- trytechnical
- infokik

![image](https://user-images.githubusercontent.com/31002981/208591934-018d710b-c2ea-40c0-a02f-bc1333099e52.png)

**服务器版**适合挂在服务器上运行，把里面的python在服务器上运行，会定时抓取有效的Cookie。然后搭配网页显示Cookie，就可以方便的使用Cookie了。    

服务器版示例网站：[http://xfxuezhang.cn/web/grammarly/](http://xfxuezhang.cn/web/grammarly/)    

![image](https://user-images.githubusercontent.com/31002981/213758853-5887d4a9-de8f-4dff-8fa7-9b072997cbce.png)



---

## 用法

-   环境安装：

```python
conda create -n grammarly python=3.9
conda activate grammarly
pip install -r requirements.txt
```

-   运行脚本：

```python
python search_grammarly_cookie.py
```

-   打包脚本：

```python
pyinstaller -F -i icon.ico search_grammarly_cookie.py
```





## TODO：

-   多线程化
-   爬取更多网站
