# @python3.9
# @icon https://d2hlo835aj7uqe.cloudfront.net/production/wp-content/uploads/2021/04/StockXAuthor-400x400.jpg
# @argument1 { "type": "text", "placeholder": "SKU/PID" 

import pandas as pd
import requests
import json
from tabulate import tabulate
import sys


def parse(kw):
    sess = requests.session()
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'Host': 'stockx.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br'
    }  # 设置请求头

    searchURL = f'https://stockx.com/api/browse?_search={kw}&page=1&resultsPerPage=20&dataType=product&facetsToRetrieve[]=browseVerticals&propsToRetrieve[][]=brand&propsToRetrieve[][]=colorway&propsToRetrieve[][]=media.thumbUrl&propsToRetrieve[][]=title&propsToRetrieve[][]=productCategory&propsToRetrieve[][]=shortDescription&propsToRetrieve[][]=urlKey'
    search = sess.get(searchURL,
                      headers=header).json()['Products']

    # for index in range(len(search)):
    #     print(f'[{index}] - [{search[index]["urlKey"]}]')
    # pickIndex = input('请输入你想查找的商品INDEX: ') 此处使用sku 因此默认选择index=0

    pickIndex = 0
    productDscp = search[int(pickIndex)]
    pickurlKey = productDscp["urlKey"]
    pickUrl = f'https://stockx.com/zh-cn/{pickurlKey}'
    picture = search[int(pickIndex)]['media']['thumbUrl']

    dt = {
        "operationName": "GetProduct",
        "variables": {
            "id": f"{pickurlKey}",
            "currencyCode": "USD",
            "countryCode": "US",
            "marketName": "US"
        },
        "query": "query GetProduct($id: String!, $currencyCode: CurrencyCode, $countryCode: String!, $marketName: String) {\n  product(id: $id) {\n    id\n    listingType\n    ...AffirmCalloutFragment\n    ...BidButtonContentFragment\n    ...BreadcrumbsFragment\n    ...BreadcrumbSchemaFragment\n    ...BuySellContentFragment\n    ...BuySellFragment\n    ...HazmatWarningFragment\n    ...HeaderFragment\n    ...LastSaleFragment\n    ...LowInventoryBannerFragment\n    ...MarketActivityFragment\n    ...MediaFragment\n    ...MyPositionFragment\n    ...ProductDetailsFragment\n    ...ProductMetaTagsFragment\n    ...ProductSchemaFragment\n    ...ScreenTrackerFragment\n    ...SizeSelectorWrapperFragment\n    ...StatsForNerdsFragment\n    ...ThreeSixtyImageFragment\n    ...TrackingFragment\n    ...UtilityGroupFragment\n    __typename\n  }\n}\n\nfragment AffirmCalloutFragment on Product {\n  productCategory\n  urlKey\n  market(currencyCode: $currencyCode) {\n    bidAskData(country: $countryCode, market: $marketName) {\n      lowestAsk\n      __typename\n    }\n    __typename\n  }\n  variants {\n    id\n    market(currencyCode: $currencyCode) {\n      bidAskData(country: $countryCode, market: $marketName) {\n        lowestAsk\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment BidButtonContentFragment on Product {\n  id\n  urlKey\n  sizeDescriptor\n  productCategory\n  lockBuying\n  lockSelling\n  minimumBid(currencyCode: $currencyCode)\n  market(currencyCode: $currencyCode) {\n    bidAskData(country: $countryCode, market: $marketName) {\n      highestBid\n      highestBidSize\n      lowestAsk\n      lowestAskSize\n      __typename\n    }\n    __typename\n  }\n  variants {\n    id\n    market(currencyCode: $currencyCode) {\n      bidAskData(country: $countryCode, market: $marketName) {\n        highestBid\n        highestBidSize\n        lowestAsk\n        lowestAskSize\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment BreadcrumbsFragment on Product {\n  breadcrumbs {\n    name\n    url\n    level\n    __typename\n  }\n  __typename\n}\n\nfragment BreadcrumbSchemaFragment on Product {\n  breadcrumbs {\n    name\n    url\n    __typename\n  }\n  __typename\n}\n\nfragment BuySellContentFragment on Product {\n  id\n  urlKey\n  sizeDescriptor\n  productCategory\n  lockBuying\n  lockSelling\n  market(currencyCode: $currencyCode) {\n    bidAskData(country: $countryCode, market: $marketName) {\n      highestBid\n      highestBidSize\n      lowestAsk\n      lowestAskSize\n      __typename\n    }\n    __typename\n  }\n  variants {\n    id\n    market(currencyCode: $currencyCode) {\n      bidAskData(country: $countryCode, market: $marketName) {\n        highestBid\n        highestBidSize\n        lowestAsk\n        lowestAskSize\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment BuySellFragment on Product {\n  id\n  title\n  urlKey\n  sizeDescriptor\n  productCategory\n  market(currencyCode: $currencyCode) {\n    bidAskData(country: $countryCode, market: $marketName) {\n      highestBid\n      highestBidSize\n      lowestAsk\n      lowestAskSize\n      __typename\n    }\n    __typename\n  }\n  media {\n    imageUrl\n    __typename\n  }\n  variants {\n    id\n    market(currencyCode: $currencyCode) {\n      bidAskData(country: $countryCode, market: $marketName) {\n        highestBid\n        highestBidSize\n        lowestAsk\n        lowestAskSize\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment HazmatWarningFragment on Product {\n  id\n  hazardousMaterial {\n    lithiumIonBucket\n    __typename\n  }\n  __typename\n}\n\nfragment HeaderFragment on Product {\n  primaryTitle\n  secondaryTitle\n  condition\n  productCategory\n  __typename\n}\n\nfragment LastSaleFragment on Product {\n  id\n  market(currencyCode: $currencyCode) {\n    ...LastSaleMarket\n    __typename\n  }\n  variants {\n    id\n    market(currencyCode: $currencyCode) {\n      ...LastSaleMarket\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment LastSaleMarket on Market {\n  salesInformation {\n    annualHigh\n    annualLow\n    volatility\n    pricePremium\n    lastSale\n    changeValue\n    changePercentage\n    __typename\n  }\n  __typename\n}\n\nfragment LowInventoryBannerFragment on Product {\n  id\n  productCategory\n  primaryCategory\n  sizeDescriptor\n  market(currencyCode: $currencyCode) {\n    ...LowInventoryBannerMarket\n    __typename\n  }\n  variants {\n    id\n    market(currencyCode: $currencyCode) {\n      ...LowInventoryBannerMarket\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment LowInventoryBannerMarket on Market {\n  bidAskData(country: $countryCode, market: $marketName) {\n    numberOfAsks\n    lowestAsk\n    __typename\n  }\n  salesInformation {\n    lastSale\n    __typename\n  }\n  __typename\n}\n\nfragment MarketActivityFragment on Product {\n  id\n  title\n  productCategory\n  primaryTitle\n  secondaryTitle\n  media {\n    smallImageUrl\n    __typename\n  }\n  __typename\n}\n\nfragment MediaFragment on Product {\n  id\n  productCategory\n  title\n  brand\n  urlKey\n  variants {\n    id\n    hidden\n    traits {\n      size\n      __typename\n    }\n    __typename\n  }\n  media {\n    gallery\n    all360Images\n    imageUrl\n    __typename\n  }\n  __typename\n}\n\nfragment MyPositionFragment on Product {\n  id\n  urlKey\n  __typename\n}\n\nfragment ProductDetailsFragment on Product {\n  id\n  title\n  productCategory\n  description\n  traits {\n    name\n    value\n    visible\n    format\n    __typename\n  }\n  __typename\n}\n\nfragment ProductMetaTagsFragment on Product {\n  id\n  urlKey\n  productCategory\n  brand\n  model\n  title\n  description\n  condition\n  styleId\n  breadcrumbs {\n    name\n    url\n    __typename\n  }\n  traits {\n    name\n    value\n    __typename\n  }\n  media {\n    thumbUrl\n    imageUrl\n    __typename\n  }\n  market(currencyCode: $currencyCode) {\n    bidAskData(country: $countryCode, market: $marketName) {\n      lowestAsk\n      numberOfAsks\n      __typename\n    }\n    __typename\n  }\n  variants {\n    id\n    hidden\n    traits {\n      size\n      __typename\n    }\n    market(currencyCode: $currencyCode) {\n      bidAskData(country: $countryCode, market: $marketName) {\n        lowestAsk\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment ProductSchemaFragment on Product {\n  id\n  urlKey\n  productCategory\n  brand\n  model\n  title\n  description\n  condition\n  styleId\n  traits {\n    name\n    value\n    __typename\n  }\n  media {\n    thumbUrl\n    imageUrl\n    __typename\n  }\n  market(currencyCode: $currencyCode) {\n    bidAskData(country: $countryCode, market: $marketName) {\n      lowestAsk\n      numberOfAsks\n      __typename\n    }\n    __typename\n  }\n  variants {\n    id\n    hidden\n    traits {\n      size\n      __typename\n    }\n    market(currencyCode: $currencyCode) {\n      bidAskData(country: $countryCode, market: $marketName) {\n        lowestAsk\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment ScreenTrackerFragment on Product {\n  id\n  brand\n  productCategory\n  primaryCategory\n  title\n  market(currencyCode: $currencyCode) {\n    bidAskData(country: $countryCode, market: $marketName) {\n      highestBid\n      lowestAsk\n      numberOfAsks\n      numberOfBids\n      __typename\n    }\n    salesInformation {\n      lastSale\n      __typename\n    }\n    __typename\n  }\n  media {\n    imageUrl\n    __typename\n  }\n  traits {\n    name\n    value\n    __typename\n  }\n  variants {\n    id\n    traits {\n      size\n      __typename\n    }\n    market(currencyCode: $currencyCode) {\n      bidAskData(country: $countryCode, market: $marketName) {\n        highestBid\n        lowestAsk\n        numberOfAsks\n        numberOfBids\n        __typename\n      }\n      salesInformation {\n        lastSale\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment SizeSelectorWrapperFragment on Product {\n  id\n  ...SizeSelectorFragment\n  ...SizeSelectorHeaderFragment\n  ...SizesFragment\n  ...SizesOptionsFragment\n  ...SizeChartFragment\n  ...SizeChartContentFragment\n  ...SizeConversionFragment\n  ...SizesAllButtonFragment\n  __typename\n}\n\nfragment SizeSelectorFragment on Product {\n  id\n  title\n  productCategory\n  sizeDescriptor\n  availableSizeConversions {\n    name\n    type\n    __typename\n  }\n  defaultSizeConversion {\n    name\n    type\n    __typename\n  }\n  variants {\n    id\n    hidden\n    traits {\n      size\n      __typename\n    }\n    sizeChart {\n      baseSize\n      baseType\n      displayOptions {\n        size\n        type\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment SizeSelectorHeaderFragment on Product {\n  sizeDescriptor\n  productCategory\n  availableSizeConversions {\n    name\n    type\n    __typename\n  }\n  __typename\n}\n\nfragment SizesFragment on Product {\n  id\n  productCategory\n  title\n  __typename\n}\n\nfragment SizesOptionsFragment on Product {\n  id\n  variants {\n    id\n    hidden\n    group {\n      shortCode\n      __typename\n    }\n    traits {\n      size\n      __typename\n    }\n    sizeChart {\n      baseSize\n      baseType\n      displayOptions {\n        size\n        type\n        __typename\n      }\n      __typename\n    }\n    market(currencyCode: $currencyCode) {\n      bidAskData(country: $countryCode, market: $marketName) {\n        lowestAsk\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment SizeChartFragment on Product {\n  availableSizeConversions {\n    name\n    type\n    __typename\n  }\n  defaultSizeConversion {\n    name\n    type\n    __typename\n  }\n  __typename\n}\n\nfragment SizeChartContentFragment on Product {\n  availableSizeConversions {\n    name\n    type\n    __typename\n  }\n  defaultSizeConversion {\n    name\n    type\n    __typename\n  }\n  variants {\n    id\n    sizeChart {\n      baseSize\n      baseType\n      displayOptions {\n        size\n        type\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment SizeConversionFragment on Product {\n  productCategory\n  sizeDescriptor\n  availableSizeConversions {\n    name\n    type\n    __typename\n  }\n  defaultSizeConversion {\n    name\n    type\n    __typename\n  }\n  __typename\n}\n\nfragment SizesAllButtonFragment on Product {\n  id\n  sizeAllDescriptor\n  market(currencyCode: $currencyCode) {\n    bidAskData(country: $countryCode, market: $marketName) {\n      lowestAsk\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment StatsForNerdsFragment on Product {\n  id\n  title\n  productCategory\n  sizeDescriptor\n  urlKey\n  __typename\n}\n\nfragment ThreeSixtyImageFragment on Product {\n  id\n  title\n  variants {\n    id\n    __typename\n  }\n  productCategory\n  media {\n    all360Images\n    __typename\n  }\n  has360Images\n  __typename\n}\n\nfragment TrackingFragment on Product {\n  id\n  productCategory\n  primaryCategory\n  brand\n  title\n  market(currencyCode: $currencyCode) {\n    bidAskData(country: $countryCode, market: $marketName) {\n      highestBid\n      lowestAsk\n      __typename\n    }\n    __typename\n  }\n  variants {\n    id\n    market(currencyCode: $currencyCode) {\n      bidAskData(country: $countryCode, market: $marketName) {\n        highestBid\n        lowestAsk\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment UtilityGroupFragment on Product {\n  id\n  ...FollowFragment\n  ...FollowContentFragment\n  ...FollowShareContentFragment\n  ...FollowSuccessFragment\n  ...PortfolioFragment\n  ...PortfolioContentFragment\n  ...ShareFragment\n  __typename\n}\n\nfragment FollowFragment on Product {\n  id\n  productCategory\n  title\n  variants {\n    id\n    traits {\n      size\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment FollowContentFragment on Product {\n  title\n  __typename\n}\n\nfragment FollowShareContentFragment on Product {\n  id\n  title\n  sizeDescriptor\n  urlKey\n  variants {\n    id\n    traits {\n      size\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment FollowSuccessFragment on Product {\n  id\n  title\n  productCategory\n  sizeDescriptor\n  media {\n    smallImageUrl\n    __typename\n  }\n  variants {\n    id\n    traits {\n      size\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment PortfolioFragment on Product {\n  id\n  title\n  productCategory\n  variants {\n    id\n    __typename\n  }\n  traits {\n    name\n    value\n    __typename\n  }\n  __typename\n}\n\nfragment PortfolioContentFragment on Product {\n  id\n  productCategory\n  sizeDescriptor\n  variants {\n    id\n    traits {\n      size\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment ShareFragment on Product {\n  id\n  productCategory\n  title\n  media {\n    imageUrl\n    __typename\n  }\n  __typename\n}\n"
    }

    productInfo = sess.post('https://stockx.com/p/e',
                            headers={
                                'Host': 'stockx.com',
                                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98.0',
                                'Accept-Language': 'zh-CN',
                                'Accept-Encoding': 'gzip, deflate, br',
                                'Content-Type': 'application/json',
                                'Content-Length': '999',
                                'apollographql-client-name': 'Iron',
                                'apollographql-client-version': '2022.03.13.01',
                                'x-stockx-device-id': '8303ef6f-e2be-4095-a694-88a4b995e80f',
                                'Origin': 'https://stockx.com',
                                'Sec-Fetch-Dest': 'empty',
                                'Sec-Fetch-Mode': 'cors',
                                'Sec-Fetch-Site': 'same-origin',
                                'Referer': pickUrl,
                                'Connection': 'keep-alive'
                            },
                            data=json.dumps(dt)
                            ).json()['data']['product']
    return productDscp, productInfo


