BOT_NAME = 'kocruse'

SPIDER_MODULES = ['kocruse.spiders']
NEWSPIDER_MODULE = 'kocruse.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'kocruse.pipelines.KocrusePipeline': 100,

}