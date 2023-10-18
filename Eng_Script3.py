# William Eng
# weng2@oakland.edu
# video game inventory

def display_inventory(inventory):
    total = 0
    print('-----Inventory-----')
    # need list to order, convert from dictionary
    keys=list(inventory.keys())
    keys.sort()
    # create new dictionary that has keys is sorted order
    sortedInventory={}
    for i in range(len(keys)):
        sortedInventory[keys[i]]=inventory.get(keys[i])
    for k,v in sortedInventory.items():
        print("{}\t\t{}".format(v,k))
        total += v
    print('Total number of items: {}'.format(total))

def update_inventory(inventory, add_items):
    total = 0
    print('-----Inventory-----')
    # Add new item types to our inventory
    # Set default as 0 if no item
    for i in add_items:
        inventory.setdefault(i,0)
    # need list to be ordered, convert from dictionary
    keys=list(inventory.keys())
    keys.sort()
    # create new dictionary that has keys is sorted order
    sortedInventory={}
    for i in range(len(keys)):
        sortedInventory[keys[i]]=inventory.get(keys[i])    
    for k,v in sortedInventory.items():
        # increment for each item added to the inventory
        for i in add_items:
            if k == i:
                v += 1
        print("{}\t\t{}".format(v,k))
        total += v
    print('Total number of items: {}'.format(total))


inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

display_inventory(inventory)
update_inventory(inventory, dragon_loot)
