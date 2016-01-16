label cabbageInit:
    $ p = player
    $ s = secretary
    show expression Image('pic/events/cabbage/secretary.png', xalign=0.8, yalign= 0.8, yanchor = 'center') as char1 
    show expression getCharImage(player,'dialog') as char2
    p.say 'Здравствуйте, что Вы здесь делаете? - интересуетесь вы у незнакомца в вашем кабинете.'
    s 'Приятно познакомится. [p.name], если я не ошибаюсь?'
    'Мужчина наклоняется к вам и галантно целует ручку.'
    p.say 'Да, вы не ошиблись. С кем имею честь? - принимаете вы правила игры, начиная изображать из себя великосветскую львицу.'
    s 'Александр, для Вас просто Александр, - поправляет свой галстук мужчина.'
    p.say 'Просто Александр, может перейти ближе к делу?'
    s 'Ну, размумеется. В общем, я представляю компанию по выращиванию овощей и занимаюсь рекрутингом, - начинает объяснять мужчина.'
    p.say 'В школе? - выгибаете вы бровь.'
    s 'Да, в школе... У нас уродился ОГРОМНЫЙ урожай капусты, и нам необходимо её собрать. С министерством всё согласовано, дело осталось за вами.'
    'Он протягивает вам какие-то бумаги. Быстро пробежавшись по ним глазами, вы выясняете, что, подписав их, вы сможете отправлять учителей и школьников на уборку капусты хоть ежедневно. Но платить вам будут в зависимости от собранного количества.'
    p.say 'Мне необходимо отправлять их каждый день? - задаёте вы уточняющий вопрос.'
    s 'Как захотите, автобус будет ждать вас с 7 до 8. Если никто не появится, то он поедет собирать людей в другом месте, - пожимает плечами Александр.'
    'Не вижу причин отказываться от столь привлекательного предложения! - Вы подмахиваете документ и прощаетесь с мужчиной.'
    $ is_cabbage = 1
    $ move(curloc)
    
label cabbageStart:
    'Собрав всех учеников и объявив им, что сегодня вместо занятий все отправляются на заготовку овощей, вы под радостный вой загнали всех в автобус и отправились покорять капусту.'
    'В пути студенты веселились и шутили, чем подняли себе настроение. Спустя час, вы прибыли на место и тут же взяли на себя руководящую роль, отправив учеников на заготовки, а учителей на сортировку. Для себя вы приготовили занятие получше - отдохнуть, походить и посмотреть, что да как.'
    if stat_fun < 20: 
        $ setFun(50,4)
        $ setLoy(50,4)
    $ cabbage_eff = 0
    jump cabbageIn
    
label cabbageIn:
    $clrscr()
    hide tempPic
    if hour > 18:
        jump cabbageEnd
    show expression 'pic/events/cabbage/cabbage.png' at top as bg
    menu:
        'Погоды стоят жаркие, ученики работают, все при деле. Чем бы заняться самой?'
        'Погулять пару часиков' if player.getEnergy() >= 300:
            if rand(1,3) == 1 or development == 1:
                $ changetime(120)
                $ tryEvent('loc_cabbage')
            else:
                'Вы погуляли пару часиков, но ничего интересного не встретили. Зато эта прогулка положительно сказалась на вашем здоровье!'
                $ player.incHealth(10)
                $ player.incEnergy(-250)
                $ changetime(120)
            jump cabbageIn
        'Надзирать за работой' if player.getEnergy() >= 300:
            show expression getCharImage(player,'dialog') as tempPic
            'Вы 2 часа гоняли учеников в хвост и гриву, заставляя их работать. Это безусловно скажется на их эффективности положительно, но вот на лояльности к вам - отрицательно. К тому же, постоянный надзор - жутко утомительное занятие.'
            python:
                cabbage_eff += 1
                setFun(50,-1)
                setLoy(50,-1)
                changetime(120)
            jump cabbageIn
        'Отдохнуть пару часиков':
            show expression 'pic/events/cabbage/rest.png' at top as tempPic
            'Вы отдохнули пару часиков, глядя на облачка, и, кажется, даже всхрапнули минут 40. Вроде, самочувствие улучшилось, да и сил прибавилось.'
            python:
                changetime(120)
                player.incEnergy(150)
            jump cabbageIn

