import test, time



def algorithm():
    m1 = 0
    a1 = 20
    a2 = 80
    bal = 1
    pos = 0
    for m2 in test.generate():
        if m2 >= m1+a2:
            print('Closed at ${}.'.format(m2))
            print('----------------------------------')
            print('Profit of ${}.'.format((abs(m2)*bal)-((abs(m2)*bal)//3)))
            time.sleep(3)
            break
        elif m2 >= m1 and m2 < m1+a2:
            if m2 >= m1+a1:
                if pos == 0:
                    continue
                else:
                    pos = 0
                    bal *= 3
            else:
                continue
        elif m2 < m1 and m2 > m1-a2:
            if m2 <= m1-a1:
                if pos == 1:
                    continue
                else:
                    pos = 1
                    bal *= 3
            else:
                continue
        elif m2 <= m1-a2:
            print('Closed at ${}.'.format(m2))
            print('----------------------------------')
            print('Profit of ${}.'.format((abs(m2)*bal)-((abs(m2)*bal)//3)))
            time.sleep(3)
            break


test.plot()
algorithm()
