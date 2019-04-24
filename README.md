# scrapy_sakura1
scrapy爬樱花动漫，保存动漫封面图片和数据



1、创建项目
D:\>scrapy startproject 项目名称

2、目录介绍
spiders 文件夹：存储爬虫文件
settings：进行爬虫相关的配置
items：保存爬取到的数据的容器
pipelines：执行保存数据的操作，例如将items中的数据保存到mysql中
scrapy.cfg:项目的配置文件

3、创建爬虫
D:\code\myscrapyproject>scrapy genspider jobbole blog.jobbole.com

4、执行爬虫
D:\code\myscrapyproject>scrapy crawl jobbole

5、robots.txt
（1）、大部分网站都会定义robots.txt
这个文件就是给‘网络爬虫’了解爬取该网站时存在哪些限制
即该目录下哪些可爬，哪些不可以
（2）、该协议可遵守，可不遵守，良好的网民会遵守
（3）、如何看这个协议：robots.txt都会被放在网络的根目录下
www.baidu.com/robots.txt
(4)、
User-agent: Baiduspider 禁止代理为Googlebot的爬虫爬取该网站
Disallow 禁止访问的网站路径
allow:允许访问的路径
Crawl-delay: 5     秒 不管用户是什么，两次请求间隔时间要大于5秒

ROBOTSTXT_OBEY = False 忽略robots.txt
