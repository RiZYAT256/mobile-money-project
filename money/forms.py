from django.forms import ModelForm

from money.models import Agent,Deposit,Withdraw,Customer,Transfer,Transaction

class AgentForm(ModelForm):
    class Meta:
        model = Agent
        fields = '__all__'

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class DepositForm(ModelForm):
    class Meta:
        model = Deposit
        fields = '__all__'

class WithdrawForm(ModelForm):
    class Meta:
        model = Withdraw
        fields = '__all__'

class TransferForm(ModelForm):
    class Meta:
        model = Transfer
        fields = '__all__'

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'



