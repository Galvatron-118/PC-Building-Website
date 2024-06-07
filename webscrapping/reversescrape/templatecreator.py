import webbrowser
import csv
import os

# open blank file
f = open('template.html', 'w')


with open('./partsdemo.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        name = row[0]
        price = row[1]
        stock = row[2]

        message = """
                        <tr class="tr__product" data-pb-id="329297"><td class="td__name"><a href="/product/g94BD3/amd-ryzen-5-5600x-37-ghz-6-core-processor-100-100000065box"><div class="td__imageWrapper"> <div class="td__image"><img alt="AMD Ryzen 5 5600X" src="//cdna.pcpartpicker.com/static/forever/images/product/3ef757133d38ac40afe75da691ba7d60.256p.jpg"><div class="td__image--lg"><img alt="AMD Ryzen 5 5600X" src="//cdna.pcpartpicker.com/static/forever/images/product/3ef757133d38ac40afe75da691ba7d60.256p.jpg"></div></div></div></a></td>     
                            <div class="product"><td class="product_name">"""+name+"""</td>
                                <td></td>
                                <td></td>
                                <td class="product_price">"""+price+"""</td>
                                <td><button class="learn-more-btn">"""+stock+"""</button></td>
                            </div> 
                        </tr>
                        
                            """

        # write to file
        f.write(message)

# close file
f.close()

# open in browser
filename = 'template.html'
webbrowser.open_new_tab(filename)