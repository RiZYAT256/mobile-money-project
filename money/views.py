from django.core.checks import messages
from django.shortcuts import render,redirect
from money.forms import AgentForm
from .models import Agent, Deposit
from money.forms import CustomerForm
from .models import Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Withdraw
from money.forms import WithdrawForm
from .models import Deposit
from money.forms import DepositForm
from money.forms import TransferForm
from .models import Transfer
from money.forms import TransactionForm
from .models import Transaction
from django.contrib.auth import logout
from django.shortcuts import redirect



@login_required
def index_view(request):
    return render(request, 'index.html')

@login_required
def money_list_view(request):
    transactions = [
        {
            "type": "Deposit",
            "customer": deposit.customer,
            "sender": None,
            "receiver": None,
            "agent": deposit.agent,
            "amount": deposit.amount,
            "date": deposit.date,
        }
        for deposit in Deposit.objects.select_related("customer", "agent")
    ]
    transactions.extend(
        {
            "type": "Withdraw",
            "customer": withdraw.customer,
            "sender": None,
            "receiver": None,
            "agent": withdraw.agent,
            "amount": withdraw.amount,
            "date": withdraw.date,
        }
        for withdraw in Withdraw.objects.select_related("customer", "agent")
    )
    transactions.extend(
        {
            "type": "Transfer",
            "customer": None,
            "sender": transfer.sender,
            "receiver": transfer.receiver,
            "agent": None,
            "amount": transfer.amount,
            "date": transfer.date,
        }
        for transfer in Transfer.objects.select_related("sender", "receiver")
    )
    transactions.sort(key=lambda transaction: transaction["date"], reverse=True)
    return render(request, "money_list.html", {"transactions": transactions})

@login_required
def add_agent_view(request):
    message = ''
    if request.method == "POST":
        agent_form = AgentForm(request.POST)

        if agent_form.is_valid():
            agent_form.save()

            message = "Agent Added Successfully"
    else:
        agent_form = AgentForm()

    agents = Agent.objects.all()    

    context = {
        'form':agent_form,
        'message': message,
        'agents' :agents,
    }
    
    return render(request, "add_agent.html",context)

@login_required
def edit_agent_view(request, agent_id):
    agent = Agent.objects.get(id=agent_id)
    message = ""

    if request.method == "POST":
        agent_form = AgentForm(request.POST, instance=agent)

        if agent_form.is_valid():
            agent_form.save()
            message = "Agent Updated"
        else:
            message = "Invalid Data"
    else:
        agent_form = AgentForm(instance=agent)

    context = {
        'form': agent_form,
        'agent': agent,
        'message': message,
    }

    return render(request, "edit_agent.html", context)

@login_required
def delete_agent_view(request,agent_id):
    agent = Agent.objects.get(id=agent_id)

    agent.delete()

    return redirect (add_agent_view)

@login_required
def add_customer_view(request):
    message = ""

    if request.method == "POST":
        customer_form = CustomerForm(request.POST)

        if customer_form.is_valid():
            customer_form.save()
            message = "Customer Added Successfully"
            customer_form = CustomerForm()  
    else:
        customer_form = CustomerForm()
        agent_form = AgentForm()
    
    
    agents = Agent.objects.all()
    customers = Customer.objects.all()
    context = {
        'form': customer_form,
        'message': message,
        'customers': customers,
        'agents': agents
    }
    return render(request, 'add_customer.html', context)

