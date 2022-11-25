time_list = []
time_total = [0, 0, 0, 0]

while True:
    
    def PlusMinusZeroCheck(character):
        if character == '+':
            return True
        elif character == '-':
            return False
        elif character == '0':
            return "Endroll"
        elif character == 'c':
            return "CalculationStart"
        else:
            print("ERRR: Invalid first value input.")
            return "ERRR 0001"

    def InputThreeZeroCheck(element):
        element_checkcount = 1
        while True:
            if input_list[element_checkcount] == 0:
                if element_checkcount == 3:
                    print("WARN: Your input element has no actual calculation.")
                    return False
                else:
                    print("CHEK: Keep checking your element...")
                    element_checkcount += 1
            else:
                time_list.append(element)
                print("SUCS: Your element has been saved.")
                return True

    while True: #Value Input & Checking
        print("Please write [(+/-)] [Hour] [Minute] [Second]. Input '0' in first value to start calculation.")
        input_list = input().split(" ")
        threecheck_result = PlusMinusZeroCheck(input_list[0])
        if threecheck_result == "Endroll":
            quit()
        elif threecheck_result == "ERRR 0001":
            continue
        elif threecheck_result == True:
            input_list[0] = True
        elif threecheck_result == False:
            input_list[0] = False
        elif threecheck_result == "CalculationStart":
            break
        else:
            print("ERRR: Invalid first value input checked.")
            continue

        for count in range(1, 4):
            if input_list[count].isdigit() == True:
                input_list[count] = int(input_list[count])
            else:
                print(f"ERRR: Invalid value {input_list[count]}. You must input integer there.")
        
        zerocheck_result = InputThreeZeroCheck(input_list)
        if zerocheck_result == False:
            continue
        else:
            print ("SUCS: Three values are confirmed. Keep going...")
            break
        
    current_element = time_list[-1]
    def PlusMinusTime(element1, element2, isAdd):
        def OverMax():
            if isAdd == True:
                for overplus_count in range (1, 4):
                    if element1[overplus_count] >= 60:
                        element1[overplus_count] -= 60
                        element1[overplus_count - 1] += 1
            else:
                for overplus_count in range (1, 4):
                    if element1[overplus_count] < 0:
                        element1[overplus_count - 1] -= 1
                        element1[overplus_count] += 60
            return element1

        if isAdd == True:
            for count in range(1, 4):
                element1[count] += element2[count]
            element1 = OverMax()
        else:
            for count in range(1, 4):
                element1[count] -= element2[count]
            element1 = OverMax()

    if current_element[0] == True:
        PlusMinusTime(time_total, current_element, True)
    else:
        PlusMinusTime(time_total, current_element, False)
    for i in range(1, 4):
        if time_total[i] < 0:
            print ("CHEK: total time is lower then 0. So we confirmed total time to 0h 0m 0s.")
            for j in range(1, 4):
                time_total[j] = 0
    print (f"Final calculated time amount is {time_total[1]}h {time_total[2]}m {time_total[3]}s.")
