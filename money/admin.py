from django.contrib import admin
from .models import (Agent,Customer,Deposit,Withdraw,Transfer,Transaction)

admin.site.site_header = "Mobile Money Admin"
admin.site.site_title = "Mobile Money Admin"
admin.site.index_title = "Dashboard"


class AgentAdmin(admin.ModelAdmin):
    list_display = ('id','name','phone_number','location')
    search_fields = ('name','phone_number','location')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','phone_number','balance')
    search_fields = ('name','phone_number','balance')

class DepositAdmin(admin.ModelAdmin):
    list_display = ('customer','agent','amount','date')
    search_fields = ('customer','agent','amount','date')

class WithdrawAdmin(admin.ModelAdmin):
    list_display = ('customer','agent','amount','date')
    search_fields = ('customer','agent','amount','date')

class TransferAdmin(admin.ModelAdmin):
    list_display = ('sender','receiver','amount','date')
    search_fields = ('sender','receiver','amount','date')

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('Transaction_type', 'amount', 'date')
    search_fields = ('Transaction_type',)

admin.site.register(Agent)
admin.site.register(Customer)
admin.site.register(Deposit)
admin.site.register(Withdraw)
admin.site.register(Transfer)
admin.site.register(Transaction, TransactionAdmin)









