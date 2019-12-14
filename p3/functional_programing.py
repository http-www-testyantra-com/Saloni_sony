# def add(sal):
#     return sal+sal*(10/100)
#
# print(add(10000))
#
# add = lambda sal:sal+sal*(10/100)
# print(add(10000))

# click
# do_click = lambda element_property:element_property.click()
# do_click("element")

# send_keys
# do_send_keys = lambda element_property,data:element_property.send_keys("data")
# do_send_keys("element","data")

# print(list(filter(lambda n:n%2 == 0,[1,2,3,4,5,6,7,8])))

# alpha = list(filter(lambda ch:(ch>='a' and ch <='z')or(ch>='A' and ch<='Z'),"Hello362"))
# print(alpha)

#perfect square

print(list(filter(lambda n:n**0.5%1 == 0,range(1,100))))

# special chars
alpha = list(filter(lambda ch:ch in "!@#$%^&*","Hello362%$#@"))
print(alpha)

#convert list of strings to upper case
def upper(str):
    return str.upper()
print(list(map(upper,["hello","world"])))

#duplicate in a given string
print(list(filter(lambda ch:ch,"hellollol")))








