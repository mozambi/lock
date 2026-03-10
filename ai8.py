class Client:
    def __init__(self,n,a,p):
        self.name = n
        self.address = a
        self.phone = p
    def place_order(self,order):
        print(f"Order placed by {self.name}:{order}")
class worker:
    def __init__(self,n,id):
        self.name = n
        self.id = id
    def take_order(self,client,order):
        print(f"Order taken by {self.name} (ID:{self.id}) from {client.name}:{order}")
class FoodItem:
    def __init__(self,n,pr):
        self.name = n
        self.price = pr
    def display(self):
        print(f"{self.name}:{self.price}")
client = Client("John","123 main st","123-456-7890")
work = worker("Alice","W001")
food = FoodItem("Pizza",10.99)
client.place_order("2 pizzas and 1 coke")
work.take_order(client,"2 pizzas and 1 coke")
food.display()
