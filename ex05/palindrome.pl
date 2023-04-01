#!/usr/bin/perl

print "Enter a string: ";
# my $string = readline(STDIN);
my $string = <>;
chomp $string;

my $reverse = reverse $string;

if ($string eq $reverse) {
    print "the string is a palindrome\n";
} else {
    print "the string is not a palindrome\n";
}
