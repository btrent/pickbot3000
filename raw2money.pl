#!/usr/bin/perl

#9/25/14 20:25,,,,,,,,,,Picks
#101ÊN.Y. Giants,169,170,170,170,175,170,170,170,165,
#102ÊWashington,-186,-200,-190,-200,-200,-200,-190,-200,-190,
#"WAS-QB-Robert Griffin III-OUT | TV: CBS | MOSTLY CLOUDY, 30% CHANCE SHOWERS EARLY. NORTH WIND 10-15. GAME TEMP 66, RH 78%",,,,,,,,,,
#9/28/14 13:00,,,,,,,,,,Picks
#251ÊMiami,-200,-200,-200,-200,-200,-200,-200,-200,-200,
#252ÊOakland,178,170,175,170,175,170,175,170,170,
#"TV: CBS, DTV: 711",,,,,,,,,,

$i = -1;
$date = "";
@teams = ("","");
@odds = ("","");
#@lines = ();


@data = ();
open(A, "data/nfl_raw.csv");
while(<A>) {
    chomp($_);
    if ($_ =~ /[0-9]{1,2}\//) {
	$i++;
	@t = split(/ /, $_);
	$date = $t[0];
	@teams = ("","");
	@odds = ("","");
    } elsif ($_ =~ /[0-9]{3},/) {
	@t = split(/,/, $_);
	$name = $t[0];
	$name =~ s/^[^A-Za-z]+//;
	$odds = $t[2];
	if ($teams[0] eq "") {
	    $teams[0] = $name;
	    $odds[0] = $odds;
	} else {
	    $teams[1] = $name;
	    $odds[1] = $odds;
	}
    } else {
#	$lines[@lines] = $date . "," . $teams[0] . "," . $odds[0] . "," . $teams[1] . "," . $odds[0] . "\n";
	print $date . "," . $teams[0] . "," . $odds[0] . "," . $teams[1] . "," . $odds[1] . "\n";
    }
}
close(A);
