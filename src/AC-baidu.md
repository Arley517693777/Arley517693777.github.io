---
layout: post
title: AC-baidu-重定向优化美化代码分享
slug: AC-baidu
date: 2021-1-15 9:10
status: publish
author: Arley
categories: 
  - 美化
tags: 
  - AC-baidu
  - Tampermonkey
  - 浏览器美化
  - 美化
excerpt: 打造个性化搜索引擎主页!
---

#### 以下代码直接复制粘贴到 附加10-自定义样式

```cpp
/**计数器的颜色样式*/
div .AC-CounterT{
    background: #FD9999;
}
/**右侧栏的样式-其实不开启更好看一些*/
#content_right{
    padding: 20px 15px 15px;
    border-radius: 5px;
    background-color: #fff;
    box-sizing: border-box;
    box-shadow: 0 0 20px 2px rgba(0, 0, 0, .1);
    -webkit-box-shadow: 0 0 20px 2px rgba(0, 0, 0, .1);
    -moz-box-shadow: 0 0 20px 2px rgba(0, 0, 0, .1);
}
/****可以加一些自己的背景图片,替换引号内的内容为可外链的图片即可****/
body{
    background-repeat: repeat-y;
    background-size: 100%;
    background-attachment:fixed;
    background-image: url('https://s3.ax1x.com/2020/11/18/Dm6ex0.jpg');
}
/*****窗口背景的透明虚化效果*****/
body>#wrapper,body>.wrap,body>#main,body #appbar,body #hdtbSum{
    background: rgba(225,225,225,0);
}
body>#wrapper,body>.wrap,body>.wrapper_new #foot #help {
    background: rgba(225,225,225,0);
}
body>#wrapper,body>.wrap,body>.wrapper_new #foot {
    background: rgba(225,225,225,0);
}
body>#wrapper,body>.wrap,body>.wrapper_new .sam_newgrid~#page {
    background: rgba(225,225,225,0);
}
body>#wrapper,body>.wrap,body>#main,body #appbar,body .f6F9Be {
    background: rgba(225,225,225,0);

}
body #head {
    background-color: rgba(225,225,225,0);
}
form.fm .s_ipt_wr.bg {
    background: #fff0
}
body>.minidiv .sfbg {
    background: #b3b3b354;
}
body>.minidiv .RNNXgb {
    background: #b3b3b354;
}
/**隐藏首页的大图标-修复可能导致外援样式异常**/
body[baidu] #s_lg_img_new{
    display:none !important;
}
#wrapper #content_left .result, #wrapper #content_left .c-container{
    border-radius: 5px;
}
```
### 代码预览样图

![baidu1](./images/baidu1.png)

![baidu2](./images/baidu2.png)

![baidu3](./images/baidu3.png)

![google1.png](./images/google1.png)

![google2.png](./images/google2.png)

<a href="https://cdn.jsdelivr.net/gh/Arley517693777/Arley517693777.github.io@master/archives/assets/5313c1c282ef5b7f2bea5d82b5142f06.png" data-fancybox="images">
<img src="https://cdn.jsdelivr.net/gh/Arley517693777/Arley517693777.github.io@master/archives/assets/5313c1c282ef5b7f2bea5d82b5142f06.png">
<figcaption>baidu1.png</figcaption>
  </a>
