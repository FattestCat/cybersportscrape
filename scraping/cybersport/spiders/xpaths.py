XPATH_POST_LINK = '//a[@class="cs-news__link inverse-color--black-4a"]/@href'
XPATH_POST_TITLE = '//h1[@itemprop="headline"]/text()'
XPATH_POST_DATE = '//time[@itemprop="datePublished"]/@datetime'
XPATH_POST_CONTENT = '//div[@class="typography js-mediator-article"]/p//text()'
XPATH_POST_TAGS = '//div[@class="article__tags"]/span//text()'


XPATH_POST_LINK_DOT = '//li[@class="panel active-panel"]//div[@class="short-news"]//a[@class="short-text"]/@href'
XPATH_POST_TITLE_DOT = '//header[@class="news-item__header"]//h1//text()'
XPATH_POST_DATE_DOT = '//header[@class="news-item__header"]//time/@datetime'
XPATH_POST_CONTENT_DOT = '//div[@itemprop="articleBody"]/p/text()'
XPATH_POST_TAGS_DOT = '//div[@class="news-item__tags-line"]/a/text()'
XPATH_POST_NEXT_PAGE_DOT = '//div[@class="pager"]//a[@class="next"]//@href'
