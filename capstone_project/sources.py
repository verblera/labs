from getting_data import news_agencies

agencies_list = []
agencies_en = []
agencies_de = []
agencies_it = []
agencies_ru = []
lang_dict = {}
country_dict = {}
category_list = []
description_words = {}

for agency in news_agencies:
    agencies_list.append(agency['name'])
    if agency['language'] in lang_dict:
        lang_dict[agency['language']] += 1
    else:
        lang_dict[agency['language']] = 1
    if agency['country'] in country_dict:
        country_dict[agency['country']] += 1
    else:
        country_dict[agency['country']] = 1
    if agency['language'] == 'en':
        agencies_en.append(agency['name'])
    elif agency['language'] == 'de':
        agencies_de.append(agency['name'])
    elif agency['language'] == 'it':
        agencies_it.append(agency['name'])
    elif agency['language'] == 'ru':
        agencies_ru.append(agency['name'])
    category_list.append(agency['category'])

    for word in agency['description']:
        if word in description_words:
            description_words[word] +=1
        else:
            description_words[word] = 1

print(f'Here is a list of available sources: \n{agencies_list}')
print(f'Here is a list of sources in English: \n{agencies_en}')
print(f'Here is a list of sources in German: \n{agencies_de}')
print(f'Here is a list of sources in Italian: \n{agencies_it}')
print(f'Here is a list of sources in Russian: \n{agencies_ru}')

with open('Analysis of sources.txt', 'a') as file:
    file.write('A FULL LIST OF SOURCES: \n{agencies_list}\n')
    file.write('ALL SOURCES IN SELECTED LANGUAGES: \n')
    file.write(f'English sources:{agencies_en}\nGerman sources:{agencies_de}\n'
               f'Italian sources:{agencies_it}\nRussian sources:{agencies_ru}\n\n\n')

with open('Analysis of sources.txt', 'a') as file:
    for k, v in lang_dict.items():
        if v != 1:
            file.write(f'\nThere are {v} sources in {k}')
            print(f'\nThere are {v} sources in {k}')
        else:
            file.write(f'\nThere is {v} source in {k}')
            print(f'\nThere is {v} source in {k}')


input_file = open('Analysis of sources.txt', 'rt')
data = input_file.read()
data = data.replace(' ru\n', 'Russian')
data = data.replace(' en\n', 'English')
data = data.replace(' no\n', 'Norwegian')
data = data.replace(' it\n', 'Italian')
data = data.replace(' ar\n', 'Arabic')
data = data.replace(' ud\n', 'unknown')
data = data.replace(' de\n', 'German')
data = data.replace(' pt\n', 'Portuguese')
data = data.replace(' es\n', 'Spanish')
data = data.replace(' fr\n', 'French')
data = data.replace(' he\n', 'Hebrew')
data = data.replace(' se\n', 'Serbian')
data = data.replace(' nl\n', 'Dutch')
data = data.replace(' zh\n', 'Chinese')
input_file.close()
output_file = open('Analysis of sources.txt', 'wt')
data += '\n\n'
output_file.write(data)
output_file.close()


with open('Analysis of sources.txt', 'a') as file:
    for k, v in country_dict.items():
        if v == 1:
            file.write(f'\nThere is {v} source in {k}')
            print(f'\nThere is {v} source in {k}')
        else:
            file.write(f'\nThere are {v} sources in {k}')
            print(f'\nThere are {v} sources in {k}')


input_file = open('Analysis of sources.txt', 'rt')
data = input_file.read()
data = data.replace(' ru\n', 'Russia')
data = data.replace(' us\n', 'USA')
data = data.replace(' au\n', 'Australia')
data = data.replace(' no\n', 'Norway')
data = data.replace(' it\n', 'Italian')
data = data.replace(' sa\n', 'Saudi Arabia')
data = data.replace(' pk\n', 'Pakistan')
data = data.replace(' gb\n', 'Great Britain')
data = data.replace(' de\n', 'Germany')
data = data.replace(' br\n', 'Brazil')
data = data.replace(' ca\n', 'Canada')
data = data.replace(' es\n', 'Spain')
data = data.replace(' ar\n', 'Argentina')
data = data.replace(' fr\n', 'France')
data = data.replace(' in\n', 'India')
data = data.replace(' is\n', 'Iceland')
data = data.replace(' se\n', 'Serbia')
data = data.replace(' za\n', 'South Africa')
data = data.replace(' nl\n', 'the Netherlands')
data = data.replace(' zh\n', 'China')
input_file.close()
output_file = open('Analysis of sources.txt', 'wt')
data += '\n\n'
output_file.write(data)
output_file.close()

set_category = set(category_list)
with open('Analysis of sources.txt', 'a') as file:
    file.write(f'\nHere {len(set_category)} categories: {set_category}')
print(f'Here {len(set_category)} categories: {set_category}')

# description
print(description_words(sorted(x.items(), key=lambda item: item[1])))