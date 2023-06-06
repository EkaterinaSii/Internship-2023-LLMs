import re
from re import search

file_names = [f'page # {i}.txt' for i in range(1, 65) if i not in [63, 64]]
file_names.append('links_main.txt')
unique_links = set()

links_to_ignore = ['https://www.samk.fi/uraseurantakysely-uraseuranta',
                   'https://www.samk.fi/osaamisalueet',
                   'https://www.samk.fi/library/infopoint/?lang=en',
                   'https://www.samk.fi/library',
                   'https://www.samk.fi/satakunnan-ammattikorkeakoulun-opiskelijakunta-sammakko',
                   'https://www.samk.fi/en/education/admissions/bring-your-own-device',
                   'https://www.samk.fi/en/about-samk/international-events/international-teaching-and-expertise-week-of-tourism',
                   'https://www.samk.fi/en/education/master-robot-builders-2023',
                   'https://www.samk.fi/en/library/infopoint/?lang=en',
                   'https://www.samk.fi/yhteystiedot/henkilohaku',
                   'https://www.samk.fi/en/about-samk',
                   'https://www.samk.fi/en//../faculties',
                   'https://www.samk.fi/en/education/choose-finland',
                   'https://www.samk.fi/en/study/bachelor-degree/nursing',
                   'https://www.samk.fi/en/about-samk-2/safety/code-of-conduct-2',
                   'https://www.samk.fi/en/education/open-studies',
                   'https://www.samk.fi/en/education/choose-satakunta-university-of-applied-sciences',
                   'https://www.samk.fi/en/education/bachelor-degree/international_business',
                   'https://www.samk.fi/en/education/studying-at-a-university-of-applied-sciences',
                    'https://www.samk.fi/en/education/master-degree',
                    'https://www.samk.fi/en/how-to-apply/master-degree',
                    'https://www.samk.fi/en/education/to-working-life/enterprise-accelerator',
                    'https://www.samk.fi/en/about-samk-2/strategy',
                    'https://www.samk.fi/en/education/samk-summer-school',
                    'https://www.samk.fi/en/education/bachelor-degree',
                    'https://www.samk.fi/en/education/international-samk',
                    'https://www.samk.fi/en/education/bachelor-degree/logistics',
                    'https://www.samk.fi/en/new-student/enrollment',
                    'https://www.samk.fi/en/education/admissions/tuition-fees-scholarships',
                    'https://www.samk.fi/en/education/bachelor-degree/artificial-intelligence',
                  'https://www.samk.fi/en/education/bachelor-degree/sea_captain',
                   'https://www.samk.fi/en/research-and-cooperation/principles-of-open-science-and-research',
                   'https://www.samk.fi/en/research-and-cooperation/research-groups'



                   ]


for file_name in file_names:
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            if line.endswith('/'):
                line = line[:-1]
            unique_links.add(line)


with open("final_links2.txt", 'w') as output_file:
    for link in unique_links:
        if search('tietoa-meista',link) or search('tyoelama-ja-tutkimus',link) or search('ajankohtaista',link) or  search('opiskelu',link) or search('uutisen-avainsana',link) or search('international-events',link) or link in links_to_ignore:
            pass
        else:
            output_file.write(link + '\n')

print("Unique links have been saved to final_links2.txt.")

