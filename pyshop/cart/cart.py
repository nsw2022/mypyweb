from _decimal import Decimal
from django.conf import settings

from shop.models import Product


# 장바구니를 세션
class Cart:
    def __init__(self, request):
        self.session = request.session  # 세션 발급
        cart = self.session.get(settings.CART_ID)
        if not cart:
            cart = self.session[settings.CART_ID] = {}
        self.cart = cart  # 세션에서 불러온 cart
        # self.coupon_id = self.session.get('coupon_id')

    def __len__(self):  # 수량 합계
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):  # 전체 순회(반복)
        product_ids = self.cart.keys()  # 제품번호
        # 목록 id에서 해당 id의 모든 제품
        products = Product.objects.filter(id__in=product_ids)  # filter 는 sql의 where같은 느낌

        for product in products:
            item = self.cart[str(product.id)]
            item['product'] = product  # 해당 제품이 있으면 카트에 저장
            item['price'] = Decimal(item['price'])
            # 총 가격 = 단위당 가격 * 수량
            item['total_price'] = item['price'] * item['quantity']

            yield item  # item을 반환(retrun) # 뭔말인지 봐도모르겠다 써봐야알듯

    # 장바구니에 제품 추가
    def add(self, product, quantity=1, is_update=False):
        product_id = str(product.id)

        # 카트에 제품이 없는 경우
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}

        # 카트에 제품이 있는 경우
        if is_update:
            self.cart[product_id]['quantity'] = quantity  # 수량 변경
        else:
            self.cart[product_id]['quantity'] = quantity  # 수량 증가

        self.save()
    def save(self):
        self.session[settings.CART_ID] = self.cart
        self.session.modified = True

    # 주문 총 금액
    def get_product_total(self):
        return sum(item['price'] * item['quantity']
                   for item in self.cart.values())

    # 장바구니 제품 삭제
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del(self.cart[product_id])
            self.save()
