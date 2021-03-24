print('Hello,Welcome!')

ans = input('Are you ready to play? (yes/no): ')

if ans.lower() == 'no':
    print('Sorry,Good Bye!')

if ans.lower() == 'yes':
    ans = input('Who Am I?')
    if ans.lower() == 'szocslaci':
     print('Yes,I Am!')

    while ans.lower() != 'szocslaci':
        print('No,try again!')
        ans = input('Who Am I?')
        if ans.lower() == 'szocslaci':
            print('Cool,I Am?')

    ans = input('How Old Am I?')
    if ans.lower() == '38':
        print('Correct,You are Amazing!')

    while ans.lower() != '38':
        print('What?Are You Kidding Me?')
        ans = input('How Old Am I?')
        if ans.lower() == '38':
            print('Yeees!')

    ans = input('Do You Like My Silly Game? (Yes/No):')

    if ans.lower() == 'no':
        print('What Were You Expecting, StarCraft 3? I Am A Begginer!')
        print('Bye!')

    if ans.lower() == 'yes':
        print('You Are So Kind, Thanks!')
        print('Bye!')

