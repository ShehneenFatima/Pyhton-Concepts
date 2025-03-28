class InsufficientBalanceError(Exception):
      def __init__(self,message = "Insufficient balance to perform this operation"):
          self.message = message
          super().__init__(self.message)


#function to simulate a  bank transaction
def withdraw(amount, balance):
   try:
      if amount > balance:
        raise InsufficientBalanceError(f"Cannot withdraw {amount}.Available balance : {balance}")
      balance -= amount
      print(f"Withdrawal successful! New balance:{balance}")
   except InsufficientBalanceError as e :
      print (f"Error: {e}")

#Testing the custom exception

withdraw(500,300) #it should raise exception
withdraw(100,300) #should succeed
