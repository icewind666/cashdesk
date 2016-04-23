#coding: utf-8
import json, sys, datetime
from django.db import models

# Create your models here.
class FinancialOperation(models.Model):
    datetime = models.DateTimeField(u'Дата')
    amount = models.FloatField(u'Сумма')
    isSpent = models.BooleanField(u'Расходная операция')
    comment = models.TextField(max_length = 500)
    
    @staticmethod
    def get_remainder():
        remainder = 0.0
        for x in FinancialOperation.objects.all():
            if x.isSpent:
                remainder -= x.amount
            else:
                remainder += x.amount
        return remainder
    
    def remainder_amount(self):
        remainder = 0.0
                
        for x in FinancialOperation.objects.all():
            if x.isSpent:
                remainder -= x.amount
            else:
                remainder += x.amount
        return remainder

    
    def __unicode__(self):
        return self.datetime.isoformat() + ' -> ' + str(self.amount) + '. ' + self.comment
    
    def toJSON(self):
        try:
            dictForJson = {"datetime":self.datetime.isoformat(), "amount":self.amount, 
                       "isSpent":self.isSpent, "comment":self.comment}
        except Exception as e:
            print(e.message)
            print(e.__doc__)
            
        return json.dumps(dictForJson)
    
    def toDict(self):
        try:
            dictForJson = {"datetime":self.datetime.isoformat(), "amount":self.amount, 
                       "isSpent":self.isSpent, "comment":self.comment}
        except Exception as e:
            print(e.message)
            print(e.__doc__)
            
        return dictForJson
        
        