import os
from flask import Flask, render_template, request
import stripe


stripe_keys = {
    'secret_key': os.environ['sk_test_51MQxFEJ5tRjRTacrz9gGG59UuAKP9aTmgB5BjmnkYNeoUJM2fztQG8zBaPA5jDzp3pzU2ZCj3XbRKupa0JB95gyf00s1DMClm2'],
    'publishable_key': os.environ['pk_test_51MQxFEJ5tRjRTacrmRceeme6orRxRCrfUEN4uVOgig3BkbfjzXy03qVi7HHNuhOP7eR4HQACcK9k5JWrvbwCeuQ100Xi9kLoS7']
}

stripe.api_key = stripe_keys["secret_key"]

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', key=stripe_keys['publishable_key'])


@app.route('/charge', methods=['POST'])
def charge():
    # Amount in cents
    amount = 500

    customer = stripe.Customer.create(
        email='customer@example.com',
        source=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='sgd',
        description='Flask Charge'
    )

    return render_template('charge.html', amount=amount)



if __name__ == '__main__':
    app.run(debug=True)
