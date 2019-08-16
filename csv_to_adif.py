import sys
import csv


class QSO(object):
    def __init__(self, callsign, my_summit, date, time, band, mode, o_call, o_summit, notes):
        self._callsign = callsign
        self._my_summit = my_summit
        self._date = date
        self._time = time
        self._band = band
        self._mode = mode
        self._o_call = o_call
        self._o_summit = o_summit
        self._notes = notes

    def is_activation(self):
        return self._my_summit != ''

    def is_chase(self):
        return self._o_summit != ''

    def get_SOTA_csv(self):
        output = f"V2,{self._callsign},{self._my_summit},"
        output += f"{self._date[6:]}/{self._date[4:6]}/{self._date[2:4]},"
        output += f"{self._time},{self._band},{self._mode},{self._o_call},"
        output += f"{self._o_summit},{self._notes}"
        return output

    def get_ADIF(self):
        output = ''
        output += f"<qso_date:{len(self._date)}>{self._date}\n"
        output += f"<time_on:{len(self._time)}>{self._time}\n"
        output += f"<call:{len(self._o_call)}>{self._o_call}\n"
        return output + "<eor>\n\n"

    def __lt__(self, other):
        return self._date < other._date

    def __gt__(self, other):
        return self._date > other._date


class Log(object):
    def __init__(self, callsign):
        self._callsign = callsign
        self._qsos = []

    def add(self, line):
        my_summit = line[0]
        date = line[1]
        time = line[2]
        band = line[3]
        mode = line[4]
        o_call = line[5]
        o_summit = line[6]
        notes = line[7]

        qso = QSO(self._callsign, my_summit, date, time, band, mode, o_call, o_summit, notes)
        self._qsos.append(qso)

    def sort(self):
        self._qsos.sort()

    def write_SOTA_activator_csv(self):
        print("Activator Log:")
        for qso in self._qsos:
            if qso.is_activation():
                print(qso.get_SOTA_csv())

    def write_SOTA_chaser_csv(self):
        print("Chaser Log:")
        for qso in self._qsos:
            if qso.is_chase():
                print(qso.get_SOTA_csv())

    def write_ADIF(self):
        print("ADIF File:")
        output = f"<adif_ver:5>3.0.5\n<programid:10>K7ASQpylog\n\n"
        output += "<EOH>\n\n"

        for qso in self._qsos:
            output += (qso.get_ADIF())

        print(output)


def build_log(filename, callsign):
    log = Log(callsign)
    infile = open(filename, 'r')
    csvreader = csv.reader(infile)
    for entry in csvreader:
        if entry[0][0] != '#':
            log.add(entry)
    infile.close()
    return log


def main():

    # if len(sys.argv) < 3:
    #     print("An error has occurred. Please try again.")
    #     sys.exit()

    # callsign = sys.argv[1]
    # droppedfile = sys.argv[2]
    # print("Callsign: ", callsign)
    # print("File: ",droppedfile)

    droppedfile = 'test2.csv'
    callsign = 'K7ASQ'

    log = build_log(droppedfile, callsign)
    log.sort()
    log.write_SOTA_activator_csv()
    log.write_SOTA_chaser_csv()
    log.write_ADIF()

main()
