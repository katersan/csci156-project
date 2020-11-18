recordsDict = {} 
currentID = 1
#idd is ID
class ShoppingCart():
    def __init__(self,palettes,lipstick,blush,mascara):
        self.total = 0
        self.items = {}
        self.palettes = palettes
        self.lipstick = lipstick
        self.blush = blush
        self.mascara = mascara
        
    def add_item(self,idd,quantity,price):
        self.total = quantity * price
        self.items = {idd:quantity}
    
    def del_item():
        self.total -= quantity * price
        if quantity > self.items:
            print('Wanted value is above item stock!')
            return self.total

    def checkout():
        pass
    
class Palettes(ShoppingCart):
    def __init__(self,natural,colorful,punk):
        self.natural = natural
        self.colorful = colorful
        self.punk = punk
class Lipstick(ShoppingCart):
    def __init__(self,liquid,velvet,matte,gloss):
        self.liquid = liquid
        self.velvet = velvet
        self.matte = matte
        self.gloss = gloss

def order():
    orderList = []
    ID = 1
    subtotal = 0
    while True:
        makeup_artist = input('Enter makeup artist name: ')
        print_by_makeup_artist(makeup_artist)
        name = input('Type makeup brand name: ')
        makeup_artist = recordsDict[name][1]
        price = recordsDict[name][3]
        quantity = recordsDict[name][4]
        if quantity == 0:
            print('Not in the stock')
            continue
        recordsDict[name][4] -= 1
        orderList.append([name, makeup_artist, price])
        subtotal += price
        cont = input('Continue? Press Y: ')
        if cont != 'Y':
            break

    print('---Bill---')
    for order in orderList:
        print(ID, order[0], order[1], order[2])
    print('4% sales tax: ', 0.48*subtotal)
    print('Total: ', subtotal + 0.48*subtotal)

def create_product():
    productname = input('Enter makeup product: ')
    fout = open(productname, 'w')
    fout.close()
    return productname

def buy_product():
    pass

def main():
    option = ''
    # menu
    state = 'BEGIN'
    while True:
        # BEGIN STATE
        if state == 'BEGIN':
            print('Q: Quit\tC: Create\tL: Load')
            option = input('Select the option: ')
            if option == 'Q':
                # END STATE
                break
            elif option == 'C':
                productname = create_product()
                state = 'WORKSPACE'
            elif option == 'L':
                productname = load_from_product()
                state = 'WORKSPACE'
        elif state == 'WORKSPACE':
            # WORKSPACE
            print('WORKSPACE: ', productname)
            print('A:Add\tS:Save\tM:Modify:\tO:Order\tT:Total\tP:Print')
            option = input('Select the option: ')

main()
