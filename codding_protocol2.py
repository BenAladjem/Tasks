import struct

#input_message = {'IMEI': 865456053906614, 'Message ID': 1, 'data':[ {'id': 210, 'value': 4.5061, 'type': 3}]}
input_message = {'IMEI': 865456053906614, 'Message ID': 1, 'data':[{'id': 216, 'value': 14241, 'type': 1}, {'id': 222, 'value': '**$$**', 'type': 2}, {'id': 210, 'value': 4.5061, 'type': 3}]}
#input_message = {'IMEI': 865456053906614, 'Message ID': 1, 'data': [{'id': 216, 'value': 14241, 'type': 1}]}


imei: int
start_bytes  = b'\x55\xaa'


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

def bytearray_to_float(n):
    # Convert bytearray to float
    return float(struct.unpack("=d", n)[0])


'''
Convert int to byte array
'''
def dec_hex_byte(value, num_bytes):
    res = (value).to_bytes(num_bytes, byteorder='big')
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


'''
Convert int to bytearray / returns num of bytes
'''
def to_bytes_and_len(d):
    count = 0
    res = (d).to_bytes(10, 'big')
    for i in range(10):
        if res[i] != 0:
            count += 1
    result = (d).to_bytes(count, 'big')
    return count

def crc16(data: bytes, poly=0x8408):
    '''
    CRC-16-CCITT Algorithm
    '''
    data = bytearray(data)
    crc = 0xFFFF
    for b in data:
        cur_byte = 0xFF & b
        for _ in range(0, 8):
            if (crc & 0x0001) ^ (cur_byte & 0x0001):
                crc = (crc >> 1) ^ poly
            else:
                crc >>= 1
            cur_byte >>= 1
    crc = (~crc & 0xFFFF)
    crc = (crc << 8) | ((crc >> 8) & 0xFF)

    return crc & 0xFFFF

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


def data_convert(d):
    #Чете масива DATA, като съединявя всички речници подред в byte array
    res = b''
    for i in data:
        v = i['value']
        #res = b''
        print(check_type_value(v))
        if check_type_value(v) == 1:
            d_type_id = dec_hex_byte(i["id"], 2)
            d_type = dec_hex_byte(i["type"], 1)
            d_value = to_bytes_without_len(i["value"])
            d_length = dec_hex_byte(to_bytes_and_len(i["value"]), 1)
            res += (d_type_id + d_type + d_length + d_value)
        elif check_type_value(v) == 2:
            d_type_id = dec_hex_byte(i["id"], 2)
            d_type = dec_hex_byte(2, 1)
            d_value = string_to_bytearray(i["value"])
            d_length = dec_hex_byte(len(d_value), 1)
            res += (d_type_id + d_type + d_length + d_value)
        elif check_type_value(v) == 3:
            d_type_id = dec_hex_byte(i["id"], 2)
            d_type = dec_hex_byte(i["type"], 1)
            d_value = float_to_bytearray(i["value"])
            d_length = dec_hex_byte(len(d_value), 1)
            res += (d_type_id + d_type + d_length + d_value)
        else:
            pass
        #res += (d_type_id + d_type + d_length + d_value)
        #print(res)

    return res



if not "IMEI" in input_message:
    raise Exception("There isn`t IMEI in message")
imei = input_message["IMEI"] # десетично
if not len(str(imei)) == 15:
    raise Exception("Wrong IMEI value")
source_id = dec_hex_byte(imei, 7)

if not "Message ID" in input_message:
    raise Exception("There isn`t Message ID in message")

message_id = input_message["Message ID"]
if not type(message_id) ==int:
    raise Exception("Wrong message ID")
else:
    message_id = dec_hex_byte(message_id, 1)

olny_for_data_type_check = []
data = input_message["data"]
if not type(data) == type(olny_for_data_type_check):
    raise Exception("Invalid data")
data_message = data_convert(data)

print(f"only data message = {data_message}")

protocol_len = dec_hex_byte((len(start_bytes) + 1 + len(source_id) + 1 + len(data_message) + 2), 1)
protocol_without_checksum = start_bytes+protocol_len+source_id+message_id+data_message
check_sum = dec_hex_byte(crc16(protocol_without_checksum), 2)
protocol = protocol_without_checksum+check_sum
print(protocol)
print(ByteToHex(protocol))