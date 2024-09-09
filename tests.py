def calculate_total(products):
    total = 0

    for product in products:
        total += product["price"]*(1 - product["disccount"]/100) 
    return total

def test_calculate_total_with_empty_list():
    assert calculate_total([]) == 0

def test_calculate_total_with_single_product():
    products=[
        {
            "name" : "Notebook", 
            "price" : 5,
            "disccount" : 10
        }
    ]
    assert calculate_total(products) == 4.5

def test_calculate_total_with_multiple_product():
    products=[
        {
            "name" : "Notebook", 
            "price" : 10,
            "disccount" : 10
        },
        {
            "name" : "Pen", 
            "price" : 2,
            "disccount" : 10
        }
    ]
    assert calculate_total(products) == 10.8

if __name__ == "__main__":
    test_calculate_total_with_empty_list()  # This will run the test    
    test_calculate_total_with_single_product()
    test_calculate_total_with_multiple_product()