label cabbageEnd:
    $ clrscr()
    $ cabbage_eff += int((100 - stat_corr)/20)
    show expression 'pic/events/cabbage/farmer.jpg' at top as bg
    'К концу дня к вам подходит фермер. Владелец поля на котором работали ваши ученики.'
    if cabbage_eff >= 9:
        farmer 'Ваши ученики - великолепные работники! Никогда таких не видел! Просто загляденье, вот что значит строгий учитель и прилежание! - радостно сказал он, начиная подсчитывать Ваш дневной заработок.'
    elif cabbage_eff >= 6:
        farmer 'Ваши ученики - хорошие работники! Но могли бы постараться и  получше! - улыбаясь сказал он, подсчитывая Ваш дневной заработок.'
    elif cabbage_eff >= 3:
        farmer 'Ваши ученики - весьма посредственные работники... Хотя, учитывая то, что работа сдельная... И так сойдёт, - хмурясь сказал он, подсчитывая Ваш дневной заработок.'
    else:
        farmer 'Хуже работников я не видел. Просто не видел. Младенец сможет натаскать больше, чем ваши озабоченные остолопы, - недовольно бросил он, подсчитывая ваш дневной заработок и свой убыток.'
    python:
        cabbage_eff = max(1,cabbage_eff)
        temp = int(cabbage_eff*rand(500,600))
        school.budget += temp
    'Вы пересчитали купюры, и оказалось, что за сегодня ваши ученики заработали [temp] монет. Жаль, что все эти деньги пройдут мимо вашего кармана, прямо в школьный бюджет.'
    $ move(curloc)
    
label event_loc_cabbage_0_1:
    'Прогуливаясь, Вы наткнулись на небольшой сарайчик из которого доносились стоны и крики.'
    menu:
        'Заглянуть' if player.getCorr() > 20:
            show expression 'pic/events/cabbage/ahmed_sex.jpg' at top as tempPic
            'Аккуратно заглянув в окошко, Вы увидели там вашего физрука, беззастенчиво трахающего в задницу жену фермера. Мало того, он использовал морковку на её текущей киске, осуществляя двойное проникновение.'
            player.say 'Офигеть... - тихо прошептали вы, ощущая как теплеет в вашем животе. Рыкнув в очередной раз, Ахмед загнал весь свой член в задницу женщины и протолкнул поглубже морковку.'
            mustangovich.say 'Класс! - выдохнул он, и его член начал дёргаться внутри её попки, расширяя сфинктер уже совсем до неприличных размеров.'
            $ renpy.say('Настасья Прокофьевна', 'Мой мустанг! - закричала изменщица, кончая.')
            'Вы поспешили убраться подальше, предварительно запомнив местоположение сарайчика.'
            $ player.incLust(15)
            $ mile_qwest_2_Ahmed = 1
        'Убежать':
            'Вы решили не испытывать судьбу и, боясь быть замеченной за столь неприглядным занятием, убегаете.'
    $ hadSex(mustangovich)
    $ mustangovich.setLust(0)
    jump cabbageIn
    
label event_loc_cabbage_0_2:
    $st1 = getChar('male')
    show expression 'pic/events/cabbage/2.png' at top as tempPic
    'Идя по дороге, Вы встретили селянку о чём то разговаривающую с вашим учеником. Вас довольно сильно удивило то, что, через 5 минут разговора, она неожиданно подняла своё платье и принялась активно поглаживать свою текущую киску перед оторопевшим парнем.'
    p.say '[st1.name]! - окликнули вы парня и выразительно показали пальцем в сторону капустного поля.'
    'Вам не особо хочется, чтобы по городу начали распространятся слухи о том, что вы тут какой-то секс туризм в глубинку устроили.'
    $ player.incLust(5)
    $ st1.incLust(20)
    jump cabbageIn
    
