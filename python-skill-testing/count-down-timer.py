# Vi benytter hvad vi har lært i de forrige moduler til at lave en count-down timer
import time as t
# variabler
timer_tid = int(input("Fra hvilket tal skal det tælles ned fra?: "))
nedtælling_tid = float(
    input("Hvor lang tid skal der være imellem hver nedtælling?: "))
Begynd_nedtælling = input("Vil du begynde nedtælling? (ja/nej): ")

if Begynd_nedtælling.lower() == "ja":
    while True:
        timer_tid -= 1
        print(f"{timer_tid}")
        t.sleep(nedtælling_tid)
        if timer_tid == 0:
            break
        else:
            continue

    print("DUT-DUT - nedtælling er færdig!")

else:
    print("Okay - nedtælling påbegyndes ikke!")
