while True:
    inpData=input('Введите число для возведении в квадрат:\n')
    if inpData=='stop':
        break
    
    #if inpData.isdigit():
    #    inpData=int(inpData)
    #else:
    #    print('Вы ввели неправильное значение...\n')
    #    continue

    try:
        inpData=int(inpData)
    except:
        print('Вы ввели неправильные данные...\n')
        continue
    
    print('Вы ввели: ',inpData,'\nРезультат вычислений: ',inpData**2,'\nНапишите "stop" для выхода...\n')

