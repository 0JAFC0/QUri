def leds(lds):
    #        0,1,2,3,4,5,6,7,8,9
    leds = [6,2,5,5,4,5,6,3,7,6]
    s = 0
    for p in lds:
        s += leds[int(p)]
    
    print(s, "leds")

for a in range(int(input())):
    leds(input())
