import read_write
import managment

def Main_Change():
    while True:
        managment.Change_Menu()
        operation =int(input())
        if operation == 0:
            break
        elif operation == 1:
            Add_Information()
        elif operation == 2:
            Delete_Employeer_ID()
        elif operation == 3:
            print ('В разработке')   
        else:
            print ('Некорректный ввод: ')
def Add_Another(list,ID,text):
    while True:
        op = input(f'Введите 1, если нужно добавить {text} или Enter, если не требуется - ')
        if op == str(1):
            list.append({"ID_employeer":ID}) 
            for key in list[0].keys():
                if key != "ID_employeer": 
                    list[len(list)-1][key] = input(f'Введите значение {key} - ')
        else:
            break    

def Delete_ID(list,ID):
    item = []
    for i in range(len(list)):
        for key , value in list[i].items():
            if key == "ID_employeer" and str(value) == str(ID): 
                item.append(i)
    item.sort(reverse = True)            
    for j in item:
        list.pop(j)

def Add_Information():
    employeer = read_write.Read_json('employeer.json')
    adresses = read_write.Read_json('adresses.json')    
    email = read_write.Read_json('email.json')
    phones = read_write.Read_json('phones.json')
    adresses_count = len(adresses)
    email_count = len(email)
    phones_count = len(phones)
    id_empl = len(employeer)+1
    employeer.append({"ID_employeer":id_empl}) 
    for key in employeer[0].keys():
        if key != "ID_employeer": 
            employeer[len(employeer)-1][key] = input(f'Введите значение {key} - ')
    Add_Another(phones,id_empl,'телефон')
    Add_Another(email,id_empl,'e-mail')
    Add_Another(adresses,id_empl,'адрес')
    print('Добавлен новый сотрудник')
    while True:
        managment.Add_Confirm_Menu()
        operation = input()
        if operation == str(1):
            Add_Information()
        elif operation == str(2):
            read_write.Write_json(employeer,'employeer.json')
            if adresses_count < len(adresses):
                read_write.Write_json(adresses,'adresses.json')
            if email_count < len(email):
                read_write.Write_json(email,'email.json')
            if phones_count < len(phones):
                read_write.Write_json(phones,'phones.json')
            break
        elif operation != str(1) or operation != str(2):
            break

def Delete_Employeer_ID():
    employeer = read_write.Read_json('employeer.json')
    adresses = read_write.Read_json('adresses.json')    
    email = read_write.Read_json('email.json')
    phones = read_write.Read_json('phones.json')
    ID = input('Введите ID сотрудника, информацию о котором нужно удалить - ')
    Delete_ID(employeer,ID)
    Delete_ID(adresses,ID)
    Delete_ID(email,ID)
    Delete_ID(phones,ID)
    print(f'Удалена информация о сотруднике с ID = {ID}')
    while True:
        managment.Delete_Confirm_Menu()
        operation = input()
        if operation == str(1):
            Add_Information()
        elif operation == str(2):
            read_write.Write_json(employeer,'employeer.json')
            read_write.Write_json(adresses,'adresses.json')
            read_write.Write_json(email,'email.json')
            read_write.Write_json(phones,'phones.json')
            break
        elif operation != str(1) or operation != str(2):
            break