@login_required
def edit_customer_view(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    message = ""

    if request.method == "POST":
        customer_form = CustomerForm(request.POST, instance=customer)

        if customer_form.is_valid():
            customer_form.save()
            message = "Customer Updated"
        else:
            message = "Invalid Data"
    else:
        customer_form = CustomerForm(instance=customer)

    context = {
        'form': customer_form,
        'customer': customer,
        'message': message,
    }

    return render(request, "edit_customer.html", context)


@login_required
def delete_customer_view(request,customer_id):
    customer = Customer.objects.get(id=customer_id)

    customer.delete()

    return redirect (add_customer_view)


@login_required
def withdraw_view(request):
    message = ""

    if request.method == "POST":
        withdraw_form = WithdrawForm(request.POST)
        if withdraw_form.is_valid():
            withdraw_form.save()
            message = "Withdraw Successful"
            withdraw_form = WithdrawForm()
    else:       
        withdraw_form = WithdrawForm()

    withdraws = Withdraw.objects.all()    

    context = {
        'form':withdraw_form,
        'message': message,
        'withdraws' :withdraws,
    }
    
    return render(request, "withdraw.html", context) 
 

@login_required
def edit_withdraw_view(request,withdraw_id):
    withdraw = Withdraw.objects.get(id=withdraw_id)
    message = ""
    
    if request.method == "POST":
            
        withdraw_form = WithdrawForm(request.POST, instance=withdraw)
    
        if withdraw_form.is_valid():
            withdraw_form.save()
            message = "Withdraw Updated"
        else:
            message = "Invalid"
    else:
        withdraw_form = WithdrawForm(instance=withdraw)
    
    context = {
        'form': withdraw_form,
        'withdraw': withdraw,
        'message': message,
    }
    
    return render(request, "edit_withdraw.html", context)


@login_required
def delete_withdraw_view(request,withdraw_id):
    withdraw = Withdraw.objects.get(id=withdraw_id)
    
    withdraw.delete()

    return redirect (withdraw_view)

@login_required
def deposit_view(request):
    message = ""

    if request.method == "POST":
        deposit_form = DepositForm(request.POST)
        if deposit_form.is_valid():
            deposit_form.save()
            message = "Deposit Successful"
            deposit_form = DepositForm()
    else:       
        deposit_form = DepositForm()

    deposit = Deposit.objects.all()    

    context = {
        'form':deposit_form,
        'message': message,
        'deposits': deposit,
    }
    
    return render(request, "deposit.html", context) 

@login_required
def edit_deposit_view(request,deposit_id):
    deposit = Deposit.objects.get(id=deposit_id)
    message = ""
    
    if request.method == "POST":
            
        deposit_form = DepositForm(request.POST, instance=deposit)
    
        if deposit_form.is_valid():
            deposit_form.save()
            message = "Deposit Updated"
        else:
            message = "Invalid"
    else:
        deposit_form = DepositForm(instance=deposit)
    
    context = {
        'form': deposit_form,
        'deposit': deposit,
        'message': message,
    }
    
    return render(request, "edit_deposit.html", context)


@login_required
def delete_deposit_view(request,deposit_id):
    deposit = Deposit.objects.get(id=deposit_id)
    
    deposit.delete()

    return redirect (deposit_view)


def logout_view(request):
    logout(request)
    return redirect('login_page')

def sign_up_view(request):
    if request.method == "POST":
        sign_up_form = UserCreationForm(request.POST)

        if sign_up_form.is_valid():
            sign_up_form.save()
            message = "User Created Successfully"
        else:
            message = "Invalid Data"
    else:
        sign_up_form = UserCreationForm()

    context = {
        'form': sign_up_form,
    }

    return render(request, 'registration/sign_up.html', context)

@login_required
def transfer_view(request):
    message = ""

    if request.method == "POST":
        transfer_form = TransferForm(request.POST)
        if transfer_form.is_valid():
            transfer_form.save()
            message = "Successful"
            transfer_form = TransferForm()
    else:       
        transfer_form = TransferForm()

    transfers = Transfer.objects.all()    

    context = {
        'form':transfer_form,
        'message': message,
        'transfers' :transfers,
    }
    
    return render(request, "transfer.html", context)


@login_required
def edit_transfer_view(request,transfer_id):
    transfer = Transfer.objects.get(id=transfer_id)
    message = ""
    
    if request.method == "POST":
            
        transfer_form = TransferForm(request.POST, instance=transfer)
    
        if transfer_form.is_valid():
            transfer_form.save()
            message = "Transfer Updated"
        else:
            message = "Invalid"
    else:
        transfer_form = TransferForm(instance=transfer)
    
    context = {
        'form': transfer_form,
        'transfer': transfer,
        'message': message,
    }
    
    return render(request, "edit_transfer.html", context)

@login_required
def delete_transfer_view(request,transfer_id):
    transfer = Transfer.objects.get(id=transfer_id)
    
    transfer.delete()

    return redirect (transfer_view)

@login_required
def transaction_view(request):
    message = ""
    if request.method == "POST":
        transaction_form = TransactionForm(request.POST)
        if transaction_form.is_valid():
            transaction_form.save()
            message = "Transaction Successful"
            transaction_form = TransactionForm()
    else:       
        transaction_form = TransactionForm()

    transactions = Transaction.objects.all()    

    context = {
        'form':transaction_form,
        'message': message,
        'transactions' :transactions,
    }
    
    return render(request, "transaction.html", context)


