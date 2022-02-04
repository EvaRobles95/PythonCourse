"""PDI english"""

vp_code = input('Versuchspersonen-code?   ')

file = open(vp_code +'_pdi.csv','w')

questions=['Do you ever feel as if you are under control of some force or power other than yourself?\n',
           'Do you ever feel as if you are a robot or zombie without a will of your own?\n',
           'Do you ever feel as if you are possessed by someone or something else?\n',
           'Do you ever feel like your feelings or actions are not under your control?\n',
           'Do you ever feel as if someone or something is playing games with your mind?\n',
           'Do you ever feel as if people seem to drop hints about you or say things with a double meaning?\n',
           'Do you ever feel as if things in magazines or on TV were written especially for you?\n',
           'Do you ever feel like everyone is gossiping about you?\n',
           'Do you ever feel as if some people are not what they seem to be?\n',
           'Do things around you ever feel unreal, as though it was all part of an experiment?\n',
           'Do you ever feel as if someone is deliberately trying to harm you??\n',
           'Do you ever feel as if you are being prosecuted in any way?\n',
           'Do you ever feel as if there is a conspiracy against you?\n',
           'Do you ever feel as if some organization or institution has it in for you?\n',
           'Do you ever feel as if someone or something is watching you?\n',
           'Do you ever feel as if you have special abilities or powers?\n',
           'Do you ever feel as if there is a special purpose or mission to your life?\n',
           'Do you ever feel as if there is a mysterious power working for the good in the world?\n',
           'Do you ever feel as if you are or destined to be someone very important?\n',
           'Do you ever feel that you are a very special or unusual person?\n',
           'Do you ever feel that you are especially close to God?\n',
           'Do you ever think that people can communicate telepathically?\n',
           'Do you ever feel as if electrical devices such as computers can influence the way you think?\n',
           'Do you ever feel as if there are forces around you which affected you in strange ways?\n',
           'Do you ever feel as if you have been chosen by God in some way?\n',
           'Do you believe in the power of witchcraft, voodoo or the occult?\n',
           'Are you often worried that your partner may be unfaithful?\n',
           'Do you ever think that you smell very unsual to other people?\n',
           'Do you ever feel as if your body is changing in a peculiar way?\n',
           'Do you ever think that strangers want to have sex with you?\n',
           'Do you ever feel that you have sinned more than the average person?\n',
           'Do you ever feel that people look at you oddly because of your appearance?\n',
           'Do you ever feel as if you had no thoughts in your head at all?\n',
           'Do you ever feel as if your insides might be rotting?\n',
           'Do you ever feel as if the world is about to end?\n',
           'Do your thoughts ever feel alien to you in some way?\n',
           'Have your thoughts ever been so vivid that you were worried other people would hear them?\n',
           'Do you ever feel as if your own thoughts were being echoed back to you?\n',
           'Do you ever feel as if your thoughts were blocked by someone or something else?\n',
           'Do you ever feel as if other people can read your mind?\n']

response_global = 0
belastung_global, ablenkend_global, frequenz_global = 0,0,0
for q in range(len(questions)):
    print('\n\n\n\n')
    print(questions[q])
    answer = int(input('0 for No, 1 for Yes\n'))
    response_global += answer
    if answer == 1:
        print('How distressing is this for you? \n1 (not at all distressing) to 5 (very distressing)?\n')
        belastung = int(input())
        print('How often do you think about this? \n1 (hardly ever think about it) to 5 (think about it all the time)?\n')
        ablenkend = int(input())
        print('How much do you believe that this is true?\n1 (Do not believe it is true) to 5 (believe it is absolutely true)\n')
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

print('\n\nThank you! PDI Survey completed!')
