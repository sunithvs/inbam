from django.shortcuts import render
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required

# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


@login_required(login_url='/accounts/login/')
def homepage(request):
    if request.method == 'POST':
        form = False
        if form.is_valid():
            order = form.save()
            print("form saved")
            currency = 'INR'
            razorpay_order = razorpay_client.order.create(dict(amount=order.price,
                                                               currency=currency,
                                                               payment_capture='0'))
            # order id of newly created order.
            razorpay_order_id = razorpay_order['id']
            callback_url = 'http://localhost:8000/payment/callback/'
            # we need to pass these details to frontend.
            context = {'razorpay_order_id': razorpay_order_id, 'razorpay_merchant_key': settings.RAZOR_KEY_ID,
                       'razorpay_amount': order.price, 'currency': currency, 'callback_url': callback_url,
                       "order": order}

            return render(request, 'payment/index.html', context=context)
    return HttpResponseBadRequest()


# checkout class view for handling checkout with authentication.

# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def payment_handler(request):
    # only accept POST request.
    if request.method == "POST":
        try:
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }

            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                amount = 20000  # Rs. 200
                try:

                    # capture the payment
                    razorpay_client.payment.capture(payment_id, amount)

                    # render success page on successful capture of payment
                    return render(request, 'paymentsuccess.html')
                except Exception as e:
                    print(e)
                    # if there is an error while capturing payment.
                    return render(request, 'paymentfail.html')
            else:
                # if signature verification fails.
                return render(request, 'paymentfail.html')
        except Exception as e:
            print(e)
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
        # if other than POST request is made.
        return HttpResponseBadRequest()
