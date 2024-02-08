file_paths = ['data/2023_07_Airspace_Germany2023.txt', 'data/SFVS-FSVV_CH-Airspace23_eDABS_APR2.txt', 'data/france.txt',
              'data/australia_class_all_23_11_30.txt', 'data/CH-ASP-National-OpenAIP.txt',
              'data/FR-ASP-National-OpenAIP.txt', 'data/DE-ASP-National-DAEC.txt', 'data/DE-ASP-National-OpenAIP.txt']

unique_AY_tags = set()
unique_non_ICAO_AY_tags = set()

for file_path in file_paths:
    cnt_without_AY = 0
    cnt_with_AY = 0
    cnt_not_ICAO = 0
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # Iterate through lines and check for 'AC ' followed by 'AY '
        for i in range(len(lines) - 1):
            if lines[i].startswith('AC '):
                if lines[i + 1].startswith('AY '):
                    sp = lines[i].strip().split(' ')
                    sp2 = lines[i + 1].strip().split(' ')
                    ##unique_AY_tags.add(sp2[1])  # Collecting unique AY tags
                    if sp[1] in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'UNCLASSIFIED']:
                        unique_AY_tags.add(sp2[1])  # Collecting unique AY tags
                    else:
                        print(i + 1, 'AC not ICAO', sp[1])
                        cnt_not_ICAO += 1
                        unique_non_ICAO_AY_tags.add(sp2[1])
                    cnt_with_AY += 1
                else:
                    cnt_without_AY += 1
    print('file ', file_path, '  total AC with following AY', cnt_with_AY, 'without AY', cnt_without_AY, 'not ICAO',
          cnt_not_ICAO)

print('Unique AY tags in files', unique_AY_tags)
print('Unique non ICAO AY tags in files', unique_non_ICAO_AY_tags)

predef_AY_tags = ['UNCLASSIFIED', 'RESTRICTED', 'DANGER', 'PROHIBITED', 'CTR', 'TMZ', 'RMZ', 'TMA', 'TRA', 'TSA', 'FIR',
                 'UIR', 'ADIZ', 'ATZ', 'MATZ', 'AWY', 'MTR', 'ALERT',
                 'WARNING', 'PROTECTED', 'HTZ', 'GLIDING_SECTOR', 'TRP', 'TIZ', 'TIA', 'MTA', 'CTA', 'ACC_SECTOR',
                 'AERIAL_SPORTING_RECREATIONAL', 'OVERFLIGHT_RESTRICTION', 'MRT', 'TFR', 'VFR_SECTOR']

not_in_predef_AY_tags = set()
for tag in unique_AY_tags:
    if tag not in predef_AY_tags:
        not_in_predef_AY_tags.add(tag)
print('AYs not in prdef_AY_tags', not_in_predef_AY_tags)
