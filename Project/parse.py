import urlparse
...

    def parse_items(self, response):
        content = Selector(response=response).xpath('//body')
        for nodes in content:

            # build absolute URLs
            img_urls = [urlparse.urljoin(response.url, src)
                        for src in nodes.xpath('//img/@src').extract()]

            # use "image_urls" instead of "image_url"
            item['image_urls'] = img_urls

            yield item
