# Scrapy settings for procurement project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "procurement"

SPIDER_MODULES = ["procurement.spiders"]
NEWSPIDER_MODULE = "procurement.spiders"

ADDONS = {}

PROVINCE_CONFIG = {
    "guang_xi": {
        # 主页面
        "check": {
            "url": "https://zfcg.gxzf.gov.cn/portal/category",
            "method": "post",
            "static_param": {
                    "categoryCode": "ZcyAnnouncement10016",
                    "leaf": 0,
                    "pageNo": 1,
                    "pageSize": 15,
                    "publishDateBegin": "2025-11-13",
                    "publishDateEnd": "2025-11-13",
                    "_t": ""
                }
        },
        # 详情页面
        "detail": {
            "url": "https://zfcg.gxzf.gov.cn/portal/detail",
            "method": "get",
            "static_param": {
                    "articleId": "lTGKt8QxZ9wRMXlLiMQT9A==",
                    "parentId": 66485,
                    "timestamp": ""
                }
        }

    }
}



# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Concurrency and throttling settings
#CONCURRENT_REQUESTS = 16
CONCURRENT_REQUESTS_PER_DOMAIN = 1
# 请求之间的间隔时长 s
DOWNLOAD_DELAY = 1
# 随机请求之间时长间隔
# RANDOMIZE_DOWNLOAD_DELAY = True

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# 定义请求头
# DEFAULT_REQUEST_HEADERS = {
#    "Content-Type": "application/json",
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "procurement.middlewares.ProcurementSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# 启用中间件
DOWNLOADER_MIDDLEWARES = {
   # "procurement.middlewares.AutoJsonContentTypeMiddleware": 500,
   "procurement.middlewares.InfoOnSuccessMiddleware": 1000,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "procurement.pipelines.ProcurementPipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# 启动自动限速
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
FEED_EXPORT_ENCODING = "utf-8"

# 设置请求超时
DOWNLOAD_TIMEOUT = 15