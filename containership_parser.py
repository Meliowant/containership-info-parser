import scrapy


class SiteSpider(scrapy.Spider):
    name = 'siteSpider'
    custom_settings = {
        'CONCURRENT_ITEMS': 1,
        'CONCURRENT_REQUESTS': 1,
    }
    start_urls = ['http://www.containership-info.com/page_names_a.html',
                  'http://www.containership-info.com/page_names_b.html',
                  'http://www.containership-info.com/page_names_c.html',
                  'http://www.containership-info.com/page_names_d.html',
                  'http://www.containership-info.com/page_names_e.html',
                  'http://www.containership-info.com/page_names_f.html',
                  'http://www.containership-info.com/page_names_g.html',
                  'http://www.containership-info.com/page_names_h.html',
                  'http://www.containership-info.com/page_names_i.html',
                  'http://www.containership-info.com/page_names_j.html',
                  'http://www.containership-info.com/page_names_k.html',
                  'http://www.containership-info.com/page_names_l.html',
                  'http://www.containership-info.com/page_names_m.html',
                  'http://www.containership-info.com/page_names_n.html',
                  'http://www.containership-info.com/page_names_o.html',
                  'http://www.containership-info.com/page_names_p.html',
                  'http://www.containership-info.com/page_names_q.html',
                  'http://www.containership-info.com/page_names_r.html',
                  'http://www.containership-info.com/page_names_s.html',
                  'http://www.containership-info.com/page_names_t.html',
                  'http://www.containership-info.com/page_names_u.html',
                  'http://www.containership-info.com/page_names_v.html',
                  'http://www.containership-info.com/page_names_w.html',
                  'http://www.containership-info.com/page_names_x.html',
                  'http://www.containership-info.com/page_names_y.html',
                  'http://www.containership-info.com/page_names_z.html',
                  ]

    def parse(self, response):
        self.log("Type is {}".format(type(response)))
        vals = response.xpath('//td/small/small/text()').extract()
        if vals:
            ship_no = vals[0][vals[0].find(":")+1:].strip()
        for ship_info in vals:
            self.log(ship_info)
            if len(ship_info[:ship_info.find(":")].strip()) > 0:
                yield {
                    'ship number': ship_no,
                    'ship_field': ship_info[:ship_info.find(":")].replace('\r\n', ' ').replace('\n\r', ' ').strip(),
                    'ship_field_value': ship_info[ship_info.find(":")+1:].
                    strip()
                }

        next_page = response.css("td > a::attr(href)").extract()
        for p in next_page:
            if p:
                yield scrapy.Request(response.urljoin(p), callback=self.parse)
