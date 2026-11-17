from django.db import models

class Agent(models.Model):

    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        return self.name

class Deposit(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE
    )
    agent = models.ForeignKey(
        Agent, on_delete=models.CASCADE
    )    
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Deposit - {self.amount}"

class Withdraw(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete = models.CASCADE
    )
    agent = models.ForeignKey(
        Agent, on_delete=models.CASCADE
    )
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Withdraw - {self.amount}"

class Transfer(models.Model):
    sender = models.ForeignKey(
        Customer, on_delete = models.CASCADE,
        related_name="sent_transfers"
    )
    receiver = models.ForeignKey(
        Customer, on_delete=models.CASCADE,
        related_name="received_transfers"
    )
    date = models.DateTimeField(
        auto_now_add=True
    )
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    def __str__(self):
        return f"Transfer - {self.amount}"

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ("Deposit","Deposit"),
        ("Withdraw", "Withdraw"),
        ("Transfer", "Transfer"),
    ]

    Transaction_type = models.CharField(
        max_length=20,
        choices=TRANSACTION_TYPES
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.Transaction_type