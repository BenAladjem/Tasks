import struct
import json
test_j = {
  "strt": 1650480351,
  "stp": 60,
  "dt" : {'123': [1, 2.2, 0, 1, 2, 3, "test"],
          '456': [1, 4, 6.3456, 8, 9, [2, 3, 4]],
          '346': [9, 8, 7, 6,7, 2, 3],
          "ASD": ["qwe", "fg", "LKJ"]}
}
'''
strt- start timestamp
stp - step (seconds) between data reports
dt - data array with higpsID (dataType) as key and array of measurements

'''
start_json_bytes = b''

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

def t_json_data_convert(js_data):
    # dt_convert = брой двойки(4б) ключ(2б) бр.стойности_за_този_ключ(2б) дължина_на_елемент(1б) тип_на _ел(1б) стойност_ел(6б)
    #    = num_key/v(2b)len_key(1b) key() num_of_elements(2b) type_el(1b) len_el(1b) value_el()
    num_el = len(dt)
    num_el_bytearay = dec_hex_byte(num_el, 2)
    keys = [k for k in dt]  # ключовете на dt daнните
    dt_bytearay = b''
    dt_bytearay += num_el_bytearay

    for el in keys:
        key_bytearay = string_to_bytearray(el)  # ключа в битове
        dt_bytearay += dec_hex_byte(len(key_bytearay), 1)
        dt_bytearay += key_bytearay
        len_value = len(dt[el])  # дължина на масива стойности за настоящият ключ
        dt_bytearay += dec_hex_byte(len_value, 2)
        values = dt[el]

        for value in values:
            type_value = check_type_value(value)
            if type_value == 1:  # int
                data_el_bytearay = to_bytes_without_len(value)
                len_el = len(data_el_bytearay)

            elif type_value == 2:  # string
                data_el_bytearay = string_to_bytearray(value)
                len_el = len(data_el_bytearay)
            elif type_value == 3:  # float
                data_el_bytearay = float_to_bytearray(value)
                len_el = len(data_el_bytearay)
            else:
                type_value = 2  # всичко, което не е горните три се преобразува на string и така се обработва
                value = str(value)
                data_el_bytearay = string_to_bytearray(value)
                len_el = len(data_el_bytearay)
            dt_bytearay += dec_hex_byte(type_value, 1) # add type of value
            dt_bytearay += dec_hex_byte(len_el, 1) # add len of valie
            dt_bytearay += data_el_bytearay  # add value
    return dt_bytearay


j_protocol = b''
# j_protocol = message_len(4b) start_value(4b) step_value(4b) dt_bytearay()
elements = [el for el in test_j]
number_of_elements = len(elements)

if not "strt" in test_j:
    raise Exception("There isn`t 'Start' in message")
strt = test_j["strt"] # десетично
start_value_byt = dec_hex_byte(strt, 4)
if not "stp" in test_j:
    raise Exception("Wrong step data")
step = test_j["stp"]
step_value_byt = dec_hex_byte(step, 3)
if not "dt" in test_j:
    raise Exception("There isn`t data in message")
dt = test_j["dt"]

dt_bytearay = t_json_data_convert(dt)
protocol_without_len = start_value_byt + step_value_byt + dt_bytearay
len_protocol_by = dec_hex_byte(len(protocol_without_len), 2)
j_protocol += len_protocol_by + protocol_without_len
print(j_protocol)
print(ByteToHex(j_protocol))
print(f'len converted json= {len(j_protocol)} bytes')
# За сравнение:
str_json = json.dumps(test_j)
not_converted_json = string_to_bytearray(str_json)
print(not_converted_json)
print(ByteToHex(not_converted_json))
print(f'len not converted json = {len(not_converted_json)} bytes')
