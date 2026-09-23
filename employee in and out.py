class e:

    def __init__(self):
        print('employee created')

    def __del__(self):
        print("destructor called")

def co():
    print('making object...')
    o = e()
    print('function end...')
    return o

print('calling create_obj() function...')
o = co
print('program end...')