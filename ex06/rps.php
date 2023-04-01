<?php

$choices = array("rock", "paper", "scissors");

echo "Please choose rock, paper, or scissors: ";
$userChoice = trim(fgets(STDIN));

// Check if user input is valid
if (!in_array($userChoice, $choices)) {
    echo "Invalid choice. Please choose rock, paper, or scissors.\n";
    exit();
}

$computerChoice = $choices[array_rand($choices)];
echo "Computer chose $computerChoice.\n";

if ($userChoice == $computerChoice) {
    echo "It's a tie!\n";
} elseif ($userChoice == "rock" && $computerChoice == "scissors" ||
          $userChoice == "paper" && $computerChoice == "rock" ||
          $userChoice == "scissors" && $computerChoice == "paper") {
    echo "You win!\n";
} else {
    echo "Computer wins.\n";
}

?>
