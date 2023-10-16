import scrapy

class MemberItem(scrapy.Item):
    name = scrapy.Field()
    activities = scrapy.Field()
    subsector_activities = scrapy.Field()
    po_box = scrapy.Field()
    city = scrapy.Field()
    fax = scrapy.Field()
    email = scrapy.Field()
    location = scrapy.Field()
    manager = scrapy.Field()
