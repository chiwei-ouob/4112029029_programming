inventory={}
    # inventory是字典，每新增一組資料，key是item_name，value則是quantity
    
def add_item(item_name, quantity):
    if item_name in inventory:
        inventory[item_name]+=quantity
    else:
        inventory[item_name]=quantity
    # print(inventory)
def remove_item(item_name, quantity):
    if item_name in inventory and inventory[item_name]>=quantity:
        inventory[item_name]-=quantity
        if inventory[item_name]==0:
            del inventory[item_name]
    else:
        print("庫存不足或不存在。")

def view_inventory():
    for item, quantity in inventory.items():
        print(f"{item}: {quantity} ")

