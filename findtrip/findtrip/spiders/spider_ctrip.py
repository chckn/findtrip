import scrapy
from findtrip.items import FindtripItem

class CtripSpider(scrapy.Spider):
    name = 'Ctrip'
#    start_urls=["http://flights.ctrip.com/booking/BJS-XMN-day-1.html?DDate1=2017-09-19"]
    
    datelist=['2017-09-30','2017-10-03']
    depature=['PEK']
    arrival=['XMN']
    def start_requests(self):
        url="http://flights.ctrip.com/booking/%s-%s-day-1.html?DDate1=%s"
        for t in CtripSpider.datelist:
            for dep in CtripSpider.depature:
                for arr in CtripSpider.arrival:            
                    yield scrapy.Request(url%(dep,arr,t),callback=self.parse)
    
    def parse(self, response):
#        print response.body
        sel = scrapy.Selector(response)
        fligint_div = "//div[@id='J_flightlist2']/div"
        dataList = sel.xpath(fligint_div)
        print "List"
        print dataList,len(dataList)
#        sys.stdout.flush()
        items = []
        for index,each in enumerate(dataList):
            flight_each = fligint_div+'['+str(index+1)+']'
            flight_tr = flight_each+"//tr[@class='J_header_row']"
            istrain = sel.xpath(flight_each + "//div[@class='train_flight_tit']")

            if istrain:
                print "this data is train add"
            else:
                company = sel.xpath(flight_tr + "//div[@class='info-flight J_flight_no']//text()").extract()
                flight_no = sel.xpath(flight_tr + "//div[@class='clearfix J_flight_no']/@data-flight").extract()
                flight_time_from = sel.xpath(flight_tr + "//td[@class='right']/div[1]//text()").extract()
                flight_time_to = sel.xpath(flight_tr + "//td[@class='left']/div[1]//text()").extract()

                airports_from =  sel.xpath(flight_tr + "//td[@class='right']/div[2]//text()").extract()
                airports_to = sel.xpath(flight_tr + "//td[@class='left']/div[2]//text()").extract()
                airports_via=sel.xpath(flight_tr+"//div[@class='stopover']/span/text()").extract() 
#                airports = [airports_from,airports_to]

                price_middle = sel.xpath(flight_tr + "[1]//td[7]/span//text()").extract()
               # price_middle = sel.xpath(flight_tr + "[1]//td[@class='price middle ']/span//text()").extract()
                price = sel.xpath(flight_tr + "[1]//td[@class='price ']/span//text()").extract()
                if price_middle:
                    price = price_middle
                elif price:
                    price = price
                else:
                    price = ''
                try:
                    item = FindtripItem()
                    item['site'] = 'Ctrip'
                    item['flight'] = flight_no[0]
                    item['flight_date']=response.url[-10:]
                    item['dep_time'] = flight_time_from[0]
                    item['arr_time'] = flight_time_to[0]
                    item['dep_city'] = airports_from[0]
                    item['arr_city'] = airports_to[0]
                    if airports_via:
                        item['via_city']=airports_via[0]
                    item['price'] = price[1]
                    items.append(item)
               
                except Exception,e:
                    pass
                  #  print e
                 #   print "\t",dataList[index].extract()
                else:
                    print item
               
        return items   
