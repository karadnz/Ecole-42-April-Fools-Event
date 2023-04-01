#include <stdio.h>
#include <string.h>

int get_card_value(char card) {
    if (card >= '2' && card <= '9') {
        return card - '0';
    } else if (card == 'T' || card == 'J' || card == 'Q' || card == 'K') {
        return 10;
    } else if (card == 'A') {
        return 11;
    } else {
        return 0;
    }
}

int calculate_hand_value(const char *hand) {
    int value = 0;
    int num_aces = 0;

    for (int i = 0; i < strlen(hand); i++) {
        int card_value = get_card_value(hand[i]);

        if (hand[i] == 'A') {
            num_aces++;
        }

        value += card_value;
    }

    while (value > 21 && num_aces > 0) {
        value -= 10;
        num_aces--;
    }

    return value;
}

int main() {
    char hand[50];

    printf("Enter a blackjack hand (e.g. D8, A4, AA8): ");
    scanf("%s", hand);

    int hand_value = calculate_hand_value(hand);
    printf("The value of the hand is: %d\n", hand_value);

    return 0;
}