import glob
import random
import sys
from datetime import datetime, timedelta

def pick_winner():
    data_file = "data/nfl2014linesfromraw.csv"
    team_results_by_week = [{}] * 20
    good = 0
    bad = 0

    file = open(data_file)
    lines = file.readlines()
    start_date = datetime.strptime(lines[4].split(',')[0], "%m/%d/%y")

    lines.pop(0)
    i = -1
    max_line = [[0,0]]*20
    picked_winners = []
    while i < len(lines)-1:
        i = i + 1
        line = lines[i]
        line = line.rstrip()
        tmp = line.split(',')
        date = datetime.strptime(tmp[0], "%m/%d/%y")

        weekday = date.weekday()
        if weekday == 3:
            date = date + timedelta(days=3)
        if weekday == 0:
            date = date - timedelta(days=1)

        week = date - start_date

        if week.total_seconds() < 0:
            week = 1
        else:
            week = int(week.total_seconds() / (60 * 60 * 24 * 7)) 

        # if week just incremented
        if max_line[week] == [0,0] and week > 1:
            picked_winners.append(max_line[week-1][2])

        visitor_line = float(tmp[2])
        home_line = float(tmp[4])

        if (visitor_line < 0 and visitor_line < max_line[week][0]):
            chosen_team = tmp[1]
            if chosen_team not in picked_winners:
                max_line[week] = [visitor_line,i,chosen_team]

        if (home_line < 0 and home_line < max_line[week][0]):
            chosen_team = tmp[3]
            if chosen_team not in picked_winners:
                max_line[week] = [home_line,i,chosen_team]


    i = -1

    print "\n"
    for best in max_line:
        #print best
        i += 1
        try:
            current_pick = best[2]
            print "Week: " + str(i+1)
            print "Pick: " + current_pick
            print "\n"
        except IndexError:
            sys.exit(0)

if __name__ == "__main__":
    pick_winner()

