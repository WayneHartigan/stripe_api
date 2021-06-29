import os
import stripe

stripe.api_key = os.environ['STRIPE_SECRET_KEY']

# balance = stripe.Balance.retrieve()
# print(balance)

resp = stripe.Charge.create(
  amount=2000,
  currency="eur",
  source="tok_mastercard",
  description="My First Test Charge (created for API docs)",
)
# print(resp)

# balance = stripe.Balance.retrieve()
# print(balance)

stripe.Charge.modify(
  resp['id'],
  metadata={"order_id": "1958"},
)

get_resp = stripe.Charge.retrieve(resp['id'])
# print(get_resp)
print(stripe.Charge.list())
# stripe.Charge.capture(resp['id'])
