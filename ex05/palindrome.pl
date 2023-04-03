#!/usr/bin/perl

print "Enter a string: ";

$input = <STDIN>;

chomp($input);

if ($input eq reverse $input) {
    print("The string is a palindrome!\n");
} else {
    print("The string is not a palindrome.\n");
}
