from requests import get
from time import sleep
# url = "https://www.epicgames.com/store/zh-CN/free-games"
url = "https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?locale=zh-CN&country=CN&allowCountries=CN"
response = get(url)
hashMap = response.json()
ls = hashMap["data"]["Catalog"]["searchStore"]["elements"]
# ls.keys()
# title	id	namespace	description	effectiveDate	offerType	expiryDate	status
# isCodeRedemptionOnly	keyImages	seller	productSlug	urlSlug	url	items	customAttributes
# categories	tags	catalogNs	offerMappings	price	promotions
messageList = list(ls[0].keys())
print("Epic free games".center(60))
print(f"{'Name':20s}{'Price':10s}{'Time':10s}")
# title price promotions
for item in hashMap["data"]["Catalog"]["searchStore"]["elements"]:
    # {'title': '《Yooka-Laylee and the Impossible Lair》', 'id': '617b64a9631c4df0a66ea8fca480d2b9', 'namespace': 'fa11862b1cfd42e3b3c6395af46efe3e', 'description': '《Yooka-Laylee and the Impossible Lair》是《Donkey Kong Country》幕后核心成员制作的一款全新开放世界平台跳跃游戏。死敌企业B（Capital B）想做坏事，双人组需要再次挺身而出拯救世界！', 'effectiveDate': '2019-12-31T13:00:00.000Z', 'offerType': 'BASE_GAME', 'expiryDate': None, 'status': 'ACTIVE', 'isCodeRedemptionOnly': False, 'keyImages': [{'type': 'DieselStoreFrontWide', 'url': 'https://cdn1.epicgames.com/undefined/offer/EGS_PlaytonicGamesLtd_YookaLayleeandtheImpossibleLair_S3-1360x766-8faccccfe9ca390483f8a177b7fccbd4.jpg'}, {'type': 'DieselStoreFrontTall', 'url': 'https://cdn1.epicgames.com/undefined/offer/EGS_PlaytonicGamesLtd_YookaLayleeandtheImpossibleLair_S4-510x680-5f1857ce88f7747b88c5121c674470e6.jpg'}, {'type': 'OfferImageTall', 'url': 'https://cdn1.epicgames.com/undefined/offer/EGS_PlaytonicGamesLtd_YookaLayleeandtheImpossibleLair_S4-510x680-5f1857ce88f7747b88c5121c674470e6.jpg'}, {'type': 'Thumbnail', 'url': 'https://cdn1.epicgames.com/fa11862b1cfd42e3b3c6395af46efe3e/offer/EGS_PlaytonicGamesLtd_YookaLayleeandtheImpossibleLair_S5-640x478-54920a9a777ce201c97cd9650d98471a.png'}, {'type': 'CodeRedemption_340x440', 'url': 'https://cdn1.epicgames.com/fa11862b1cfd42e3b3c6395af46efe3e/offer/EGS_PlaytonicGamesLtd_YookaLayleeandtheImpossibleLair_S4-510x680-5f1857ce88f7747b88c5121c674470e6.jpg'}, {'type': 'OfferImageWide', 'url': 'https://cdn1.epicgames.com/undefined/offer/EGS_PlaytonicGamesLtd_YookaLayleeandtheImpossibleLair_S3-1360x766-8faccccfe9ca390483f8a177b7fccbd4.jpg'}], 'seller': {'id': 'o-uvtztrtfjdn3xgrwyhbuwwb5z42mbv', 'name': 'Team17 Digital Ltd'}, 'productSlug': 'yooka-laylee-and-the-impossible-lair/home', 'urlSlug': 'yooka-laylee-and-the-impossible-lair', 'url': None, 'items': [{'id': 'fd71bd8498794b1d9efe0d0b9ce2fc52', 'namespace': 'fa11862b1cfd42e3b3c6395af46efe3e'}], 'customAttributes': [{'key': 'com.epicgames.app.blacklist', 'value': '[]'}, {'key': 'publisherName', 'value': 'Team17 Digital Ltd'}, {'key': 'developerName', 'value': 'Playtonic Games Ltd.'}, {'key': 'com.epicgames.app.productSlug', 'value': 'yooka-laylee-and-the-impossible-lair/home'}], 'categories': [{'path': 'freegames'}, {'path': 'games'}, {'path': 'games/edition/base'}, {'path': 'games/edition'}, {'path': 'applications'}], 'tags': [{'id': '14944'}, {'id': '18777'}, {'id': '1370'}, {'id': '14346'}, {'id': '9547'}, {'id': '16011'}, {'id': '1117'}, {'id': '9549'}, {'id': '1151'}, {'id': '15375'}], 'catalogNs': {'mappings': [{'pageSlug': 'yooka-laylee-and-the-impossible-lair', 'pageType': 'productHome'}]}, 'offerMappings': [], 'price': {'totalPrice': {'discountPrice': 7800, 'originalPrice': 7800, 'voucherDiscount': 0, 'discount': 0, 'currencyCode': 'CNY', 'currencyInfo': {'decimals': 2}, 'fmtPrice': {'originalPrice': '¥78.00', 'discountPrice': '¥78.00', 'intermediatePrice': '¥78.00'}}, 'lineOffers': [{'appliedRules': []}]}, 'promotions': None}
    if item["promotions"] is not None:
        dateMessage = None
        if len(item["promotions"]["promotionalOffers"]) != 0:
            dateMessage = item["promotions"]["promotionalOffers"][0]["promotionalOffers"][0]
        else:
            dateMessage = item["promotions"]["upcomingPromotionalOffers"][0]["promotionalOffers"][0]
        print(f'{(item["title"]).strip("《").strip("》"):20s}'
              f'{"¥"+(item["price"]["totalPrice"]["originalPrice"] / 100).__str__():10s}'
              f'{dateMessage["startDate"]}——{dateMessage["endDate"]}')

print("\n")
for i in range(10):
    print(f"\r{10-i}s后自动关闭................................................",end="")
    sleep(1)