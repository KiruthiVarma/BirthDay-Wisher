from playsound import playsound
import threading
import time

cake='''

           _..._  ,s$$$s.                                                                                          _..._  ,s$$$s.
         .$$$$$$$s$$ss$$$$,                                                                                     .$$$$$$$s$$ss$$$$,
         $$$sss$$$$s$$$$$$$                                                                                     $$$sss$$$$s$$$$$$$
         $$ss$$$$$$$$$$$$$$                                   (             )                                   $$ss$$$$$$$$$$$$$$
         '$$$s$$$$$$$$$$$$'                           )      (*)           (*)      (                           '$$$s$$$$$$$$$$$$'
          '$$$$$$$$$$$$$$'                           (*)      |             |      (*)                           '$$$$$$$$$$$$$$'
            S$$$$$$$$$$$'                             |      |~|           |~|      |                              S$$$$$$$$$$$'
             '$$$$$$$$$'                             |~|     | |           | |     |~|                              '$$$$$$$$$'
               '$$$$$'                               | |     | |           | |     | |                                '$$$$$'
                '$$$'                               ,| |a@@@@| |@@@@@@@@@@@| |@@@@a| |.                                '$$$'
                  ;                            .,a@@@| |@@@@@| |@@@@@@@@@@@| |@@@@@| |@@@@a,.                            ;
                 ;                           ,a@@@@@@| |@@@@@@@@@@@@.@@@@@@@@@@@@@@| |@@@@@@@a,                         ; 
                 ;                          a@@@@@@@@@@@@@@@@@@@@@' . `@@@@@@@@@@@@@@@@@@@@@@@@a                        ;
                 ',                         ;`@@@@@@@@@@@@@@@@@@'   .   `@@@@@@@@@@@@@@@@@@@@@';                        ',
                  ;                         ;@@@`@@@@@@@@@@@@@'     .     `@@@@@@@@@@@@@@@@'@@@;                         ;
                 ,'                         ;@@@;,.aaaaaaaaaa       .       aaaaa,,aaaaaaa,;@@@;                        ,'
                 ;                          ;;@;;;;@@@@@@@@;@      @.@      ;@@@;;;@@@@@@;;;;@@;                        ;
                 ',                         ;;;;;;;@@@@;@@;;@    @@ . @@    ;;@;;;;@@;@@@;;;;;;;                        ',
                  ',                        ;;;;;;;;@@;;;;;;;  @@   .   @@  ;;;;;;;;;;;@@;;;;@;;                         ',
                   ;                        ;;;;;;;;;;;;;;;;;@@     .     @@;;;;;;;;;;;;;;;;@@@;                          ;
                  '                     ,%%%;;;;;;;;@;;;;;;;;       .       ;;;;;;;;;;;;;;;;@@;;%%%,                      '
                                     .%%%%%%;;;;;;;@@;;;;;;;;     ,%%%,     ;;;;;;;;;;;;;;;;;;;;%%%%%%,
                                    .%%%%%%%;;;;;;;@@;;;;;;;;   ,%%%%%%%,   ;;;;;;;;;;;;;;;;;;;;%%%%%%%,
                                    %%%%%%%%`;;;;;;;;;;;;;;;;  %%%%%%%%%%%  ;;;;;;;;;;;;;;;;;;;'%%%%%%%%
                                    %%%%%%%%%%%%`;;;;;;;;;;;;,%%%%%%%%%%%%%,;;;;;;;;;;;;;;;'%%%%%%%%%%%%
                                    `%%%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%%%%%%'
                                      `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
                                          `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
                                                 """"""""""""""`,,,,,,,,,'"""""""""""""""""
                                                                `%%%%%%%'
                                                                 `%%%%%'
                                                                   %%% 
                                                                  %%%%%
                                                               .,%%%%%%%,.
                                                          ,%%%%%%%%%%%%%%%%%%%,

'''


