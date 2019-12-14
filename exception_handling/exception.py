def value():
    try:
        a = int(input("enter a value"))
        b = int(input("enter b value"))
        return a,b
    except ValueError as e:
        print(e)
        return value()
    finally:
        print("finally of value")

def div(a,b):
    try:
        c = a/b
        return c
    except ZeroDivisionError as e:
        print(e)
    finally:
        print("finally of div")

def main():
    try:
        a,b = value()
        c= div(a,b)
        print(c)
    except ZeroDivisionError as e:
        print(e)
        main()
    except ValueError as e:
        print(e)
        main()
    except Exception as e:
        print(e)
        main()
    except:
        print("exception is arrised")
    finally:
        print("successfully completed")

if __name__ == '__main__':
    main()



# if try,except,finally have return statement then in buffer memory finally value get over
#ridden by try block value
# def smaple():
#   try:
#       return 10
#   except:
#       return 20
#   finally:
#       return 30
# print(smaple())
