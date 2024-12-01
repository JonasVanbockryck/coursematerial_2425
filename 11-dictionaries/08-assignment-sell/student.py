def sell(stock, model):
    # if model appears in stock. this searches through our dictionary based on a given key. 
    if model in stock: 
        # reduces stock by 1
        stock[model] -= 1
        # then if we don't have any more stock, delete stock.
        if stock[model] == 0:
            del stock[model]
    
    return stock