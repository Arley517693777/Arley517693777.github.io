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
<link rel="shortcut icon" href="https://cdn.jsdelivr.net/gh/Arley517693777/Arley517693777.github.io/favicon.ico">
<script async src="//busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Arley517693777/Arley517693777.github.io/assets/font-awesome.min.css">
<!-- 悬挂的喵 -->
<link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/gh/Arley517693777/gotop/css/szgotop.css" />
<!-- Core CSS file -->
<link rel="stylesheet" href="https://arley517693777.github.io/assets/PhotoSwipe/photoswipe.css"> 
<link rel="stylesheet" href="phttps://arley517693777.github.io/assets/PhotoSwipe/default-skin/default-skin.css"> 
<!-- Core JS file -->
<script src="https://arley517693777.github.io/assets/PhotoSwipe/photoswipe.min.js"></script> 
<!-- UI JS file -->
<script src="https://arley517693777.github.io/assets/PhotoSwipe/photoswipe-ui-default.min.js"></script> 

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

body_addon = r'''
<script type="text/javascript" src="https://cdn.jsdelivr.net/gh/Arley517693777/gotop/js/szgotop.js"></script>
<script type="text/javascript" src="https://cdn.jsdelivr.net/gh/Arley517693777/gotop/js/jquery-3.2.1.min.js"></script>
<div class="back-to-top cd-top faa-float animated cd-is-visible" style="top: -999px;"></div>
<!-- Root element of PhotoSwipe. Must have class pswp. -->
<div class="pswp" tabindex="-1" role="dialog" aria-hidden="true">
    <!-- Background of PhotoSwipe. 
         It's a separate element as animating opacity is faster than rgba(). -->
    <div class="pswp__bg"></div>
    <!-- Slides wrapper with overflow:hidden. -->
    <div class="pswp__scroll-wrap">
        <!-- Container that holds slides. 
            PhotoSwipe keeps only 3 of them in the DOM to save memory.
            Don't modify these 3 pswp__item elements, data is added later on. -->
        <div class="pswp__container">
            <div class="pswp__item"></div>
            <div class="pswp__item"></div>
            <div class="pswp__item"></div>
        </div>
        <!-- Default (PhotoSwipeUI_Default) interface on top of sliding area. Can be changed. -->
        <div class="pswp__ui pswp__ui--hidden">
            <div class="pswp__top-bar">
                <!--  Controls are self-explanatory. Order can be changed. -->
                <div class="pswp__counter"></div>
                <button class="pswp__button pswp__button--close" title="Close (Esc)"></button>
                <button class="pswp__button pswp__button--share" title="Share"></button>
                <button class="pswp__button pswp__button--fs" title="Toggle fullscreen"></button>
                <button class="pswp__button pswp__button--zoom" title="Zoom in/out"></button>
                <!-- Preloader demo https://codepen.io/dimsemenov/pen/yyBWoR -->
                <!-- element will get class pswp__preloader--active when preloader is running -->
                <div class="pswp__preloader">
                    <div class="pswp__preloader__icn">
                      <div class="pswp__preloader__cut">
                        <div class="pswp__preloader__donut"></div>
                      </div>
                    </div>
                </div>
            </div>
            <div class="pswp__share-modal pswp__share-modal--hidden pswp__single-tap">
                <div class="pswp__share-tooltip"></div> 
            </div>
            <button class="pswp__button pswp__button--arrow--left" title="Previous (arrow left)">
            </button>
            <button class="pswp__button pswp__button--arrow--right" title="Next (arrow right)">
            </button>
            <div class="pswp__caption">
                <div class="pswp__caption__center"></div>
            </div>
        </div>
    </div>
</div>
<script>
(function (gallerySelector, itemSelector) {
    var openPhotoSwipe = function (galleryIndex, itemIndex) {
        var gallery = this.gallerys[galleryIndex];
        var options = {
            galleryUID: String(galleryIndex + 1),
            index: itemIndex,
            getThumbBoundsFn: function (index) {
                var thumbnail = gallery[index].el,
                    pageYScroll = window.pageYOffset || document.documentElement.scrollTop,
                    rect = thumbnail.getBoundingClientRect();
                return { x: rect.left, y: rect.top + pageYScroll, w: rect.width };
            }
        }
        var pswp = new PhotoSwipe(document.querySelectorAll('.pswp')[0],
            PhotoSwipeUI_Default, gallery, options);
        pswp.init();
    };

    var figureClick = function (e) {
        e = e || window.event;
        e.preventDefault ? e.preventDefault() : e.returnValue = false;
        var eTarget = e.target || e.srcElement;  // figure

        // 找到最近的 item
        var figure = eTarget;
        while (!figure.matches(itemSelector)) {
            figure = figure.parentNode;
        }

        // 找到最近的 gallery
        var gallery = figure;
        while (!gallery.matches(gallerySelector)) {
            gallery = gallery.parentNode;
        }

        var galleryIndex = parseInt(gallery.dataset.pswpGid) - 1;
        var itemIndex = parseInt(figure.dataset.pswpPid) - 1;
        openPhotoSwipe(galleryIndex, itemIndex);
    }

    var initPhotoSwipeFromDOM = function () {
        this.gallerys = [];

        var gallyers = document.querySelectorAll(gallerySelector);
        for (var i = 0; i < gallyers.length; i++) {
            var gallery = gallyers[i];
            gallery.setAttribute('data-pswp-gid', i + 1);
            var currentList = []

            var figures = gallery.querySelectorAll(itemSelector);
            for (var j = 0; j < figures.length; j++) {
                var figure = figures[j];
                figure.setAttribute('data-pswp-pid', j + 1);
                figure.onclick = figureClick;
                img = figure.firstChild;
                currentList.push({
                    src: img.src,
                    h: parseInt(img.getAttribute('height')),
                    w: parseInt(img.getAttribute('width')),
                    el: img
                })
            }

            this.gallerys.push(currentList);
        }
    }
    // parse picture index and gallery index from URL (#&pid=1&gid=2)
    var photoswipeParseHash = function () {
        var hash = window.location.hash.substring(1),
            params = {};

        if (hash.length < 5) {
            return params;
        }

        var vars = hash.split('&');
        for (var i = 0; i < vars.length; i++) {
            if (!vars[i]) {
                continue;
            }
            var pair = vars[i].split('=');
            if (pair.length < 2) {
                continue;
            }
            params[pair[0]] = pair[1];
        }

        if (params.gid) {
            params.gid = parseInt(params.gid, 10);
        }

        return params;
    };

    var openFromUrl = function () {
        var hashData = photoswipeParseHash();
        if (hashData.gid && hashData.pid) {
            openPhotoSwipe(hashData.gid - 1, hashData.pid - 1);
        }
    }

    initPhotoSwipeFromDOM();
    openFromUrl();
})('.pswp-gallery', '.pswp-item');
</script>
'''
