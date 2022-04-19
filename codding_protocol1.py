input_message = {'IMEI': 865456053906614, 'Message ID': 1, 'data':[{'id': 216, 'value': 14241, 'type': 1}, {'id': 222, 'value': 55, 'type': 1}, {'id': 210, 'value': 40, 'type': 1}]}
#input_message = {'IMEI': 865456053906614, 'Message ID': 1, 'data': [{'id': 216, 'value': 14241, 'type': 1}]}

imei: int
start_bytes  = b'\x55\xaa'


def ByteToHex(byteStr):
    # Служи за отпечатване на byte array в удобен за възприемане вид
    return " ".join(["{:02x}".format(x) for x in byteStr])


def dec_hex_byte(value, num_bytes):
    # Convert int to byte array
    res = (value).to_bytes(num_bytes, byteorder='big')
    return res


def to_bytes_without_len(d):
    # Convert int to bytearray / unknown num of bytes, returns bytearray
    count = 0
    res = (d).to_bytes(7, 'big')
    for i in range(7):
        if res[i] != 0:
            count += 1
    result = (d).to_bytes(count, 'big')
    return result


def to_bytes_and_len(d):
    # Convert int to bytearray / returns num of bytes
    count = 0
    res = (d).to_bytes(10, 'big')
    for i in range(10):
        if res[i] != 0:
            count += 1
    result = (d).to_bytes(count, 'big')
    return count

def data_protokol(k_data, v_data, t_data ):
    #Чете всички Data и ги пакетира побитово по шаблона
    res = b''
    for i in range(len(k_data)):

        data = to_bytes_without_len(int(v_data[i]))
        data_len = dec_hex_byte(len(data), 1)
        data_type = dec_hex_byte(int(t_data), 1)
        data_type_id = dec_hex_byte(int(k_data[i]),2)
        res += (data_type_id +data_type + data_len +data)
    return res

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

def data_convert(d):
    #Чете масива DATA, като съединявя всички речници подред в byte array
    res = b''
    for i in d:
        d_type_id = dec_hex_byte(i["id"], 2)
        d_type = dec_hex_byte(i["type"], 1)
        d_value = to_bytes_without_len(i["value"])
        d_length = dec_hex_byte(to_bytes_and_len(i["value"]), 1)
        res += (d_type_id+d_type+d_length+d_value)

    return res

if not "IMEI" in input_message:
    raise Exception("There isn`t IMEI in message")
imei = input_message["IMEI"] # десетично
source_id = dec_hex_byte(imei, 7)

if not "Message ID" in input_message:
    raise Exception("There isn`t Message ID in message")
message_id = input_message["Message ID"]
message_id = dec_hex_byte(message_id, 1)

data = input_message["data"]
data_message = data_convert(data)

print(data_message)

protocol_len = dec_hex_byte((len(start_bytes) + 1 + len(source_id) + 1 + len(data_message) + 2), 1)
protocol_without_checksum = start_bytes+protocol_len+source_id+message_id+data_message
check_sum = dec_hex_byte(crc16(protocol_without_checksum), 2)
protocol = protocol_without_checksum+check_sum
print(protocol)
print(ByteToHex(protocol))