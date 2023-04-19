#include <fcntl.h>
#include <linux/input.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    int fd = open("/dev/input/event2", O_RDONLY);
    if (fd == -1) {
        perror("open");
        exit(EXIT_FAILURE);
    }

    int counter = 0;
    while (true) {
        input_event event;
        if (read(fd, &event, sizeof(event)) != sizeof(event)) {
            perror("read");
            exit(EXIT_FAILURE);
        }

        counter++;
        if (counter == 2 && event.type == EV_KEY && event.value == 1) {
            printf("%d\n", event.code);
        }
        if (counter == 3) {
            counter = 0;
        }
    }

    close(fd);
    return 0;
}