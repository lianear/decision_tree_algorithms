import csv
import random
from faker import Faker

fake = Faker()
us_faker = Faker('en_US')

RECORD_COUNT = 1000000

def writeTo_csv():
    #print('starting func')
    with open('loan_applications.csv', 'w', newline='') as csvfile:
        fieldnames = ['ID','Firstname', 'Surname', 'Address', 'Postcode', 'Phone', 'CreditScore', 'Income', 'DTI', 'Approved']
        seed = 0
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        #print('header written')
        for i in range(RECORD_COUNT):
            #print('printing row' + str(i))
            seed += 1
            creditscore = random.randint(350,800)
            minIncome = 0
            income = random.randint(15000,200000)
            dti = random.random() * .5
            approved = 1

            if(dti > 0.36):
                approved = 0
            else:
                if creditscore < 600:
                    minIncome = 100000
                elif creditscore < 700:
                    minIncome = 50000
                else:
                    minIncome = 20000
                if income < minIncome:
                    approved = 0
                


            writer.writerow({"ID": seed, "Firstname": us_faker.first_name(), \
                "Surname": us_faker.last_name(), \
                "Address": us_faker.address().replace("\n", ", "), \
                "Postcode": us_faker.postcode(), \
                "Phone": f'+1 {fake.msisdn()[3:]}', \
                'CreditScore': creditscore, \
                'Income': income, \
                'DTI': dti, \
                'Approved': approved})

            if (i % 1000 == 0):
                print('Progress: ' + str(i))
    print('finished')

def main():
    writeTo_csv()

if __name__ == '__main__':
    main()