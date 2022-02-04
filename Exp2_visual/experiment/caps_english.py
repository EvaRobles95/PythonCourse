"""CAPS ENGLISH"""

vp_code = input('Versuchspersonen-code?   ')

file = open(vp_code +'_caps.csv','w')

questions = ['1 Do you ever notice that sounds are much louder than they normally would be?\n',
             '2 Do you ever sense the presence of another being, despite being unable to see any evidence?\n',
             '3Do you ever hear your own thoughts echoed or repeated?\n',
             '4Do you ever see shapes, lights or colors even though there is nothing really there?\n',
             '5Do you ever experience unusual burning sensations or other strange feelings in your body?\n',
             '6Do you ever hear noises or sounds when there is nothing there to explain them?\n',
             '7Do you ever hear your own thoughts spoken aloud in your head, so that someone near might be able to hear them?\n',
             '8Do you ever detect smells which dont seem to come from your surrounding?\n',
             '9Do you ever have the sensation that your body, or part of it, is changing or has changed shape?\n',
             '10Do you ever have the sensation that your limbs might not be your own or might not be preoperly connected to your body?\n',
             '11Do you ever hear voices commenting on what you are saying or doing?\n',
             '12Do you ever feel like someone is touching you, but when you look nobody is there?\n',
             '13Do you ever hear voices saying words or sentences when there is no one around that might account for it?\n',
             '14 Do you ever experience unexplained tastes in your mouth?\n',
             '15Do you ever find that sensations happen all at once and flood you with information?\n',
             '16Do you ever find that sounds are distorted in strange or unusual ways?\n',
             'Do you ever have difficulty distinguishing one sensation from another?\n',
             'Do you ever smell everyday odors and think they are unusually strong?\n',
             '19Do you ever find the appearance of things or people seems to change in a puzzling way, eg, distorted shapes, sizes or colors?\n',
             'Do you ever find that your skin is more sensitive to touch, heat or cold than usual?\n',
             'Do you ever think that food or drink tastes much stronger than it usually would?\n',
             '22Do you ever look in the mirror and think that your face seems different from usual?\n',
             'Do you ever have days where lights or colors seem brighter or more intense than usual?\n',
             'Do you ever have the feeling of being uplifted, as if driving or rolling over a road while sitting quietly?\n',
             'Do you ever find that common smells sometimes seem unusually different?\n',
             'Do you ever think that everyday things look abnormal to you?\n',
             'Do you ever find that your experience of time changes dramatically?\n',
             'Have you ever heard 2 or more unexplained voices talking with each other?\n',
             'Do you ever experience smells or odors that people next to you seem unaware of?\n',
             'Do you ever notice that food or drink seems to have an unusual taste?\n',
             'Do you ever see things that other people cannot?\n',
             'Do you ever hear sounds or music that people near you do not hear?\n']

response_global = 0
belastung_global, ablenkend_global, frequenz_global = 0,0,0
for q in range(len(questions)):
    print('\n\n\n\n')
    print(questions[q])
    answer = int(input('0 für Nein, 1 für Ja\n'))
    response_global += answer
    if answer == 1:
        print('How distressing is this for you? \n1 (not distressing) to 5 (very distressing)?\n')
        belastung = int(input())
        print('How distracting is this? \n1 (not distracting) to 5 (very distracting)?\n')
        ablenkend = int(input())
        print('How often does this happen?\n1 (rarely ever happens) to 5 (happens all the time)?\n')
        frequenz = int(input())
        
    elif answer ==0:
        belastung, ablenkend, frequenz = 0,0,0
        
    belastung_global+=belastung
    ablenkend_global+=ablenkend
    frequenz_global += frequenz

    print('\n\n')

    file.write('Q%i,%i,%i,%i,%i\n' % (q+1, answer,belastung,ablenkend,frequenz))
file.write('Global,%i,%i,%i,%i' % (response_global,belastung_global, ablenkend_global, frequenz_global))

file.close()

print('\n\nThank you! CAPS survey completed.')
