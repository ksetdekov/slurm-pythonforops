from copy import copy


if __name__ == '__main__':
    payment_amount = 2000
    payment_amount += 1000
    copy_of_payment_amount = payment_amount

    print(payment_amount * 0.1)
    print(payment_amount)
    print(copy_of_payment_amount)

    payment_amount +=10

    print(payment_amount)
    print(copy_of_payment_amount)
