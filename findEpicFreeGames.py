from requests import get
from time import sleep

# url = "https://www.epicgames.com/store/zh-CN/free-games"
url = "https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?locale=zh-CN&country=CN&allowCountries=CN"
response = get(url)
hashMap = response.json()
ls = hashMap["data"]["Catalog"]["searchStore"]["elements"]
now = []
soon = []


def getTitle(item):
    s = item.get("title", "")  # s might be have '《' or '》'
    lst = s.strip("《").split("》")
    return "".join(lst)


def getOriginalPrice(item):
    details = item.get("price").get("totalPrice")
    return int(details.get("originalPrice", 0))


def isFree(item):  # Well this function is poorly designed
    if getOriginalPrice(item) == 0:
        return False

    if item.get("promotions", None) is not None:
        if len(item["promotions"]["promotionalOffers"]) != 0:
            if item["promotions"]["promotionalOffers"][0]["promotionalOffers"][0]["discountSetting"][
                "discountPercentage"] == 0:
                now.append(
                    f"{getTitle(item):25s}{(getOriginalPrice(item) / 100).__str__() + ' ' + (item['price']['totalPrice']['currencyCode']):10s}{getTime(item)}")
                return True

        elif len(item["promotions"]['upcomingPromotionalOffers']) != 0:
            if item["promotions"]['upcomingPromotionalOffers'][0]["promotionalOffers"][0]["discountSetting"][
                "discountPercentage"] == 0:
                soon.append(
                    f"{getTitle(item):25s}{(getOriginalPrice(item) / 100).__str__() + ' ' + (item['price']['totalPrice']['currencyCode']):10s}{getTime(item)}")
                return True
    else:
        return False  # It might have a bug,maybe I should check it more.


def getTime(item):
    if item.get("promotions", None) is not None:
        if len(item["promotions"]["promotionalOffers"]) != 0:
            startDate = item["promotions"]["promotionalOffers"][0]['promotionalOffers'][0]['startDate'].split("T")[0]
            endDate = item["promotions"]["promotionalOffers"][0]['promotionalOffers'][0]['endDate'].split("T")[0]
            return f"{startDate}——{endDate}"
        elif len(item["promotions"]['upcomingPromotionalOffers']) != 0:
            startDate = \
                item["promotions"]["upcomingPromotionalOffers"][0]['promotionalOffers'][0]['startDate'].split("T")[0]
            endDate = item["promotions"]["upcomingPromotionalOffers"][0]['promotionalOffers'][0]['endDate'].split("T")[
                0]
            return f"{startDate}——{endDate}"


def main():
    for item in ls:
        item.pop('id', "")
        item.pop('namespace', "")
        item.pop('description', "")
        item.pop('url', "")
        item.pop('keyImages', "")
        item.pop('categories', "")
        item.pop('tags', "")
        item.pop('catalogNs', "")
        item.pop('offerMappings', "")
        item.pop('items', "")
        item.pop('expiryDate', "")
        item.pop('customAttributes', "")
        item.pop('offerType', "")
        item.pop('productSlug', "")
        item.pop('isCodeRedemptionOnly', "")  # I don't know what is isCodeRedemptionOnly mean.
        item.pop('seller', "")
        item.pop('status', "")
        item.pop('effectiveDate', "")
        item.pop('urlSlug', "")
        item.pop('', "")
        #   It's not necessary but easy for me to maintain.

        isFree(item)

    print("Epic Free Games".center(60))

    print()
    print("FREE NOW".center(60))
    for item in now:
        print(item)

    print()
    print("COMING SOON".center(60))
    for item in soon:
        print(item)

    print()
    for i in range(15):
        print(f"\r..........Automatically shuts off after {15 - i} seconds..........", end="")
        sleep(1)


if __name__ == '__main__':
    main()
