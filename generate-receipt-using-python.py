from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle 
from reportlab.lib import colors 
from reportlab.lib.pagesizes import A4 
from reportlab.lib.styles import getSampleStyleSheet 

num_rows = int(input("Enter number of rows: "))
data = [["Date", "Product", "Quantity", "price per unit","Price (Rs.)"]]

subtotal = 0
for i in range(num_rows):
    date = input("Enter Date for row {}: ".format(i+1))
    product = input("Enter Product Name for row {}: ".format(i+1))
    quantity = float(input("Enter Quantity for row {}: ".format(i+1)))
    priceperqty = float(input("Enter Price (Rs.) per unit for row {}: ".format(i+1)))
    price = priceperqty*quantity
    subtotal += price
    data.append([date, product, quantity, "{:,.2f}/-".format(priceperqty),"{:,.2f}/-".format(price)])

discount = float(input("Enter Discount % : "))
total = subtotal - (discount * subtotal)/100

data += [
    ["Sub Total", "", "", "", "{:,.2f}/-".format(subtotal)],
    ["Discount", "", "", "", "-{:,.2f}/-".format(discount)],
    ["Total", "", "", "", "{:,.2f}/-".format(total)]
]

pdf = SimpleDocTemplate("receipt.pdf", pagesize=A4) 

styles = getSampleStyleSheet() 

title_style = styles["Heading1"] 

title_style.alignment = 1

title = Paragraph("ABC COMPANY - reciept ", title_style) 

style = TableStyle( 
    [ 
        ("BOX", (0, 0), (-1, -1), 1 , colors.black), 
        ("GRID", (0, 0), (4 , 4), 1 , colors.black), 
        ("BACKGROUND", (0, 0), (4, 0), colors.gray), 
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke), 
        ("ALIGN", (0, 0), (-1, -1), "CENTER"), 
        ("BACKGROUND", (0 , 1), (-1 , -1), colors.beige), 
    ] 
) 

table = Table(data, style=style) 

pdf.build([title, table])
