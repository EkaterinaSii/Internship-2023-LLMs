import scrapy
import re
from re import search
from scrapy.linkextractors import LinkExtractor

class AllLinksSpider(scrapy.Spider):
    name = 'all_links'

    def start_requests(self):
        with open('links_main.txt', 'r') as f:
            links = f.read().splitlines()

        for i, link in enumerate(links, start=1):
            yield scrapy.Request(url=link, callback=self.parse, meta={'page_number': i})

        # for link in links:
        #     yield scrapy.Request(url=link, callback=self.parse)

    def save_to_file(self, links,page_number):

        link_to_ignore = ['https://www.samk.fi','https://www.samk.fi/en/','https://www.samk.fi/en/?page_id=1721',
                      'https://www.samk.fi/en/research-and-cooperation/simulation-centre-for-health-and-welfare/', 'https://www.samk.fi/en/search-staff/',
                      'https://www.samk.fi/en/study/to-working-life/', 'https://www.samk.fi/en/study/admissions/', 'https://www.samk.fi/en/new-student/study-info/',
                      'https://www.samk.fi/en/how-to-apply/bachelor-degree/']

        news_articles = ['https://www.samk.fi/en/news/','https://www.samk.fi/en/samk-at-the-dubai-world-expo/']

        filename = f'page # {page_number}.txt'
        with open(filename, 'w') as f:
            for link in links:
                if search('/#',link.url) or search('/cn/',link.url) or link.url in link_to_ignore or link.url in news_articles or search('www.samk.fi/en/uutiset/',link.url) or search('www.samk.fi/en/aihe',link.url) or not link.url.startswith('https://www.samk.fi'):
                    pass
                else:
                    f.write(link.url + '\n')

    def parse(self,response):

        link_extractor = LinkExtractor(allow_domains=['samk.fi'], unique=True)
        links = link_extractor.extract_links(response)


        page_number = response.meta['page_number']
        self.save_to_file(links, page_number)

        #self.save_to_file(links)



class LinkSpider(scrapy.Spider):
    
    name = 'links'
    allowed_domains = ['samk.fi']
    start_urls = ['https://www.samk.fi/en/']

    def start_requests(self):
        urls = ['https://www.samk.fi/en/']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def save_to_file(self, links):

        link_to_ignore = ['https://www.samk.fi','https://www.samk.fi/en/','https://www.samk.fi/en/?page_id=1721',
                      'https://www.samk.fi/en/research-and-cooperation/simulation-centre-for-health-and-welfare/', 'https://www.samk.fi/en/search-staff/',
                      'https://www.samk.fi/en/study/to-working-life/', 'https://www.samk.fi/en/study/admissions/', 'https://www.samk.fi/en/new-student/study-info/',
                      'https://www.samk.fi/en/how-to-apply/bachelor-degree/']

        news_articles = ['https://www.samk.fi/en/news/','https://www.samk.fi/en/samk-at-the-dubai-world-expo/']

        all_links =[]

        with open('links_main.txt', 'w') as f:
            for link in links:
                if search('/#',link.url) or search('/cn/',link.url) or link.url in link_to_ignore or link.url in news_articles or search('www.samk.fi/en/uutiset/',link.url) or search('www.samk.fi/en/aihe',link.url) or not link.url.startswith('https://www.samk.fi'):
                    pass
                else:
                    f.write(link.url + '\n')
                    all_links.append(link.url)

        # other_links = []
        # with open('links6.txt', 'w') as f:
        #     for link in all_links:
        #         response = scrapy.Request(url=link) 
        #         link_extractor = LinkExtractor(allow_domains=['samk.fi'], unique=True)
        #         extracted_links = link_extractor.extract_links(response)
                
        #         for extracted_link in extracted_links:
        #             if search('/#',extracted_link.url) or search('/cn/',extracted_link.url) or extracted_link.url in link_to_ignore or extracted_link.url in news_articles or search('www.samk.fi/en/uutiset/',extracted_link.url) or search('www.samk.fi/en/aihe',extracted_link.url) or not extracted_link.url.startswith('https://www.samk.fi'):
        #                 f.write('OLD\n')
        #             else:
        #                 f.write('NEW\n')
        #                 other_links.append(extracted_link.url)
        #                 f.write(extracted_link.url + '\n')

    def parse(self,response):
        link_extractor = LinkExtractor(allow_domains=['samk.fi'], unique=True)

        links = link_extractor.extract_links(response)
        self.save_to_file(links)


class TextSpider(scrapy.Spider):
    name = "text"
    #allowed_domains = ["samk.fi"]
    #start_urls = ["https://www.samk.fi/en/education/bachelor-degree/"]


    def start_requests(self):
        # url = 'https://www.samk.fi/en/education/bachelor-degree/'
        url = 'https://www.samk.fi/en/'
        yield scrapy.Request(url=url, callback=self.parse)

    def save_to_file(self, text):
        with open('content2.txt', 'w', encoding='utf-8') as f:
            f.write(text)

    def parse(self, response):

        ###### WORKS #########
        header_elements = response.css('header#masthead *')
        # footer_element = response.css('footer#footer')
        response = response.replace(body=''.join(header_elements.getall()))
        #response = response.replace(body=''.join(header_elements.getall()) + ''.join(footer_element.getall()))
        text_content = response.css('body ::text').getall()
        text = ' '.join(text_content).strip()

        self.save_to_file(text)
        ######################

##############################################################################################################################
# exclude_list = ['header', 'div#top-nav', 'footer']
# exclude_selector = ', '.join(exclude_list)
# excluded_elements = response.css(exclude_selector)
# response = response.replace(body=''.join(response.css('*:not({})'.format(exclude_selector)).getall()))

# text_content = response.css('body ::text').getall()

#response = response.replace(body=''.join(div_elements.getall()))
#div_elements = response.css('div#top-nav *')
#  excluded_elements = response.css('header, div#top-nav')
# excluded_div = response.css('div#top-nav')

#excluded_header = response.css('header *')

        # paragraphs = response.css('p:not(div#top-nav p):not(header *) ::text').getall()
        # headings = response.css('h2:not(div#top-nav h2):not(header *) ::text').getall()

        # extracted_text = ' '.join(paragraphs + headings).strip()
        # self.save_to_file(extracted_text)

# header_elements = response.scc('header *')
        # response = response.replace(body=''.join(header_elements.getall()))
        # text_content = response.css('body ::text').getall()

        # text = ' '.join(text_content).strip()

        # self.save_to_file(text)