class product_UI:
    def __init__(self, productDscp, productInfo):
        self.productName = productDscp['title']  # product name
        self.imageLink = productDscp['media']['thumbUrl']  # product thumbImage
        self.fullLink = f'https://stockx.com/zh-cn/{productDscp["urlKey"]}'

        self.priceList = productInfo['variants']

        traitDict = {}
        for trait in productInfo['traits']:
            traitDict[trait['name']] = trait['value']
            
        self.retailPrice = traitDict.get('Retail Price')  # product's retail price
        self.releaseDate = traitDict.get('Release Date')  # when does product release
        try:
            self.sku = traitDict.get('Style')  # product's id/sku
        except:
            self.sku = None

    def show_description(self):
        print(f'\n名称：{self.productName}')
        print(f'货号SKU：{self.sku}')
        print(f'发售价格：${self.retailPrice}')
        print(f'发售日期：{self.releaseDate}')
        print(f'图片：{self.imageLink}')
        print(f'具体请查看：\n{self.fullLink}\n')
        return

    def price_Analysis(self):
        # 获取市场价格
        priceDict = {}
        for item in self.priceList:
            size = item['traits']['size']
            ask = item['market']['bidAskData']['lowestAsk']
            bid = item['market']['bidAskData']['highestBid']
            priceDict[size] = [ask, bid]

        for size, values in priceDict.items():
            if values[0] is None:
                values.append(None)
                values.append(None)
            elif values[-1] is None:
                values[0] = values[0]
                values.append(round(values[0] * 0.88, 1))
                values.append(None)
            else:
                values[0] = values[0]
                values[-1] = values[-1]
                values.append(round(float(values[0]) * 0.88))
                try:
                    values.append(format(float(values[-1])-float(self.retailPrice), '.0f'))
                except ValueError:
                    values.append('None')
        # if ask is not None:
        #     payOff = round(ask * 0.88, 1)
        #     profit = bid-eval(self.retailPrice)
        # else:
        #     payOff = None
        #     profit = None
        # print(size,ask,bid)

        df = pd.DataFrame.from_dict(priceDict, orient='index', columns=['ask', 'bid', 'payoff', 'profit'], dtype=float)
        df_sort = df.sort_values(by=['profit'], ascending=False)
        return df_sort

    def show_Price(self, df):
        # print(f'\n正在生成{self.productName}的市场价格...\n')
        print(tabulate(df, headers=['size', 'ask', 'bid', 'payoff', 'profit'], tablefmt='psql'))
        return


productDscp, productInfo = parse(kw=sys.argv[1])
product = product_UI(productDscp, productInfo)
product.show_description()
product.show_Price(product.price_Analysis())
# print(product.price_Analysis())


