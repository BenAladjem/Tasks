import struct

protocol = b'\x00\x85b`T\xdf\x00\x00<\x00\x04\x03123\x00\x07\x01\x01\x01\x03\x08\x9a\x99\x99\x99\x99\x99\x01@\x01\x00\x01\x01\x01\x01\x01\x02\x01\x01\x03\x02\x04test\x03456\x00\x06\x01\x01\x01\x01\x01\x04\x03\x08\x8b\xfde\xf7\xe4a\x19@\x01\x01\x08\x01\x01\t\x02\t[2, 3, 4]\x03346\x00\x07\x01\x01\t\x01\x01\x08\x01\x01\x07\x01\x01\x06\x01\x01\x07\x01\x01\x02\x01\x01\x03\x03ASD\x00\x03\x02\x03qwe\x02\x02fg\x02\x03LKJ'

def check_json_protokol(m):
    flag = True
    l = len(protocol)
    len_protocol = int.from_bytes(protocol[:2], 'big')
    if not l == len_protocol:
        flag = False
        raise Exception("Check length error")
    return flag


def bytearray_to_str(d):
    # Uncodding bytearray, returns string
    res = d.decode('utf-8')
    return res


def bytearray_to_float(n):
    # Convert bytearray to float
    return float(struct.unpack("=d", n)[0])

uncodded_protocol = {}
keys = ["strt", "stp", "dt"]
start_value = int.from_bytes(protocol[2:6], 'big')
step_value = int.from_bytes(protocol[6:9], 'big')
dt_value = protocol[9:]
test_value = 5
uncodded_protocol["strt"] = start_value
uncodded_protocol["stp"] = step_value

values = [start_value, step_value, test_value]
#print(check_json_protokol(protocol))

#print(f"start value = {start_value}")
#print(f"step value = {step_value}")
#print(dt_value)
print(uncodded_protocol)

def dt_encoding(d):
    dt = {}
    #print(d)
    num_elements = int.from_bytes(d[:2], 'big')
    d = d[2:]
    #print(d)
    # <len_protocol(2b)><num_key/v(2b)><len_key(1b)><key()><num_of_elements(2b)><type_el(1b)><len_el(1b)><value_el()>
    while d:
        list_data = []
        len_key = int.from_bytes(d[:1], 'big')
        d = d[1:]
        key = bytearray_to_str(d[:len_key]) # ключ на текущият лист
        #print(key)
        d = d[len_key:]
        num_el= int.from_bytes(d[:2], 'big')
        d = d[2:]
        for i in range(num_el):
            value = ''
            type_el = int.from_bytes(d[:1], 'big')
            d = d[1:]
            len_current_el = int.from_bytes(d[:1], 'big')
            d = d[1:]
            if type_el == 1: # int
                value = int.from_bytes(d[:len_current_el], 'big')
            elif type_el == 2: # str
                value = bytearray_to_str(d[:len_current_el])
            elif type_el == 3: # float
                pass
                value = bytearray_to_float(d[:len_current_el])
            else:
                raise Exception("Wrong data type")
            d = d[len_current_el:]
            list_data.append(value)
        dt[key] = list_data
    return dt

data_protocol = dt_encoding(dt_value)
uncodded_protocol["dt"] = data_protocol
print(uncodded_protocol)