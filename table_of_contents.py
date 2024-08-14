# table of contents solution
content_text = {
  "Toyota. Corolla": 3,
  "Honda. Civic and Accord": 33,
  "Honda. Legend": 35,
  "Skoda. Octavia": 133,
  "Volkswagen AG. Golf and Passat": 1013,
  "Volkswagen AG. Beetle": 1014,
  "Ford. Mustang": 1014,
  "Ferrari. F40": 1114,
  "Toyota. Supra": 1115,
}

content_receipt = {
    "Bread, 1pc": [99.89, 2],
    "Cheese, 10pc": [128.87, 4],
    "Cheese, 1KG": [178.01, 1.54],
    "Milk, 1L": [101.04, 5],
    "Potato, 1KG": [112.10, 4.59],
    "Wine, 1btl": [203.10, 3, 13],
    # "name": Milk""  [203.10, 3, 13],
}

product_list = [
    {"name": "Milk", "qty": "L", "price": 299, "amount": 2},
    {"name": "Bread", "qty": "pc", "price": 251, "amount": 3},
    {"name": "Cheese", "qty": "kg", "price": 100, "amount": 1.008},
    {"name": "Cheese slice", "qty": "pc", "price": 10, "amount": 7},
    {"name": "Potato", "qty": "kg", "price": 86.29, "amount": 3.780},
]
# for product in product_list:
#     print(product["name"])

# print(product_list[0]["name"])
# print(product_list[0]["price"])
width_page = 49
padding_symbol = "_"
content_len = len(content_text)
# title_text = f'My favorite cars({content_len})'
# print(f'{title_text.center(width_page, ".")}')
# print(padding_symbol*width_page)
# Single colum


def return_single_column():
    result = ""
    for key, value in content_text.items():
        # print(f"{key.ljust(1)} {padding_symbol.center(len_padding,padding_symbol)} {str(value).rjust(1)}")
        # print(f"{key.ljust(width_page-5, '-')}{str(value).rjust(5,'-')}")
        # print(f"{key.ljust(width_page - len(str(value)), '-')}{value}")
        # print(f"{key.ljust(width_page - len(str(value)) - 1, '-')}{str(value).rjust(len(str(value)) + 1, ' ')}")
        # result = result + f"{key.ljust(width_page - len(str(value)), '-')}{value}\n"
        result = f"{result}{key.ljust(width_page - len(str(value)), '-')}{value}\n"
        # result += f"{key.ljust(width_page - len(str(value)), '-')}{value}\n"
        # print(result)
    # print('-' * width_page)
    return result


# double column
def return_w_pad():
    if width_page % 2 == 0:
        w_pad = 2
    else:
        w_pad = 3
    return int(w_pad)


# def return_double_column():
#     result = ""
#     string = 1
#     for key, value in content_text.items():
#         if string % 2 == 0:
#             new_string = "\n"
#         else:
#             new_string = w_pad * " "
#         result = f"{result}{key.ljust(((width_page-w_pad)//2)-5,'_')}{str(value).rjust(5)}{new_string}"
#         string += 1
#     return result

# receipt
company_name = 'OOO "Roga i kopyta"'.upper().center(width_page)

# fixme: kopeyki dobavit(2 znaka posle ) , ves v KG and gramms (3 znaka)


# def return_receipt():
#     result = ""
#     gst = 10
#     total_gst = 0
#     total = 0
#     for key, value in content_receipt.items():
#         sum_item = round(value[0] * value[1], 2)
#         gst_item = round(sum_item * gst / 100, 2)
#         total = total + sum_item
#         total_gst = total_gst + gst_item
#         len_string = width_page // 2 - len(key)
#         name_price_weight = f"{key}{str(value[0]).rjust(len_string)} * {str(value[1])}"
#         total_product = f"= {sum_item} GST {gst}%".rjust(width_page - len(name_price_weight))
#         result = f"{result}{name_price_weight}{total_product}\n"
#     result = f"{company_name}\n{padding_symbol * width_page}\n{result}{padding_symbol * width_page }\n"
#     result = f"{result}{'Total to pay ='.ljust(20)}{str(round(total, 2)).rjust(width_page - 20)}\n"
#     gst_string = f"Including GST = {round(total_gst,2)}"
#     result = f" {result}{gst_string.rjust(width_page)}"
#     return result

def return_receipt():
    result = ""
    total = 0
    for product in product_list:
        product_description = product["name"]
        sum_products = product["price"] * product["amount"]
        total = total + sum_products
        len_string = width_page // 2 - len(product_description)
        print(len_string)
        product_qty = str(product["amount"]).rjust(len_string)
        name_price_weight = f'{product_description}{product_qty} x {product["price"]:.2f}'
        # name_price_weight = f'{product_description}{str(product_qty).rjust(len_string)} x {product["price"]:.2f}'
        total_product = f"= {sum_products:.2f}".rjust(width_page - len(name_price_weight))
        result = f"{result}{name_price_weight}{total_product}\n"
    result = f"{company_name}\n{padding_symbol * width_page}\n{result}{padding_symbol * width_page }\n"
    result = f"{result}{'Total to pay ='.ljust(20)}{str(round(total, 2)).rjust(width_page - 20)}\n"
    result = f" {result.rjust(width_page)}"
    return result


def return_receipt_v3():
    result = ""
    total_pay = 0
    column_w = round(width_page*0.20)
    for product in product_list:
        product_sum_price = round(product["price"] * product["amount"], 2)
        total_pay = total_pay + product_sum_price
        line_name = product["name"].ljust(width_page - 3 * column_w)
        line_qty = f'{product["amount"]:.3f} x '
        line_price = str(product["price"]).ljust(column_w)
        line_sum_price = f'= {product_sum_price:.2f}'
        result = f'{result}{line_name}{line_qty.rjust(column_w)}{line_price.ljust(column_w)}{line_sum_price.rjust(column_w)}\n'
    result = f"{company_name}\n{padding_symbol * width_page}\n{result}{padding_symbol * width_page }\n"
    result = f"{result}{'Total to pay ='.ljust(20)}{str(round(total_pay, 2)).rjust(width_page - 20)}\n"
    return result


print(return_receipt_v3())
# print(return_double_column())
# print(return_single_column())
# print_single_column(text)
