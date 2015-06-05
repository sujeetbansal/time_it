class PriceInfo(object):
  def __init__(self, time=None, price=None):
    super(PriceInfo, self).__init__()
    self.time = time
    self.price = price


class ItemKey(object):
  def __init__(self, url=None, seller_info=None):
    self.url = url
    self.seller_info = seller_info


class ItemInfo(object):
  def __init__(self, sku=None, title=None, description=None):
    super(ItemInfo, self).__init__()
    self.sku = sku
    self.title = title
    self.description = description


class SellerInfo(object):
  def __init__(self, name=None):
    super(SellerInfo, self).__init__()
    self.name = name


class EtailerInfo(object):
  def __init__(self, name=None):
    super(EtailerInfo, self).__init__()
    self.name = name


class Item(object):
  def __init__(self, item_key=None, item_info=None, price_history=None,
               seller_info=None, etailer_info=None,
               related_items=None):
    super(Item, self).__init__()
    self.item_key = item_key
    self.item_info = item_info
    self.price_history = price_history  # List of PriceInfo.
    self.etailer_info = etailer_info
    self.seller_info = seller_info
    self.related_items = related_items
