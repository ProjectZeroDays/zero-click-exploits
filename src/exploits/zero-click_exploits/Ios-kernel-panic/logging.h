#ifndef LOGGING_H
#define LOGGING_H

#include <time.h>
#include <stdarg.h>
#include <stdio.h>

#define LOG_LEVEL_INFO "INFO"
#define LOG_LEVEL_WARNING "WARNING"
#define LOG_LEVEL_ERROR "ERROR"

void log_message(const char *level, const char *format, ...) {
    va_list args;
    va_start(args, format);

    time_t now;
    time(&now);
    struct tm *local = localtime(&now);

    printf("[%02d:%02d:%02d] [%s] ", local->tm_hour, local->tm_min, local->tm_sec, level);
    vprintf(format, args);
    printf("\n");

    va_end(args);
}

#endif // LOGGING_H
