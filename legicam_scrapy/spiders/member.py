import scrapy
from legicam_scrapy.items import MemberItem

class MemberSpider(scrapy.Spider):
    name = "member"
    start_urls = ["https://www.legicam.cm/index.php/p/membres"]

    def parse(self, response):
        # Extract member details on the current page
        member_details = response.css(".form-group.doc1-list-item")

        for member in member_details:
            item = MemberItem()
            item["name"] = member.css("h4.media-heading a::text").get()
            
            # Follow the link to the detailed member page and pass the item
            see_more_link = member.css("h4.media-heading a::attr(href)").get()
            request = response.follow(see_more_link, self.parse_member_details, meta={"item": item})
            yield request

        # Check for pagination and follow to the next page if available
        next_page = response.css("ul.pagination li.active + li a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_member_details(self, response):
        item = response.meta["item"]

        # Extract additional details from the "See more" page
        details = response.css(".media-body p")

        for detail in details:
            text = detail.xpath("strong/text()").get()
            value = detail.xpath("text()").get()

            if text == "Activités":
                item["activities"] = value.strip().replace(":", "")
            elif text == "Sous secteur d'activités":
                item["subsector_activities"] = value.strip().replace(":", "")
            elif text == "Boite postale":
                item["po_box"] = value.strip().replace(":", "")
            elif text == "Ville":
                item["city"] = value.strip().replace(":", "")
            elif text == "Fax":
                item["fax"] = value.strip().replace(":", "")
            elif text == "Email":
                item["email"] = value.strip().replace(":", "")
            elif text == "Localisation":
                item["location"] = value.strip().replace(":", "")
            elif text == "Dirigeant(s)":
                item["manager"] = value.strip().replace(":","")
        
        yield item
