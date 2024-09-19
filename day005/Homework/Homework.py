#declaring variable name and give it variable value
#10% discount books
the_lord_of_rings = 50
harry_potter = 45
the_godfather = 55
vefxis_tkaosani = 60
don_quixote = 55

#20% discount books
galaktion_tabidze = 90
data_tutashxia = 75
the_life = 35
the_bible = 100
the_hobbit = 66

#declare discount value
discount1 = 10
discount2 = 20

#declaring variables after 10% discount on books
price_after_discount1 = the_lord_of_rings - the_lord_of_rings * discount1 // 100
price_after_discount2 = harry_potter - harry_potter * discount1 // 100
price_after_discount3 = the_godfather - the_godfather * discount1 // 100
price_after_discount4 = vefxis_tkaosani - vefxis_tkaosani * discount1 // 100
price_after_discount5 = don_quixote - don_quixote * discount1 // 100

#declaring variables after 20% discount on books
price_after_discount6 = galaktion_tabidze - galaktion_tabidze * discount2 // 100
price_after_discount7 = data_tutashxia - data_tutashxia * discount2 // 100
price_after_discount8 = the_life - the_life * discount2 // 100
price_after_discount9 = the_bible - the_bible * discount2 // 100
price_after_discount10 = the_hobbit - the_hobbit * discount2 // 100

#print created variables
#10% discount
print("10% discount")

print("the lord of rings price ->", price_after_discount1, str("gel"), 
      "harry potter price ->", price_after_discount2, str("gel"),
       "the_godfather price ->", price_after_discount3, str("gel"),
        "vefxis tkaosani price ->", price_after_discount4, str("gel"),
          "don quixote price ->", price_after_discount5, str("gel"))


#20% discount
print("20% discount")

print("galaktion tabidze price ->", price_after_discount6, str("gel"),"")
"data tutashxia price ->", price_after_discount7, str("gel"), 
"the life price ->", price_after_discount8, str("gel"),
"the bible price ->", price_after_discount9, str("gel"),
"the hobbit price ->", price_after_discount10, str("gel")