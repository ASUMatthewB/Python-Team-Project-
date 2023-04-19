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



def main():
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
        else:
            print(line, end='')

if __name__ == '__main__':
    main()