label event_loc_cabbage_0_3:
    show expression 'pic/events/cabbage/3.jpg' at top as tempPic
    $ renpy.say('Прошка', 'Да, Рекс, да!!!.')
    'Вы с удивлением узнали в кончающей девушке дочь фермера.'
    'Её всю заливала сперма из огромного члена пса. И как, чёрт побери, в такой девочке уместился такой член? Вы поспешили смотаться, пока Вас не заметили.'
    $ player.incLust(15)
    jump cabbageIn
    
label event_loc_cabbage_20_4:
    $st1 = getChar('female')
    st1.say 'Только осторожней, пожалуйста!'
    show expression 'pic/events/cabbage/4.png' at top as tempPic
    'Заинтригованная, вы залезли в кусты и увидели там свою ученицу, уже на всё готовую с сыном фермера.'
    player.say '[st1.gname]!!! - прошипели вы из листвы, - А ну, быстро на уборку!'
    'Девушка сделала огромные глаза и быстро натянув трусы убежала. Вам не особо хочется, чтобы по городу начали распространятся слухи о том, что Вы тут какой-то секс туризм в глубинку устроили.'
    $ st1.incLust(25)
    $ player.incLust(5)
    jump cabbageIn
    
label event_loc_cabbage_0_KupruvnaSex1:
    if mile_qwest_2_stage != 12:
        $ tryEvent('loc_cabbage')
    $ k = kupruvna
    $ t = teacher_son
    'В очередной раз заметив отсутствие Валентины и её сына, вы решили посмотреть не изменилось ли чего? Не долго думая, вы направились в лес из которого доносились страстные стоны.'
    show expression 'pic/events/cabbage/6.jpg' at top as tempPic
    k.say 'Да, мой мальчик, засади его поглубже! - стонала химичка стоя на одной ноге и обхватив другой своего сына.'
    t.say 'Маам, тут это, - заметив вас, сказал [teacher_son.fname].'
    k.say 'Ой, [player.fname]! - со страхом уставилась на вас учительница, впрочем не торопясь соскакивать с члена парня.'
    player.say 'Ничего, ничего, продолжайте, - с улыбкой кивнули вы, успокаивая парочку, - Я просто проверяла, что это именно вы, а не кто-то другой.'
    'Отвернувшись от вас, Валентина продолжила заниматься любовью со своим сыном. Сначала немного неуверенно от того, что за ней наблюдают, но спустя минуту, она уже забыла о вашем присутствии.'
    'А вот сын нет. Он постоянно кидал на Вас странные взгляды. То ли от смущения, то ли от похоти, Вы не смогли разобрать. Поэтому решили ретироваться, оставив любовников за спиной.'
    python:
        hadSex(t,k)
        t.setLust(0)
        k.setLust(0)
    jump cabbageIn
    
label event_loc_cabbage_0_7:
    'Прогуливаясь по природе Вы набрели на конюшню из которой раздавались страстные женские стоны и ржание коней.'
    show expression 'pic/events/cabbage/7.jpeg' at top as tempPic
    'Заглянув в приоткрытую дверь, Вы с ужасом наблюдаете, как огромный конский член таранит влагалище женщины.'
    player.say '"Да он же её счас порвёт!", - мелькает у Вас в голове мысль, но нет, похоже что зоофилка получает чистейшее удовольствие.'
    'Её живот сильно оттопыривается в месте, куда проникает огромная головка, но вроде никаких неприятных ощущений для неё это не несёт.'
    female 'Давай, Авраам, давай же! - вопит женщина в очередном оргазме, и из её влагалища вдруг сильно бьют струи не поместившейся внутри спермы.'
    'Вы вытираете резко вспотевший от подобного зрелища лоб и возвращаетесь на поле.'
    python:
        player.incLust(10)
    jump cabbageIn