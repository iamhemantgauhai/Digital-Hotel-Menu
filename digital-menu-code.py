print('''
      Welcome to Gauhai's Hotel
      गौहाई के होटल में आपका स्वागत है''')
a=True
while a==True:
    user=int(input('''
                   1:Breakfast 2:Lunch 3:Snack 4:Dinner
                   Order Number Please: '''))
    if user==1:
        user1=int(input('''
                        1:Tea 2:Dal ka Paratha 3:Namkeen Seviyaan 4:Aloo Paratha 5:Bread Pakora
                        Order Number Please: '''))
        if user1==1:
            print('''
                  10rs''')
            back=input('''
                       Any more order? (yes/no) : ''')
            if back!='''yes''':
                a=False
        elif user1==2:
            print('''
                  20rs half plate, 40rs full plate''')
            back=input('''
                       Any more order? (yes/no) : ''')
            if back!='''yes''':
                a=False
        elif user1==3:
            print('''
                  30rs half plate, 5ors full plate''')
            back=input('''Any more order? (yes/no) : ''')
            if back!='''yes''':
                a=False
        elif user1==4:
            print('''40rs half plate, 70rs full plate''')
            back=input('''Any more order? (yes/no) : ''')
            if back!='''yes''':
                a=False
        elif user1==5:
            print('''20rs half plate, 40rs full plate''')
            back=input('''Any more order? (yes/no) : ''')
            if back!='''yes''':
                a=False
        else:
            print('''invalid input''')
            back=input('''Any more order? (yes/no) : ''')
            if back!='''yes''':
                a=False
            back=input('''Any more order? (yes/no) : ''')
            if back!='''yes''':
                a=False
    elif user==2:
        print('''
              1:Chole bhature 2:Kadhi Rice 3:Biryani 4:Rajma Rice 5:Dal Makhani''')
        user1=int(input('''
                        Order Number Please: '''))
        if user1==1:
            print('''
                  50rs per plate''')
            back=input('''
                       Any more order? (yes/no) : ''')
            if back!='''yes''':
                a=False
        elif user1==2:
            print('''
                  half plate 40rs, full plate 70rs''')
            back=input('''
                       Any more order? (yes/no) : ''')
            if back!='''yes''':
                a=False
        elif user1==3:
            print('''
                  80rs per plate''')
            back=input('''
                       Any more order? (yes/no) : ''')
            if back!='''yes''':
                a=False
        elif user1==4:
            print('''
                  half plate 50rs, full plate 80rs''')
            back=input('''
                       Any more order? (yes/no) : ''')
            if back!='''yes''':
                a=False
        elif user1==5:
            print('''
                  60rs per plate''')
            back=input('''
                       Any more order? (yes/no) : ''')
            if back!='''yes''':
                a=False
        else:
            print('''
                  invalid input''')
            back=input('''
                       Any more order? (yes/no) : ''')
            if back!='''yes''':
                a=False
    elif user==3:
        print('''
              1:Dal Ki Kachori 2:Bonda 3:Dahi vada 4:Halva 5:Momo''')
        user1=int(input('''
                        Order Number Please: '''))
        if user1==1:
            print('''
                  25rs per plate''')
            back=input('''
                       Any more order? (yes/no) : ''')
            if back!='''yes''':
                a=False
        elif user1==2:
            print('''
                  99rs medium size''')
            back=input('''
                       Any more order? (yes/no) : ''')
            if back!='''yes''':
                a=False
        elif user1==3:
            print('''
                  20rs per cup''')
            back=input('''
                       Any more order? (yes/no) : ''')
            if back!='''yes''':
                a=False
        elif user1==4:
            print('''
                  half plate 30rs, full plate 50rs''')
            back=input('''
                       Any more order? (yes/no) : ''')
            if back!='''yes''':
                a=False
        elif user1==5:
            print('''
                  30rs''')
            back=input('''
                       Any more order? (yes/no) : ''')
            if back!='''yes''':
                a=False
        else:
            print('''
                  invalid input''')
            back=input('''
                       Any more order? (yes/no) : ''')
            if back!='''yes''':
                a=False
    elif user==4:
        print('''
              1:Butter Chicken Roti 2:Chicken Korma Roti 3:Fish Roti 4: Tandoori Chops Roti 5:Egg Roti''')
        user1=int(input('''
                        Order Number Please: '''))
        if user1==1:
            print('''
                  4 eggs 4 roti 100rs plate''')
            back=input('''
                       Any more order? (yes/no) : ''')
            if back!='''yes''':
                a=False
        elif user1==2:
            print('''
                  half plate chicken 4 roti 150rs plate''')
            back=input('''
                       Any more order? (yes/no) : ''')
            if back!='''yes''':
                a=False
        elif user1==3:
            print('''
                  half plate mutton 4 roti 200rs plate''')
            back=input('''
                       Any more order? (yes/no) : ''')
            if back!='''yes''':
                a=False
        elif user1==4:
            print('''
                  half plate chicken corma 4 roti 200rs plate''')
            back=input('''
                       Any more order? (yes/no) : ''')
            if back!='''yes''':
                a=False
        elif user1==5:
            print('''
                  half plate 80rs full plate 150rs''')
            back=input('''
                       Any more order? (yes/no) : ''')
            if back!='''yes''':
                a=False
        else:
            print('''
                  invalid input''')
            back=input('''
                       Any more order? (yes/no) : ''')
            if back!='''yes''':
                a=False
    else:
        print('''
              invalid input''')
        back=input('''
                   Any more order? (yes/no) : ''')
        if back!='''yes''':
            a=False