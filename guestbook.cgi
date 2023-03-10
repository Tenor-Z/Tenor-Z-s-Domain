#!/usr/bin/perl

#variables that will be used later.
$guestbookreal = “guestbook-home.html”;
$return = “guestbook-home.html”;

read(STDIN, $buffer, $ENV{‘CONTENT_LENGTH’});
@pairs = split(/&/, $buffer);
foreach $pair(@pairs) {
($name, $value) = split(/=/, $pair);
$value =~ tr/+/ /;
$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack(“C”, hex($1))/eg;
$value =~ s/<\!\-\-.*\-\->//g; # get rid of SSI
$in{$name} = $value;
}

open (FILE,”$guestbookreal”);
@LINES=<FILE>;
chop (@LINES);
close(FILE);
$SIZE=@LINES;

open (GUEST,”>$guestbookreal”);

for ($i=0;$i<=$SIZE;$i++) {
$_=$LINES[$i];
print GUEST “$_\n”;
if (/<!–add–>/) {
if ($in{’email’} ne ”) {
print GUEST “<b><a href=\”mailto:$in{’email’}\”>”;
print GUEST “$in{‘name’}</a></b>:<br>\n”;
} else {
print GUEST “<b>$in{‘name’}</b>:<br>\n”;
}
if ($in{‘www’} ne ”) {
print GUEST “<a href=\”$in{‘url’}\”>”;
print GUEST “$in{‘www’}</a><br>\n”;
}
print GUEST “$in{‘body’}<p>\n”;
}
}

close (GUEST);
print “Location: $return\n\n”;