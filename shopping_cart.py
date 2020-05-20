from statistics import median

class ShoppingCart:
    # write your code here
    def __init__(self, total=0, employee_discount=None, items=[]):
      self.total = total
      self.employee_discount = employee_discount
      self.items = items
    def add_item(self, name, price, quantity=1):
        for i in range(quantity):
            self.items.append({name: price})
        self.total = self.total + (price * quantity)
        return self.total
    def mean_item_price(self):
       return round(self.total / len(self.items), 2)

    def median_item_price(self):
        price_list = []
        for item in self.items:
            price_list.append(list(item.values())[0])
        price_list = sorted(price_list)
        return median(price_list)

    def apply_discount(self):
       if self.employee_discount:
           discount = self.total * (self.employee_discount / 100)
           return self.total - discount
       else:
           return 'Sorry, there is no discount to apploy to your cart :('

    def void_last_item(self):
        if len(self.items) > 0:
            last_item = self.items.pop()
            self.total -= list(last_item.values())[0]
        else:
            return 'There are no items in your cart!'
