import unittest
from client import getDataPoint, getRatio


class UnitTest(unittest.TestCase):
  def test_getDataPoint(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2023-03-03 00:30:00.966511', 'top_bid': {'price': 100.86, 'size': 109}, 'id': '0.203415230156', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2023-03-03 00:30:00.966511', 'top_bid': {'price': 135.73, 'size': 81}, 'id': '0.203415230156', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))


  def test_getRatio(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2023-03-03 00:30:00.966511', 'top_bid': {'price': 100.86, 'size': 109}, 'id': '0.203415230156', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2023-03-03 00:30:00.966511', 'top_bid': {'price': 135.73, 'size': 81}, 'id': '0.203415230156', 'stock': 'DEF'}
    ]
    prices = {}
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      prices[stock] = price
    self.assertEqual(getRatio(prices["ABC"],prices["DEF"]), (prices["ABC"] / prices["DEF"]))


if __name__ == '__main__':
    unittest.main()
