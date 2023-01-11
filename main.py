import os
import random
import time


lang = ''
EngGame = 0
RusGame = 0
chouCoin = 0
Coin = 0
money = 100
stavka = 0
prokrut = '1'
first = 0
second = 0
therd = 0
prokrutX = '1'
randomX = 0
pobedaX = '2'
povtor = False
prodoljit = 0
povtorRUS = True
povtorENG = True
povtor1 = False





lang = (input('choose languge (print Eng or Rus):'))
try:
  if lang == 'Eng' or lang == 'eng':
   while povtorENG == True:
     print('You balance = ', money)
     EngGame = int(input('choose the game (1 - coin; 2 - X2, 3 - one-armed bandit ) '))
     stavka = int(input('confirm the bid:'))
     if stavka > money:
       print('not enough money')
     else:
    
       if EngGame == 1:
         print('loss of an eagle or tails - X2; rib prolapse - Х20')
         time.sleep(1)
         chouCoin =  int(input('choose the side of the coin (1 - heads - 49%; 2 - tails - 49%; 3 - edge - 2%):'))
         Coin = random.randint(1,100)
         if Coin <= 49:
           print('tails')
           if chouCoin == 2:
             print('win')
             money = money + stavka
             print('your balance is', money, "coins")
             
           else:
             print("loose")
             money = money - stavka
             print('your balance is', money, "coins")
         if Coin > 49 and Coin <=98:
            print('eagle')
            if chouCoin == 1:
             print('win')
             money = money + stavka
             print('your balance is', money, "coins")
            else:
             print("loose")
             money = money - stavka
             print('your balance is', money, "coins")        
         if Coin > 98:
           print("edge")
           if chouCoin == 3:
             print('JACKPOT')
             money = money + stavka*20
             print('your balance is', money, "coins")
           else:
             print("loose")
             money = money - stavka
             print('your balance is', money, "coins") 
         povtor1 = True
         while povtor1 == True:
          if money > 0: 
            print('')
            prodoljit = int(input('want to continue? (1 - yes, 2 - no):'))
            if  prodoljit == 1:
             print()
             povtor1 = False
             
            elif  prodoljit == 2:
             print('the program has been stopped')
             povtor1 = False
             povtorENG = False
            else:
             print('enter only 1 or 2')
          else:
            povtorENG = False
            povtor1 = False
            print('Your balance is zero')
         
         
       elif EngGame == 3:
         prokrut = (input('press "Enter" to scroll'))
         if prokrut == '':
           os.system('cls||clear')
           first = random.randint(1,7)
           print(first)
           time.sleep(1)
           os.system('cls||clear')
           first = random.randint(1,7)
           print(first)
           time.sleep(1)
           os.system('cls||clear')
           first = random.randint(1,7)
           print(first)
           time.sleep(1)
           os.system('cls||clear')
           second = random.randint(1,7)
           print(first, second)
           time.sleep(1)
           os.system('cls||clear')
           second = random.randint(1,7)
           print(first, second)
           time.sleep(1)
           os.system('cls||clear')
           second = random.randint(1,7)
           print(first, second)
           time.sleep(1)
           os.system('cls||clear')
           therd = random.randint(1,7)
           print(first, second, therd)
           time.sleep(1)
           os.system('cls||clear')
           therd = random.randint(1,7)
           print(first, second, therd)
           time.sleep(1)
           os.system('cls||clear')
           therd = random.randint(1,7)
           print(first, second, therd)
           time.sleep(1)
      
           if first == second and second == therd and first>5:
             print('you won!!! (X2)')
             money = money + stavka
             time.sleep(1)
             print('your balance is', money)
           elif first == second and second == therd and first == 5:
             print('ANGEL COMBO!!! (X3)')
             money = money + stavka*2
             time.sleep(1)
             print('your balance is', money)
           
           elif first == second and second == therd and first == 6:
             print('HELL COMBO!!! (X3)')
             money = money + stavka*2
             time.sleep(1)
             print('your balance is', money)
           elif first == second and second == therd and first == 7:
             print('JACKPOT!!! (x4)')
             money = money + stavka*3
             time.sleep(1)
             print('your balance is', money)
           else:
             print('you lose!!!')
             money = money - stavka
             print('your balance is', money)
         povtor1 = True
         while povtor1 == True:
          if money > 0: 
            print('')
            prodoljit = int(input('want to continue? (1 - yes, 2 - no):'))
            if  prodoljit == 1:
             print()
             povtor1 = False
             
            elif  prodoljit == 2:
             print('the program has been stopped')
             povtor1 = False
             povtorENG = False
            else:
             print('enter only 1 or 2')
          else:
            povtorENG = False
            povtor1 = False
            print('Your balance is zero')
           
           
      
           
       elif EngGame == 2:
         print('with each successful spin, your X will double (X1.2, X2.4, X4.8, X9.6, X20), but the chances of winning will also fall (85%, 40%, 20%, 10% 3%)')
         print('')
         prokrutX = (input('press "enter" to scroll'))
         if prokrutX == '':
           randomX = random.randint(1,100)
           if randomX <= 85:
             pobedaX = (input('you win, press "Enter" to continue or "1" to finish'))
             if pobedaX == '':
               randomX = random.randint(1,100)
               if randomX <= 40:
                 pobedaX = (input('you win, press "Enter" to continue or "1" to finish'))
                 if pobedaX == '':
                   randomX = random.randint(1,100)
                   if randomX <= 20:
                    pobedaX = (input('you win, press "Enter" to continue or "1" to finish'))
                    if pobedaX == '':
                      randomX = random.randint(1,100)
                      if randomX <= 10:
                        pobedaX = (input('you win, press "Enter" to continue or "1" to finish'))
                        if pobedaX == '':
                         randomX = random.randint(1,100)
                         if randomX <= 3:
                           money = money + stavka*19
                           pobedaX = print('JACKPOT! your balance is', money)
                           
                         else:
                           print('you lose')
                           money = money - stavka
                           print('your balance is', money)
                           
                        elif pobedaX == '1':
                          money = money + stavka*8.6
                          print('Your balance is', money)
      
                        else:
                          print('error')
                        
      
                      else:
                        print('you lose')
                        money = money - stavka
                        print('your balance is', money)
                    elif pobedaX == '1':
                      money = money + stavka*3.8
                      print('your balance is', money)
                    else:
                      print('error')
                   else:
                     print('you lose')
                     money = money - stavka
                     print('your balance is', money)
                 elif pobedaX == '1':
                   money = money + stavka*1.4
                   print('your balance is', money)
                 else:
                   print('error')
               else:
                 print('you lose')
                 money = money - stavka
                 print('your balance is', money)
                 
      
             elif pobedaX == '1':
               money = money + stavka*0.2
               print('your balance is', money)
             else:
               print('error')
           else:
             print("you lose")
             money = money - stavka
             print('your balance is', money)
         povtor1 = True
         while povtor1 == True:
          if money > 0: 
            print('')
            prodoljit = int(input('want to continue? (1 - yes, 2 - no):'))
            if  prodoljit == 1:
             print()
             povtor1 = False
             
            elif  prodoljit == 2:
             print('the program has been stopped')
             povtor1 = False
             povtorENG = False
            else:
             print('enter only 1 or 2')
          else:
            povtorENG = False
            povtor1 = False
            print('Your balance is zero')
    
  
         
