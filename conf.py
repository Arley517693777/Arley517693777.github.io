# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "Arley517693777/Arley517693777.github.io@master"
}

# 站点设置
site_name = "Arley's Blog"
site_logo = "${static_prefix}arley.png"
site_build_date = "2019-10-18T16:51+08:00"
author = "Arley"
email = "leon517693777@gmail.com"
author_homepage = "https://arley.cn"
description = "Living without an aim is like sailing without a compass。<br>生活没有目标，犹如航海没有罗盘。"
key_words = ['Maverick', 'Arley', 'Galileo', 'arleyblog']
language = 'zh-CN'
background_img = "${static_prefix}bg.jpg"
external_links = [
    {
        "name": "趣味网页",
        "url": "https://arley.cn/Dog/",
        "brief": "滑稽"
    },
    {
        "name": "2021新年祝福",
        "url": "https://arley.cn/2021/",
        "brief": "新年祝福看云烟花"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "读书",
        "url": "${site_prefix}read",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "GitHub",
        "url": "https://github.com/Arley517693777",
        "icon": "gi gi-github"
    }
]

valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "djccxqIYE2J9DYtSFY7fg1c1-MdYXbMMI",
    "appKey": "GskHdEqrq48tYUSFSeoJd4Fy",
    "avatar": "wavatar",
    "visitor": True,
    "recordIP": True
}

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
<link rel="shortcut icon" href="https://arley517693777.github.io./favicon.ico">
<script async src="//busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js"></script>
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
<link rel="stylesheet" type="text/css" href="css/szgotop.css" />
<script src="https://qncdn.wanshifu.com/wshifu-user/js/jquery-3.2.1.min.js"></script>
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?d69b9b23082b2143a5bce14c4c459baa";
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(hm, s);
})();
</script>
'''

footer_addon = '本站总访问量<span id="busuanzi_value_site_pv"><i class="fa fa-spinner"></i></span> Hits'

body_addon = '<div class="back-to-top cd-top faa-float animated cd-is-visible" style="top: -900px;"></div></script><script type="text/javascript" src="https://arley517693777.github.io./assets/szgotop.js"></script>'