wish='''

$$\   $$\                                               $$$$$$$\  $$\            $$\     $$\             $$\                     
$$ |  $$ |                                              $$  __$$\ \__|           $$ |    $$ |            $$ |                    
$$ |  $$ | $$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\       $$ |  $$ |$$\  $$$$$$\ $$$$$$\   $$$$$$$\   $$$$$$$ | $$$$$$\  $$\   $$\ 
$$$$$$$$ | \____$$\ $$  __$$\ $$  __$$\ $$ |  $$ |      $$$$$$$\ |$$ |$$  __$$\\_$$  _|  $$  __$$\ $$  __$$ | \____$$\ $$ |  $$ |
$$  __$$ | $$$$$$$ |$$ /  $$ |$$ /  $$ |$$ |  $$ |      $$  __$$\ $$ |$$ |  \__| $$ |    $$ |  $$ |$$ /  $$ | $$$$$$$ |$$ |  $$ |
$$ |  $$ |$$  __$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |      $$ |  $$ |$$ |$$ |       $$ |$$\ $$ |  $$ |$$ |  $$ |$$  __$$ |$$ |  $$ |
$$ |  $$ |\$$$$$$$ |$$$$$$$  |$$$$$$$  |\$$$$$$$ |      $$$$$$$  |$$ |$$ |       \$$$$  |$$ |  $$ |\$$$$$$$ |\$$$$$$$ |\$$$$$$$ |
\__|  \__| \_______|$$  ____/ $$  ____/  \____$$ |      \_______/ \__|\__|        \____/ \__|  \__| \_______| \_______| \____$$ |
                    $$ |      $$ |      $$\   $$ |                                                                     $$\   $$ |
                    $$ |      $$ |      \$$$$$$  |                                                                     \$$$$$$  |
                    \__|      \__|       \______/                                                                       \______/                                                                                                                                                                     
                                                                                                                                                                    
                    PPPPPPPPPPPPPPPPP                     lllllll                   kkkkkkkk                           
                    P::::::::::::::::P                    l:::::l                   k::::::k                           
                    P::::::PPPPPP:::::P                   l:::::l                   k::::::k                           
                    PP:::::P     P:::::P                  l:::::l                   k::::::k                           
                      P::::P     P:::::Puuuuuu    uuuuuu   l::::l uuuuuu    uuuuuu   k:::::k    kkkkkkkaaaaaaaaaaaaa   
                      P::::P     P:::::Pu::::u    u::::u   l::::l u::::u    u::::u   k:::::k   k:::::k a::::::::::::a  
                      P::::PPPPPP:::::P u::::u    u::::u   l::::l u::::u    u::::u   k:::::k  k:::::k  aaaaaaaaa:::::a 
                      P:::::::::::::PP  u::::u    u::::u   l::::l u::::u    u::::u   k:::::k k:::::k            a::::a 
                      P::::PPPPPPPPP    u::::u    u::::u   l::::l u::::u    u::::u   k::::::k:::::k      aaaaaaa:::::a 
                      P::::P            u::::u    u::::u   l::::l u::::u    u::::u   k:::::::::::k     aa::::::::::::a 
                      P::::P            u::::u    u::::u   l::::l u::::u    u::::u   k:::::::::::k    a::::aaaa::::::a 
                      P::::P            u:::::uuuu:::::u   l::::l u:::::uuuu:::::u   k::::::k:::::k  a::::a    a:::::a 
                    PP::::::PP          u:::::::::::::::uul::::::lu:::::::::::::::uuk::::::k k:::::k a::::a    a:::::a 
                    P::::::::P           u:::::::::::::::ul::::::l u:::::::::::::::uk::::::k  k:::::ka:::::aaaa::::::a 
                    P::::::::P            uu::::::::uu:::ul::::::l  uu::::::::uu:::uk::::::k   k:::::ka::::::::::aa:::a
                    PPPPPPPPPP              uuuuuuuu  uuuullllllll    uuuuuuuu  uuuukkkkkkkk    kkkkkkkaaaaaaaaaa  aaaa                                                                                                                                                                                                                               

# Change the above name by using https://patorjk.com/software/taag/#p=display&f=Flower%20Power&t= 
                                                        /\_/|
                                                  ____/ o o |
                                                /~____  =ø= /                                                                 ✺
                                              (______)__m_m)
                                __,,,__                                                               __,,,__
   ✺                    ,-""-,-"       "-,-""-,                                              ,-""-,-"       "-,-""-,
                       /,-' , .-'-.7.-'-. , '-,\                  ♥                         /,-' , .-'-.7.-'-. , '-,\\         *               ❤
                       \(    /  _     _  \    )/                                            \(    /  _     _  \    )/
                        '-,  { (👁)   (👁) } ,-'                                             '-,  { (👁)   (👁) }  ,-'
               ❤         /    >  .---.  <    \                ♥                               /    >  .---.  <    \\     
                        |/ .-'   \___/   '-. \|                ☺                              |/ .-'  \___/   '-. \|
   ❣                    {, /  ,_       _,  \ ,}                                              {, /  ,_       _,  \ ,}                          ❤
                        \ {,    \     /    ,} /                      ♥                       \ {,    \     /    ,} /
                         ',\.    '---'    ./,'                                                ',\.    '---'    ./,'
                    _.-""""""-._     _.-""""""-._                          ❤             _.-""""""-._     _.-""""""-._
                   .'            `._.`            '.                                    .'            `._.`            '.          ❤
                 _/_               ❣                \            ❣                    _/_                                \\
       ★      .'`   `\                               \                             .'`   `\                               \\
             /        |          Happy                ;                           /        |                               ;
             |        /                               |                           |       /                                |          ❤    *
             \\ ;'---'          Birthday              ;        ❤                   \\;'---'      ♥ Love Yourself ❤
              '. ;                                 _  ;                             '. ;                                 _ ;
                `-\            Banumathi              [].' `,                 ✺      `-\                                   [].' `,
   ❤               `\                           |     \\                      ☺         `\                                 \\
                     \                          \     |                     ❤             \                                |
                      `\           ♥            /`   _/                                     `\                       /`   _/              ❤
            ,-""-.    .'`\                   /`-,-'` .-""-,      *               ,-""-.    .'`\                   /`-,-'` .-""-,
           /      `\.'    `\               /`    './`      \\                   /      `\.'    `\               /`    './`       \\
          ;  .--.   \       '\           /'       /   .--.  ;                  ;  .--.   \       '\           /'       /   .--.  ;
          | (    \   |,       '\       /'        |   /    ) |                  | (    \   |,       '\       /'        |   /    ) |
           \ ;    }             ;\   /;         `   {    ; /      ❤             \ ;    }             ;\   /;         `   {    ; /
            `;\   \         _.-'  \ /  `-._         /   /;`                      `;\   \         _.-'  \ /  `-._         /   /;`
   ✺          \ \__.'   _.-'       Y       `-._    '.__//                          \ \__.'   _.-'       Y       `-._    '.__//
               '.___,.-'                       `-.,___.'        ★        ❤          '.___,.-'               ❤       `-.,___.'                ❣

                                   ❤                                                                 
                              : .              __________________   __________________               : .                            *
       ❤                     [""]          .-/|                  \ /                  |\-.          [""]                   ❤             
                   ❤         |  |          ||||                   |                   ||||          |  |                                    
                             |  |          ||||                   |       ~~*~~       ||||          |  |
                             |  |          ||||                   |   Count your life ||||          |  |               ★               
                    :       .'--`.         ||||   Thank you       |by Smiles,not tears||||         .'--`.        :
   ❤              : .:     /`.__.'\        ||||      for          |                   ||||        /`.__.'\     : .:
                 :    .   /        \       ||||    Always         |   Count your age  ||||       /        \   :    .                   *
           (    ,-'``'-. ;          ;      ||||  being there      |by Friends,not years|||      ;          ; ,-'``'-.    (
           )\   |`-..-'| |   ,--.   |      ||||    for me!        |                   ||||      |   ,--.   | |`-..-'|    )\\                    ❤
          /  )  | .   :| |_.','`.`._|      ||||                   |                   ||||      |_.','`.`._| | .   :|   /  )
   ❤     ( * (  | . :  | |--'    `--|      ||||                   |   Happy Birthday! ||||      |--'    `--| | . :  |  ( * (
          \ #/  |`-..-'| ||   | | | |      ||||____       _______ | _              ___||||      ||   | | | | |`-..-'|   \#/        ❤
        .-"#'-. \::::::/ ||)|/|)|)|\|      ||/===================\|/===================\||      ||)|/|)|)|\| \::::::/ .-"#'-.
        |"-.-"|--`::::'--|._ ~**~ _.|------`--------------------~___~-------------------''------|._ ~**~ _.|--`::::'--|"-.-"|
        |     |    )(    |  `-..-'  |                                                           |  `-..-'  |    )(    |     |
★       |     |    )(    |          |                                                           |          |    )(    |     |              ❤
        |     | ,-')('-. |          |         *                           ❤               ❤     |          | ,-')('-. |     |
        |     |(  '  `  )`-._    _.-'                                                           `-._    _.-'(  '  `  )|     |
        '-._,-' `-....-'     ````      ❣                       ★                                    ````     `-....-' '-._,-'
         
   ❤  
   

   
                                                                                           /\_/|
                                                                                      ____/ o o |
                                                                                    /~____  =ø= /
                                                                                  (______)__m_m)
 _           
| |          
| |__  _   _ 
| '_ \| | | |
| |_) | |_| |
|_.__/ \__, |
        __/ |
       |___/      
                    
                  .---.       ,-----.    ,---.  ,---.   .-''-.   ______                 ,-----.    ,---.   .--.    .-''-.     .-''.-,  
                  | ,_|     .'  .-,  '.  |   /  |   | .'_ _   \ |    _ `''.           .'  .-,  '.  |    \  |  |  .'_ _   \   / _     \ 
                ,-./  )    / ,-.|  \ _ \ |  |   |  .'/ ( ` )   '| _ | ) _  \         / ,-.|  \ _ \ |  ,  \ |  | / ( ` )   ' (`' )/`--' 
                \  '_ '`) ;  \  '_ /  | :|  | _ |  |. (_ o _)  ||( ''_'  ) |        ;  \  '_ /  | :|  |\_ \|  |. (_ o _)  |(_ o _).    
                 > (_)  ) |  _`,/ \ _/  ||  _( )_  ||  (_,_)___|| . (_) `. |        |  _`,/ \ _/  ||  _( )_\  ||  (_,_)___| (_,_). '.  
                (  .  .-' : (  '\_/ \   ;\ (_ o._) /'  \   .---.|(_    ._) '        : (  '\_/ \   ;| (_ o _)  |'  \   .---..---.  \  : 
                 `-'`-'|___\ `"/  \  ) /  \ (_,_) /  \  `-'    /|  (_.\.' /          \ `"/  \  ) / |  (_,_)\  | \  `-'    /\    `-'  | 
                  |        \'. \_/``".'    \     /    \       / |       .'            '. \_/``".'  |  |    |  |  \       /  \       /  
                  `--------`  '-----'       `---`      `'-..-'  '-----'`                '-----'    '--'    '--'   `'-..-'    `-...-'   
                                                             
                                                                                                                                         
                                                                   
________________________________________________________________________________________________________|


'''

def task1():
	for letter in cake:
		time.sleep(0.001) # You can Change the Execution Seconds by chaning (0.01)
		print(letter, end='')
	for letter in wish:
		time.sleep(0.01) # You can Change the Execution Seconds by chaning (0.01)
		print(letter, end='')

def task2():
        playsound('BTS HAPPY BIRTHDAY GREETING SONG TO ARMY (320kbps).mp3')
        playsound('Naruto Shippuden - Samidare (ksolis Trap Remix).mp3') # Change your song by changing the song Name

t1 = threading.Thread(target=task1, name='t1')
t2 = threading.Thread(target=task2, name='t2')

# starting threads
t1.start()
t2.start()

#Code By KiruthiVarma
