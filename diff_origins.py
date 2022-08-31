import json
import csv

# Opening JSON file
netmri_file = open('netmri_devices.json')
# returns JSON devices as list
netmri_devices = json.load(netmri_file)['devices']

ca_file = open('ca_devices.json')
ca_devices = json.load(ca_file)['ca_devices']



def compare_and_change():
    filtrered_devices = []
    for device in netmri_devices:
        if 'Router' in device['DeviceType'] or 'Switch' in device['DeviceType'] or 'Switch-Router' in device['DeviceType']:
            filtrered_devices.append(device)
    ###################################################
    # Check the CA Spectrum in the NetMRI data
    ###################################################
    ca_report_rows = []
    for clean_device in ca_devices:
        #Get the attributes from CA Spectrum
        clean_id = clean_device['@mh']
        clean_attributes = clean_device['attribute']
        clean_name = clean_attributes[0]['$']
        clean_model = clean_attributes[1]['$']
        is_inNetMRI = False
        for device in filtrered_devices:
            if clean_name == device['DeviceName']:
                #The logic for exist
                is_inNetMRI = True
        #Create the row information to create the CSV report
        ca_row = {
            'id': clean_id,
            'hostname': clean_name,
            'model': clean_model,
            'exist in Netmri': is_inNetMRI
        }
        ca_report_rows.append(ca_row)
    #Create the headers to CSV report
    fieldnames=['id', 'hostname', 'model', 'exist in Netmri']
    create_report(fieldnames, ca_report_rows, 'ca_spectrum_report.csv')
    ###################################################
    # Check the NetMRI devices in the CA Spectrum data
    ###################################################
    netmri_report_rows = []
    for device in filtrered_devices:
        #Get the attributes from NetMRI devices
        device_id = device['DeviceID']
        device_name = device['DeviceName']
        device_model = device['DeviceModel']
        is_inCaSpectrum = False
        for clean_device in ca_devices:
            clean_attributes = clean_device['attribute']
            clean_name = clean_attributes[0]['$']
            if device['DeviceName'] == clean_name  :
                #The logic for exist
                is_inCaSpectrum = True
        #Create the row information to create the CSV report
        netmri_row = {
            'id': device_id,
            'hostname': device_name,
            'model': device_model,
            'exist in CA Spectrum': is_inCaSpectrum
        }
        netmri_report_rows.append(netmri_row)
    #Create the headers to CSV report
    fieldnames=['id', 'hostname', 'model', 'exist in CA Spectrum']
    create_report(fieldnames, netmri_report_rows, 'netmri_report.csv')
    unified_hostnames = []
    unified_values = []
    for ca_row in ca_report_rows:
        unified_hostnames.append(ca_row['hostname'])
        diff_value = {
            'hostname': ca_row['hostname'],
            'exist_in_ca_spectrum': True,
            'exist_in_netmri': False
        }
        unified_values.append(diff_value)
    for netmri_row in netmri_report_rows:
        if netmri_row['hostname'] not in unified_hostnames:
            unified_hostnames.append(netmri_row['hostname'])
            diff_value = {
            'hostname': ca_row['hostname'],
            'exist_in_ca_spectrum': False,
            'exist_in_netmri': True
            }
    for value in unified_values:
        for netmti_row in netmri_report_rows:
            if netmti_row['hostname'] == value['hostname']:
                value['exist_in_netmri'] = True
    final_json = {'data': unified_values}
    create_json_file(final_json, 'unified_diffs.json')

def create_report(fieldnames, rows, filename):
    with open(filename, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def create_json_file(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
        print("New json file is created from changed_devices.json file")

compare_and_change()