#------------------------------------------------------------


  
  elif lang == 'Rus' or lang == 'rus':
   
   while povtorRUS == True:
     
     print('ваш баланс = ', money)
     RusGame = int(input('выберите игру (1 - монетка; 2 - иксы; 3 - однорукий бандит):'))
     stavka = int(input('утвердите ставку:'))
     if stavka > money:
       print('не достаточно денег')
  
     else:
    
       if RusGame == 1:
         print('выпадение орла или решки - Х2; выпадение ребра - Х20')
         time.sleep(1)
         chouCoin =  int(input('выберите сторону монеты (1 - орел - 49%; 2 - решка - 49%; 3 - ребро - 2%):'))
      
                 
          
         
         Coin = random.randint(1,100)
         if Coin <= 49:
           print('решка')
           if chouCoin == 2:
             print('победа')
             money = money + stavka
             print('ваш баланс равен', money, "монет")
             
             
           else:
             print("пройгрыш")
             money = money - stavka
             print('ваш баланс равен', money, "монет")
         if Coin > 49 and Coin <=98:
            print('орёл')
            if chouCoin == 1:
             print('победа')
             money = money + stavka
             print('ваш баланс равен', money, "монет")
            else:
             print("пройгрыш")
             money = money - stavka
             print('ваш баланс равен', money, "монет")        
         if Coin > 98:
           print("ребро")
           if chouCoin == 3:
             print('ДЖЕКПОТ')
             money = money + stavka*20
             print('ваш баланс равен', money, "монет")
           else:
             print("пройгрыш")
             money = money - stavka
             print('ваш баланс равен', money, "монет") 
         povtor = True
         while povtor == True:
          if money > 0:
            print('')
            prodoljit = int(input('хотите продолжить? (1 - да, 2- нет)'))
            if  prodoljit == 1:
             print()
             povtor = False
             
            elif  prodoljit == 2:
             print('программа была остановлена')
             povtor = False
             povtorRUS = False
            else:
             print('ввеедите только 1 или 2')
          else:
            povtorRUS = False
            povtor = False
            print('Ваш баланс равен нулю')
            
         
         
       elif RusGame == 3:
         prokrut = (input('нажмите "Enter" для прокрута'))
         if prokrut == '':
           os.system('cls||clear')
           first = random.randint(1,7)
           print(first)
           time.sleep(1)
           os.system('cls||clear')
           first = random.randint(1,7)
           print(first)
           time.sleep(1)
           os.system('cls||clear')
           first = random.randint(1,7)
           print(first)
           time.sleep(1)
           os.system('cls||clear')
           second = random.randint(1,7)
           print(first, second)
           time.sleep(1)
           os.system('cls||clear')
           second = random.randint(1,7)
           print(first, second)
           time.sleep(1)
           os.system('cls||clear')
           second = random.randint(1,7)
           print(first, second)
           time.sleep(1)
           os.system('cls||clear')
           therd = random.randint(1,7)
           print(first, second, therd)
           time.sleep(1)
           os.system('cls||clear')
           therd = random.randint(1,7)
           print(first, second, therd)
           time.sleep(1)
           os.system('cls||clear')
           therd = random.randint(1,7)
           print(first, second, therd)
           time.sleep(1)
      
           if first == second and second == therd and first>5:
             print('вы выйграли!!! (Х2)')
             money = money + stavka
             time.sleep(1)
             print('ваш баланс равен', money)
           elif first == second and second == therd and first == 5:
             print('АНГЕЛЬСКОЕ КОМБО!!! (Х3)')
             money = money + stavka*2
             time.sleep(1)
             print('ваш баланс равен', money)
           
           elif first == second and second == therd and first == 6:
             print('АДСКОЕ КОМБО!!! (Х3)')
             money = money + stavka*2
             time.sleep(1)
             print('ваш баланс равен', money)
           elif first == second and second == therd and first == 7:
             print('ДЖЕКПОТ!!! (Х4)')
             money = money + stavka*3
             time.sleep(1)
             print('ваш баланс равен', money)
           else:
             print('вы проиграли!!!')
             money = money - stavka
             print('ваш баланс равен', money)
         povtor = True
         while povtor == True:
          if money > 0: 
            print('')
            prodoljit = int(input('хотите продолжить? (1 - да, 2- нет):'))
            if  prodoljit == 1:
             print()
             povtor = False
             
            elif  prodoljit == 2:
             print('программа была остановлена')
             povtor = False
             povtorRUS = False
            else:
             print('ввеедите только 1 или 2')
          else:
            povtorRUS = False
            povtor = False
            print('Ваш баланс равен нулю')
           
           
      
           
       elif RusGame == 2:
         print('с каждым удачным прокрутом ваши иксы будут удваиваться (X1.2, X2.4, X4.8, X9.6, X20), но и шансы на победу будут падать (85%, 40%, 20%, 10% 3%) ')
         print('')
         prokrutX = (input('нажмите "enter" для прокрута'))
         if prokrutX == '':
           randomX = random.randint(1,100)
           if randomX <= 85:
             pobedaX = (input('вы выйграли, нажмите "Enter" что бы продолжить или "1" для завершения'))
             if pobedaX == '':
               randomX = random.randint(1,100)
               if randomX <= 40:
                 pobedaX = (input('вы выйграли, нажмите "Enter" что бы продолжить или "1" для завершения'))
                 if pobedaX == '':
                   randomX = random.randint(1,100)
                   if randomX <= 20:
                    pobedaX = (input('вы выйграли, нажмите "Enter" что бы продолжить или "1" для завершения'))
                    if pobedaX == '':
                      randomX = random.randint(1,100)
                      if randomX <= 10:
                        pobedaX = (input('вы выйграли, нажмите "Enter" что бы продолжить или "1" для завершения'))
                        if pobedaX == '':
                         randomX = random.randint(1,100)
                         if randomX <= 3:
                           money = money + stavka*19
                           pobedaX = print('ДЖЕКПОТ! ваш баланс равен', money)
                           
                         else:
                           money = money - stavka
                           print('вы проиграли')
                           print('ваш баланс равен', money)
                           
                        elif pobedaX == '1':
                          money = money + stavka*8.6
                          print('Ваш баланс равен', money)
      
                        else:
                          print('ошибка')
                        
      
                      else:
                        print('вы проиграли')
                        money = money - stavka
                        print('ваш баланс равен', money)
                    elif pobedaX == '1':
                      money = money + stavka*3.8
                      print('ваш баланс равен', money)
                    else:
                      print('ошибка')
                   else:
                     print('вы проиграли')
                     money = money - stavka
                     print('ваш баланс равен', money)
                 elif pobedaX == '1':
                   money = money + stavka*1.4
                   print("ваш баланс равен", money)
                 else:
                   print('ошибка')
               else:
                 print('вы проиграли')
                 money = money - stavka
                 print('ваш баланс равен', money)
                 
      
             elif pobedaX == '1':
               money = money + stavka*0.2
               print("ваш баланс равен", money)
             else:
               print('ошибка')
           else:
             print("вы проиграли")
             money = money - stavka
             print('ваш баланс равен', money)
         povtor = True
         while povtor == True:
          if money > 0:
            print('')
            prodoljit = int(input('хотите продолжить? (1 - да, 2- нет):'))
            if  prodoljit == 1:
             print()
             povtor = False
             
            elif  prodoljit == 2:
             print('программа была остановлена')
             povtor = False
             povtorRUS = False
            else:
             print('ввеедите только 1 или 2')
          else:
            povtorRUS = False
            povtor = False
            print('Ваш баланс равен нулю')
           
      
       
      
       else:
             if lang == 'Eng' or lang == 'eng' or lang == 'Rus' or lang == 'rus':
              print('введите номер игры указаный выше')
              print('')
              print('enter the game number above')
             else:
               print('choose just Eng orRus Rus')


except ValueError:
    if lang == 'Rus' or lang == 'rus':
      print('вводите только то, что указано выше')
    elif lang == 'Eng' or lang == 'eng':
      print('enter only what is indicated above')
