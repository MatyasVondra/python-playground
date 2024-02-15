import csv
import json
import random

# current,deskId=desk1,zoneId=zone1 rms_avg=225 1706016645
line_protocol_temp = {
    'source': 'current',
    'deskId': '',
    'zoneId': '',
    'rms_avg': '',
    'timestamp': ''
}

virtual_desk_zone_map = {
    "owa6x7qv09jxueo7kbb0x": "zone1",
    "8c88lemyp3amlsub35xvi": "zone1",
    "lm1ftor26qh07kkve7wpp": "zone1",
    "tqzdm2ys0jr15kiy16hzs": "zone1",
    "2iozaghatirc19d90trhv": "zone1",
    "z66opagbq9kxgszlqyuj5": "zone1",
    "u03uwu6tjlxulr931abzp": "zone1",
    "ro8ck05vosu6vb68n0yvr": "zone1",
    "zcrr8wxj5caitk3yt8irc": "zone2",
}

measurement_min = 200
measurement_max = 850

with open('miot-input.csv', mode='r') as input_file:
    csvFile = csv.reader(input_file)
    next(csvFile, None)
    for line in csvFile:
        # line[2] = deviceId
        # line[7] = json
        json_data = json.loads(line[7])
        for measurement in json_data['analog_channels'][0]['measurements']:
            line_prot_dict = {
                'source': 'current',
                'deskId': line[2],
                'zoneId': 'zone1',
                'rms_avg': measurement['rms_avg'],
                'timestamp': measurement['timestamp']
            }
            line_prot_row = f'{line_prot_dict["source"]},deskId={line_prot_dict["deskId"]},zoneId={line_prot_dict["zoneId"]} rms_avg={line_prot_dict["rms_avg"]}i {line_prot_dict["timestamp"]}\n'
            with open('miot-output.txt', mode='a') as output_file:
                output_file.write(line_prot_row)

            for virtual_desk in virtual_desk_zone_map.items():
                line_prot_dict_virt = {
                    'source': 'current',
                    'deskId': virtual_desk[0],
                    'zoneId': virtual_desk[1],
                    'rms_avg': random.randint(measurement_min, measurement_max),
                    'timestamp': measurement['timestamp']
                }
                line_prot_row_virt = f'{line_prot_dict_virt["source"]},deskId={line_prot_dict_virt["deskId"]},zoneId={line_prot_dict_virt["zoneId"]} rms_avg={line_prot_dict_virt["rms_avg"]}i {line_prot_dict_virt["timestamp"]}\n'
                with open('miot-output.txt', mode='a') as output_file:
                    output_file.write(line_prot_row_virt)
