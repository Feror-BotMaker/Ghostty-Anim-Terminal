#include "all_frames.c"
#include <stdio.h>
#include <unistd.h>

int main() {
    init_frames();
    while (1) {
        for (int i = 0; i < num_frames; i++) {
            printf("\033[H\033[J");
            printf("%s\n", frames[i]);
            usleep(16600);
        }
    }
    return 0;
}