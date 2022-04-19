#message = input()
#{'IMEI': 865456053906614, 'messageID': 1, 'data': [{'id': 215, 'value': 1234, 'type': 1}, {'id': 215, 'value': 1234, 'type': 1}]}
#{'IMEI': 865456053906614, 'Message ID': 1, 'data': [{'id': 216, 'value': 14241, 'type': 1}, {'id': 222, 'value': 55, 'type': 1}, {'id': 210, 'value': 40, 'type': 1}]}


test_message = b'U\xaa\x1d\x03\x13 \xb0\xa9l\xb6\x01\x00\xd8\x01\x027\xa1\x00\xde\x01\x017\x00\xd2\x01\x01(\x9dn'
#test_message = b'U\xaa\x13\x03\x13 \xb0\xa9l\xb6\x01\x00\xd8\x01\x027\xa1G\xe2'
#               m = 'IMEI=865456053906614&data=216,14241;222,55;210,40'
message = b''

start_bytes  = b'\x55\xaa'

if start_bytes in test_message:
    start_message = test_message.index(start_bytes)
    len_message = test_message[start_message + 2]
    message = test_message[start_message:start_message + len_message]
    #print(message)


def check_protokol(m):
    flag = True
    l = len(message)
    message_len = message[2]
    if not l == message_len:
        flag = False
        raise Exception("Check length error")

    message_without_check_sum = message[:l - 2]
    check_sum = message[l - 2:]
    check_crc16 = crc16(message_without_check_sum)
    if not check_sum == (check_crc16).to_bytes(2, 'big'):
        flag = False
        raise Exception("Check sum error")
    return flag


def ByteToHex(byteStr):
    return " ".join(["{:02x}".format(x) for x in byteStr])

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

def make_data_dict(d_message):
    pass

l = len(message)
message_len = message[2]
message_without_check_sum = message[:l - 2]
check_sum = message[l - 2:]
check_crc16 = crc16(message_without_check_sum)

print(check_protokol(message))

imei = int.from_bytes(message[3:10], 'big')
message_id = message[10]

data_message = message[11:-2]
data = []
while data_message:
    id = int.from_bytes(data_message[:2], 'big')
    #print(f"id={id}")
    type = data_message[2]
    #print(f"data type={type}")
    value_len = data_message[3]
    #print(f"value len = {value_len}")
    data1 = int.from_bytes(data_message[4:4 + value_len], 'big')
    data.append({"id":id, "value": data1, "type": type})
    for i in range(4 + value_len):
        data_message = data_message[1:]


result = {}


result['IMEI'] = imei
result['Message ID'] = message_id
result['data'] = data


print(result)