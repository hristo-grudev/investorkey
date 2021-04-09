BOT_NAME = 'investorkey'

SPIDER_MODULES = ['investorkey.spiders']
NEWSPIDER_MODULE = 'investorkey.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'investorkey.pipelines.InvestorkeyPipeline': 100,

}

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
