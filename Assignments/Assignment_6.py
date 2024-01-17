# Create a 'COVID-19 Chatbot' in which the Chatbot helps the person in the place of a clinic's doctor

# Create the initial statements and the answer you expect

print('Hello! Welcome to the COVID-19 Chatbot. How can I help you today? PLEASE WRITE ONE OF THE NUMBERS FROM THE '
      'OPTIONS: '
      'Vaccine(1) - Doctor\'s Appointment(2) - Info about COVID(3)')
answer1 = int(input())

vaccine_ans_global = ()
info_covid_global = ()

# Vaccine
if answer1 == 1:
    print('What would you like to know about COVID Vaccines? PLEASE WRITE ONE OF THE NUMBERS FROM THE OPTIONS: '
          'Vaccine Selection(1) - Vaccination Centre(2)')
    vaccine_ans = int(input())
    vaccine_ans_global = vaccine_ans

# Doctor's Appointment
elif answer1 == 2:
    print('Please give your name, mobile no. & email address')
    personal_info = input()
    print('Thank you for entering the info! We\'ll inform the doctor as soon as we can.')

# Info about COVID
elif answer1 == 3:
    print('What do you want to know about COVID? PLEAS WRITE ONE OF THE NUMBERS FROM THE OPTIONS: '
          'Information(1) - Precautions(2) - How to remain FIT?(3)')
    info_covid = int(input())
    info_covid_global = info_covid

# Vaccine Branch
if vaccine_ans_global == 1:
    print('Pfizer - 95% Effective - 2 doses given 3 weeks apart, '
          'Moderna - 94% Effective - 2 doses given 4 weeks apart, '
          'Covaxin - 78% Effective - 2 doses given 2 weeks apart')

elif vaccine_ans_global == 2:
    print('Dada Dev Hospital - Delhi : Nigam Pratibha Vidyalaya - Delhi : GB Pant Hospital - Delhi')

# COVID Info Branch
if info_covid_global == 1:
    print(
        'Coronavirus disease (COVID-19) is an infectious disease caused by the SARS-CoV-2 virus. Most people infected '
        'with the virus will experience mild to moderate respiratory illness and recover without requiring special '
        'treatment. However, some will become seriously ill and require medical attention. Older people and those with'
        ' underlying medical conditions like cardiovascular disease, diabetes, chronic respiratory disease, or cancer '
        'are more likely to develop serious illness. Anyone can get sick with COVID-19 and become seriously ill or die'
        ' at any age.')

elif info_covid_global == 2:
    print(
        'The best way to prevent and slow down transmission is to be well informed about the disease and how the virus'
        ' spreads. Protect yourself and others from infection by staying at least 1 metre apart from others, wearing a'
        ' properly fitted mask, and washing your hands or using an alcohol-based rub frequently. Get vaccinated when '
        'it’s your turn and follow local guidance.')

elif info_covid_global == 3:
    print(
        'While gym and group classes may be out, you can still cycle, hike, or walk. Or if you’re stuck at home, look '
        'online for exercise videos you can follow. There are many things you can do even without equipment, such as '
        'yoga and exercises that use your own bodyweight.')
