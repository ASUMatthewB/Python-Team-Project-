"""Team project to process court calendars!"""


END_HEADER = "*" *15


def is_summary_header(line):
    return line[0] == "1" and "RUN DATE:" in line


def is_page_header(line):
    return line[0] == "1" and "RUN DATE:" not in line

def process_page_header(line, infile):
     while True:
        line = infile.readline()
        if line == "" or END_HEADER in line:
            break


def is_report_header(line):
    return line[0] != "1" and "RUN DATE:" in line

def process_report_header(line, infile):
    data = {}
    data['RunDate'] = line[12:20]
    while True:
        line = infile.readline()
        if line == "" or END_HEADER in line:
            break
        elif "COURT DATE:" in line:
            data['CourtDate'] = line[22:30]
            data['CourtTime'] = line[44:52]
            data['CourtRoom'] = line[78:].strip()
    return data


def is_fingerprinted(line):
    return "FINGERPRINTED" in line

def process_fingerprinted(line, infile):
    data = {}
    while True:
        return True


def is_offense(line):
    return line[8:9] == "("

def process_offense(line, infile):
    data = {}
    while True:
        if line == "":
            break
        else:
            data['charge'] = line[8:37].strip()
            data['plea'] = line[49:65].strip()
            data['ver'] = line[69:83].strip()
        return data


def is_defendent(line):
    return line[8:12] == "23CR"

def is_aka(line):
    return line[14:17] == "AKA"

def process_defendent(line, infile):
    data = {}
    while True:
        data['Number'] = line[4:6]
        data['Case Number'] = line[8:19]
        data['Defendent'] = line[20:41].strip()
        data['Complaintant'] = line[42:56].strip()
        data['Attorney'] = line[57:83].strip()
        data['Cont'] = line[84:].strip()
        return data

def is_bond(line):
    return line[20:24] == "BOND"

def process_bond(line, infile):
    data = {}
    while True:
        data['Bond'] = line[31:37]
        return data
    
def is_class(line):
    return line[8:11] == "CLS" or line[40:48] == "JUDGMENT"

def process_class(line, infile):
    data = {}
    while True:
        data['class'] = line[12:13]
        data['P'] = line[17:18]
        data['L'] = line[22:23]
        data['judgement'] = line[49:60]
        data['ADA'] = line[81:84]
        return data

def Merge(dict1, dict2):
    return(dict2.update(dict1))


def main():
    rpt_data = {}
    defend_data = {}
    offense_data = {}
    bond_data = {}
    class_data = {}

    # filename = input("Enter file name to process:")
    filename = "DISTRICT.DISTRICT_COURT_.04.11.23.AM.9999.CAL.txt"
    infile = open(filename, 'r')

    while True:
        line = infile.readline()
        if line == "" or is_summary_header(line):
            break
        elif line == "\n":
            continue
        elif is_aka(line):
            continue
        elif is_page_header(line):
            process_page_header(line, infile)
        elif is_report_header(line):
            rpt_data = process_report_header(line, infile)
        elif is_fingerprinted(line):
            finger_data = process_fingerprinted(line, infile)
            # print(finger_data)
        elif is_defendent(line):
            defend_data = process_defendent(line, infile)
            # print(defend_data)
        elif is_offense(line):
            offense_data = process_offense(line, infile)
            # print(offense_data.values())
        elif is_bond(line):
            bond_data = process_bond(line, infile)
            # print(bond_data.values())
        elif is_class(line):
            class_data = process_class(line, infile)
            # print(class_data.values())
        else:
            print(line, end='')

        Merge(rpt_data, defend_data)
        Merge(defend_data, offense_data)
        Merge(offense_data, class_data)
        Merge(class_data, bond_data)
        print(bond_data)

        





if __name__ == '__main__':
    main()

