def bonAppetit(bill, k, b):
    bill[k] = 0
    all_bill = sum(bill)
    per_person = int(all_bill / 2)
    if b > per_person:
        print(b - per_person)
    elif per_person == b:
        print('Bon Appetit')