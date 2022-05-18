import json
import struct

#dt = {'123': [1, 2.2, 0, 1, 2, 3, "test"], '456': [1, 4, 6, 8, 9, [2, 3, 4]], '346': [9, 8, 7, 6,7, 2, 3], "ASD": ["qwe", "fg", "LKJ"]}
dt = {"reportId":5201567,"deviceID":"863586031625605","timestamp":"2022-04-27T15:41:24+03:00","data":[{"higpsId":216,"value":"4","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":307,"value":"1","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":292,"value":"93","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":293,"value":"1110","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":294,"value":"74","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":295,"value":"1680","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":296,"value":"24.91","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":297,"value":"23.21","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":298,"value":"1335","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":299,"value":"3751","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":300,"value":"78","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":301,"value":"81","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":302,"value":"0","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":303,"value":"0","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":304,"value":"5","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":305,"value":"0","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":254,"value":"43.2258","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":255,"value":"27.84977","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":309,"value":"3","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":258,"value":"","timestamp":"2022-04-27T15:41:24+03:00"}]}
# dt_convert = брой двойки(4б) ключ(2б) бр.стойности_за_този_ключ(2б) дължина_на_елемент(1б)
# тип_на _ел(1б) стойност_ел(6б)
'''
Convert int to byte array
'''
def dec_hex_byte(value, num_bytes):
    res = (value).to_bytes(num_bytes, byteorder='big')
    return res

def ByteToHex(byteStr):
    # Служи за отпечатване на byte array в удобен за възприемане вид
    return " ".join(["{:02x}".format(x) for x in byteStr])

def string_to_bytearray(st):
    res = st.encode()
    return res


def float_to_bytearray(f):
    # Convert float number to bytearray
    res = struct.pack("=d", f)
    return res

def check_type_value(v):
    #Проверявя типа на данните и връща резултат, който отговаря на типа
    type_v = type(v)
    if type_v == int:
        res = 1
    elif type_v == str:
        res = 2
    elif type_v == float:
        res = 3
    else:
        res = 4
    return res

'''
Convert int to bytearray / unknown num of bytes, returns bytearray
'''
def to_bytes_without_len(d):
    count = 0
    res = (d).to_bytes(10, 'big')
    for i in range(10):
        if res[i] != 0:
            count += 1
    result = (d).to_bytes(count, 'big')
    return result

num_el = len(dt)
num_el_bytearay = dec_hex_byte(num_el,2)
keys = [k for k in dt] # ключовете на dt daнните
print(keys)


dt_bytearay = b''
dt_bytearay += num_el_bytearay
#print(dt_bytearay)

for el in keys:
    key_bytearay = string_to_bytearray(el) #ключа в битове
    #print(key_bytearay)
    dt_bytearay += dec_hex_byte(len(key_bytearay),1)
    dt_bytearay += key_bytearay
    len_value = len(dt[el])#дължина на масива стойности за настоящият ключ
    dt_bytearay += dec_hex_byte(len_value, 2)
    values = dt[el]
    print (values)

    for value in values:
        data_el_bytearay = b''
        len_el = ''
        type_value = check_type_value(value)
        if type_value == 1: # int
            data_el_bytearay = to_bytes_without_len(value)
            len_el = len(data_el_bytearay)

        elif type_value == 2: # string
            data_el_bytearay = string_to_bytearray(value)
            len_el = len(data_el_bytearay)
        elif type_value == 3: # float
            data_el_bytearay = float_to_bytearray(value)
            len_el = len(data_el_bytearay)
        else:
            type_value = 3 # всичко се преобразува на string и така се обработва
            value = str(value)
            data_el_bytearay = string_to_bytearray(value)
            len_el = len(data_el_bytearay)
        dt_bytearay += dec_hex_byte(type_value, 1)
        dt_bytearay += dec_hex_byte(len_el, 1)
        dt_bytearay += data_el_bytearay

print(dt_bytearay)
print(f'len converted bytearay= {len(dt_bytearay)}')

str_json = json.dumps(dt)
str_json_bytearay = string_to_bytearray(str_json)
print(str_json_bytearay)
print(f'len json to string bytearay= {len(str_json_bytearay)}')