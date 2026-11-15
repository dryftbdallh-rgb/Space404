#Space404

print("How are you؟")
print("The ship has been hit; let him choose from (3) options.؟\n")

print("One of the enemies has targeted your fool.؟")
print("You need to head to the engine room.؟")

choie1 = input("Choose number (1),   (2),  (3).")

if choie1 == "1":
    print("I reached the engine room, and there was fire everywhere.  ")#وصلت ف غرفه المحركات و النار ف كل مكان
    print ("(1)Use a fire extinguisher.")# استحدم طفايه حرايق
    print("(2)Disconnecting power from the motor")#فصل الطاقه عن المحرك
    choice2 = input( "(2) or (1)\n")
        
    if choice2 == "1":
        print("I succeeded in extinguishing the fire and repaired the fault.")#نجحت ف اخمات الحريق واصلحت العطل 
    elif choice2 == "2":
        print("The ship has docked safely; awaiting the next step.")#توقفت السفينه بسلام مستني الانجازه 
    else:
        print("The malfunction led to the reactor's explosion.") #تردد ادي لانفجار  المفاعل


elif choie1 == "2":
    print("Go to the transmitter; the enemy is approaching.")#ادهب لجهاز الارسال والعدو يقترب
    print("Attempting to repair the outdoor antenna (1)")#محاوله اصلاح الهواءي في الخارج(1)
    print("Hiding behind a nearby small planet (2)")#الاختباء خلف كوكيب قريب(2)
    
    choice3 = input("Choose number (1) or (2)")#اختر رقم (1) او(2)      
    if choice3 == ("1"):
        print("The enemy ship locked onto you and destroyed you instantly.")#رصيد سفينه العدو ودمرتك فورا 
    elif choice3 == ("2"):
        print("You hid cleverly, and I picked up your distress signal.")#اختبات بدكاء والتقطت النجده اشارتك
    else:
        print("Time has run out, and the enemy has caught you.")#انتهي الوقت وامسك بيك العدو 
    


elif choie1 == "3":
    print("Connections for the capsule area")#وصلات لمنطقه الكبسولات
    print("Escaping alone in the last capsule(1)")#الهروب لوحدك بالكبسوله الاخيره(1)
    print("Sacrifice and Assisting the Crew (2)")#النضحيه ومساعده الطاقم(2)
    choice4 = input ("(1) or (2)") 
    if choice4 == ("1"):
        print("I was drawn toward a black hole by mistake.")   
    elif choice4 == ("2"):
        print("You sacrificed yourself and saved everyone, like a hero.")#ضحيت بنفسك وانقذ الجميع كبطل
    else:
        print("The capsule crashed.")#تحطمت الكبسوله

else :
       print("There is an error in the data entry; please refer to the information provided in front of you.") #)خطا ف ادخال البينات يرجه التزام الي 
