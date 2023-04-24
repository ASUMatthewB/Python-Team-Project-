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
    while True:
        line = infile.readline()
        if line == "" or is_fingerprinted:
            break

def is_defendent(line):
    return line[20:21].isnumeric()

def process_defendent(line, infile):
    

def main():
    rpt_data = {}
    defend_data = {}
    offense_data = {}
    
    # filename = input("Enter file name to process:")
    filename = "DISTRICT.DISTRICT_COURT_.04.11.23.AM.9999.CAL.txt"
    infile = open(filename, 'r')

    while True:
        line = infile.readline()
        if line == "" or is_summary_header(line):
            break
        elif line == "\n":
            continue
        elif is_page_header(line):
            process_page_header(line, infile)
        elif is_report_header(line):
            rpt_data = process_report_header(line, infile)
        elif is_fingerprinted(line):
            finger_data = process_fingerprinted(line, infile)
        else:
            print(line, end='')

if __name__ == '__main__':
    main()

