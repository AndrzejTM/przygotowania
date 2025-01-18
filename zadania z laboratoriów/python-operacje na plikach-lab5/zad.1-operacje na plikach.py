with open("system_logs.txt", "r") as file, open('errors.log', 'w') as error_file:
    count_INFO = 0
    count_WARNING = 0
    count_ERROR = 0
    hourly_events = {}

    for line in file:
        # Liczenie typów zdarzeń
        if "INFO" in line:
            count_INFO += 1
        if "WARNING" in line:
            count_WARNING += 1
        if "ERROR" in line:
            count_ERROR += 1
            error_file.write(line)

        # Ekstrakcja godziny (zakładamy format [HH:MM:SS])
        if "[" in line and ":" in line:
            time_part = line.split("[")[1].split("]")[0]
            hour = time_part.split(":")[0]  # Pobieramy godzinę
            if hour in hourly_events:
                hourly_events[hour] += 1
            else:
                hourly_events[hour] = 1

    # Wyświetlenie liczby zdarzeń każdego typu
    print("Ilość INFO:", count_INFO)
    print("Ilość WARNING:", count_WARNING)
    print("Ilość ERROR:", count_ERROR)

    # Znalezienie godziny z największą liczbą zdarzeń
    max_hour = max(hourly_events, key=hourly_events.get)
    max_hour_count = hourly_events[max_hour]

    # Zapis do pliku summary.log
    with open('summary.log', 'w') as summary_log:
        summary_log.write(f"Hour with most events: {max_hour} ({max_hour_count} events)\n")
