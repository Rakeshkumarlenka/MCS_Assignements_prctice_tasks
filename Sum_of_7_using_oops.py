class Number:
    def _init_(self):
        print('processing the numbers')
    def process(self):
        num_seq = input('enter the numbers:').split(',')
        print(num_seq)
        order = []
        for i in num_seq:
            for j in i.split():
                if j.isdigit():
                    order.append(int(j))
        print(order)
        order2 = set(order)
        list1 = list(order2)
        list2 = list1
        print(list1, list2)
        tup = ()
        final = []
        for i in list1:
           for j in list2:
             if i + j == 7:
                tup = i, j
                final.append(tup)
                list2.remove(j)
        print("the required output ",final)

final = Number()
print(final.process())