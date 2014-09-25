import glob
import random
from datetime import datetime, timedelta

all_teams = ['Arizona Cardinals', 'Atlanta Falcons', 'Baltimore Ravens', 'Buffalo Bills', 'Carolina Panthers', 'Chicago Bears', 'Cincinnati Bengals', 'Cleveland Browns', 'Dallas Cowboys', 'Denver Broncos', 'Detroit Lions', 'Green Bay Packers', 'Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Kansas City Chiefs', 'Miami Dolphins', 'Minnesota Vikings', 'New England Patriots', 'New Orleans Saints', 'New York Giants', 'New York Jets', 'Oakland Raiders', 'Philadelphia Eagles', 'Pittsburgh Steelers', 'San Diego Chargers', 'San Francisco 49ers', 'Seattle Seahawks', 'St Louis Rams', 'Tampa Bay Buccaneers', 'Tennessee Titans', 'Washington Redskins']

def pick_winner():
    global all_teams

    data_file = "data/nfl2014lines.csv"
    team_results_by_week = [{}] * 20
    good = 0
    bad = 0

    file = open(data_file)
    lines = file.readlines()
    start_date = datetime.strptime(lines[4].split(',')[0], "%m/%d/%Y")

    lines.pop(0)
    i = -1
    max_line = [[0,0]]*20
    picked_winners = []
    while i < len(lines)-1:
        i = i + 1
        line = lines[i]
        line = line.rstrip()
        tmp = line.split(',')
        date = datetime.strptime(tmp[0], "%m/%d/%Y")

        weekday = date.weekday()
        if weekday == 3:
            date = date + timedelta(days=3)
        if weekday == 0:
            date = date - timedelta(days=1)

        week = date - start_date
#        print date

        if week.total_seconds() < 0:
            week = 1
        else:
            week = int(week.total_seconds() / (60 * 60 * 24 * 7)) 

#        print week

        if tmp[5] == "":
            continue
        line = float(tmp[5])
        home_score = float(-1)
        visitor_score = float(-1)
        winning_team = None
        try:
            home_score = float(tmp[4])
            visitor_score = float(tmp[2])
            if home_score < visitor_score:
                winning_team = tmp[1]
                team_results_by_week[week][tmp[1]] = 'won'
                team_results_by_week[week][tmp[3]] = 'lost'
            else:
                winning_team = tmp[3]
                team_results_by_week[week][tmp[1]] = 'list'
                team_results_by_week[week][tmp[3]] = 'won'
        except:
            pass

#        print line
        if ((line > 0 and line > abs(max_line[week][0])) or (line < 0 and line < abs(max_line[week][0])*-1)):
            if line > 0:
                chosen_team = tmp[3]
            else:
                chosen_team = tmp[1]
            if chosen_team not in picked_winners:
                max_line[week] = [line,i,winning_team]
                picked_winners.append(winning_team)

    i = -1

    for best in max_line:
        i += 1
        if len(best) == 3:
            #print week
            tmp = lines[best[1]].split(',')
            line = best[0]
            winning_team = best[2]

            if line > 0:
                team = tmp[3]
            else:
                team = tmp[1]

            print lines[best[1]]
            tmpp = lines[best[1]].split(',')
            our_team = None
            if line > 0:
                our_team = tmpp[3]
            else:
                our_team = tmpp[1]
            print "Pick: " + our_team

            if winning_team is not None and team != winning_team:
                #print bad
                bad = bad + 1
#                print team + " were favored to win by " + str(line) + ". " + str(winning_team) + " won."
            else:
                #print good
                good = good + 1

            
    if (good > 0 or bad > 0):
        print "Record so far: " + str(int(float(good)/float(good+bad))*100) + " %"


if __name__ == "__main__":
    all_good = 0
    all_bad = 0

    """
    [good,bad,picks] = test_all()
    [good,bad,picks] = test_most()
    for i in [0] * 100:
        [good,bad,picks] = test_most()
        all_good = all_good + good
        all_bad = all_bad + bad

    print float(all_good)/float(all_good+all_bad)
    """
    pick_winner()

