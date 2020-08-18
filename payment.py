from requests import post,get 
import json


class Paystack:
    def __init__(self, api_key='', amount='', customer_email='', ref='',nuban='',bankcode=''):
        self.api_key = api_key
        self.amount = amount
        self.customer_email = customer_email
        self.ref = ref
        self.nuban = nuban
        self.bankcode = bankcode

    def initialize(self):

        h = {
            "Authorization":"Bearer "+self.api_key,
            "Content-Type": "application/json"

        }
        body = {"email":self.customer_email,"amount":self.amount}

        response=post('https://api.paystack.co/transaction/initialize',data=json.dumps(body),headers=h)
        #this will return a transaction url that you will return users to and a transaction id
        return response.text

    
    def verify_tx(self):
        h = {
            "Authorization":"Bearer "+self.api_key
        }
        response = get('https://api.paystack.co/transaction/verify/'+self.ref, headers=h)
        # you will set a cron job or a webhook that check if the transaction is successfull
        # if yes, then you credit the wallet of the user the tx belongs to 
        return response.text

    # def verify_account(self):
    #     h = {
    #         "Authorization":"Bearer "+self.api_key
    #     }
    #     response = get("https://api.paystack.co/bank/resolve?account_number="+self.nuban+'&bank_code'=self.bankcode, headers=h)
    #     return response
    def get_allBanks(self):
        h = {
            "Authorization":"Bearer "+self.api_key
             }
        response = get('https://api.paystack.co/bank',headers=h)
        return response.text






sk='sk_test_a5eb62a5b7549366c45b4d9dc89fa4eeadfe30ca'




# tx=Paystack(sk,'3000','dspirit118@gmail.com')
# tx.ref = 't5xg07o4o5'
# a=tx.initialize()
# b = tx.verify_tx()
p=Paystack()
p.api_key=sk
print(p.get_allBanks())


