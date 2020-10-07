#Joseph Morris
#1840300

if __name__ == '__main__':

    user_file = open("inputDates.txt")
    lines_in_file = user_file.readlines()

    dictionary_of_months = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
                   "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}

    #create a list for dates
    parsing_the_dates = []

    for each_line in lines_in_file:
        new_date = []
        seperator = each_line.find(' ')
        if seperator != -1:
            month_is = each_line[0:seperator]
            if month_is in dictionary_of_months:
                comma = each_line.find(',', seperator, len(each_line))
                if comma != -1:
                    date = each_line[seperator + 1:comma]
                    new_date.append(date)
                    new_date.append(month_is)
                    year = each_line[comma + 1:].strip('\n').strip(' ')
                    new_date.append(year)
                    parsing_the_dates.append(new_date)

    new_formatted_dates = ""
    for the_dates in parsing_the_dates:
        month_as_a_value = str(dictionary_of_months[the_dates[1]])
        new_formatted_dates += (month_as_a_value + '/' + the_dates[0] + '/' + the_dates[2])
        new_formatted_dates += "\n"

    new_file_with_formatted_dates = open("parsedDates.txt", 'w')
    new_file_with_formatted_dates.write(new_formatted_dates)