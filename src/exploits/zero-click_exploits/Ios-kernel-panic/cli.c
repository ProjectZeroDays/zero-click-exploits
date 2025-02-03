#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void parse_arguments(int argc, char *argv[], char *ssid, int *channel, int *power) {
    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "--ssid") == 0 && i + 1 < argc) {
            strcpy(ssid, argv[i + 1]);
        } else if (strcmp(argv[i], "--channel") == 0 && i + 1 < argc) {
            *channel = atoi(argv[i + 1]);
        } else if (strcmp(argv[i], "--power") == 0 && i + 1 < argc) {
            *power = atoi(argv[i + 1]);
        }
    }
}

int main(int argc, char *argv[]) {
    char ssid[32] = "default_ssid";
    int channel = 1;
    int power = 20;

    parse_arguments(argc, argv, ssid, &channel, &power);

    printf("SSID: %s\n", ssid);
    printf("Channel: %d\n", channel);
    printf("Power: %d\n", power);

    return 0;
}
