import logging
import sys

def setup_scrapy_logging():
    if getattr(setup_scrapy_logging, "_installed", False):
        return

    try:
        from colorlog import ColoredFormatter
    except ImportError:
        print("Warning: colorlog not installed. Install with: pip install colorlog")
        return

    if sys.platform == "win32":
        try:
            import colorama
            colorama.init()
        except ImportError:
            pass

    use_color = sys.stdout.isatty()

    if use_color:
        formatter = ColoredFormatter(
            fmt="%(log_color)s%(asctime)s [%(name)s] %(levelname)-8s%(reset)s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            log_colors={
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'red,bg_white',
            },
            reset=True,
            style='%'
        )
    else:
        formatter = logging.Formatter(
            "%(asctime)s [%(name)s] %(levelname)-8s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    # 应用到 scrapy 及其常见子模块
    scrapy_loggers = [
        'scrapy',
        'scrapy.core',
        'scrapy.core.engine',
        'scrapy.core.scheduler',
        'scrapy.downloadermiddlewares',
        'scrapy.downloadermiddlewares.retry',
        'scrapy.downloadermiddlewares.redirect',
        'scrapy.spidermiddlewares',
        'scrapy.extensions',
        'scrapy.utils',
    ]

    for name in scrapy_loggers:
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        logger.handlers.clear()
        logger.addHandler(handler)
        logger.propagate = False  # 防止向上冒泡导致重复

    # 标记已安装
    setup_scrapy_logging._installed = True