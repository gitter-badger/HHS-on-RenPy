init python:
    lastNotebookScreen = 'studList'
label notebook:
    show expression "pic/bg.png"
    show screen notebook
    call screen personalInfo

screen notebook:
    fixed xpos 0.01 ypos 0.01:
        hbox :
            textbutton 'Назад' action [Show('stats_screen'), Hide('studList'), Hide('teacherList'), Hide('personalInfo'), Hide('charInfoLeft'), Function(move, curloc)]
            textbutton 'Вы' action [Hide ('charInfoLeft'), Show('personalInfo')]
            textbutton 'Список учеников' action Show('studList')
            textbutton 'Список учителей' action Show('teacherList')


screen studList:
    tag notebookList
    fixed xpos 0.01 ypos 0.1:
        $ xalig = 0.17
        $ yalig = 0.01
        for x in studs:
            imagebutton idle im.FactorScale(x.picto,0.5) hover im.FactorScale(x.picto,0.6) xalign xalig yalign yalig action NullAction() hovered [SetVariable('showHover',x),Show('charInfoLeft')]
            $ xalig += 0.09
            if xalig >= 0.99:
                $ yalig += 0.15
                $ xalig = 0.17

screen teacherList:
    tag notebookList
    fixed xpos 0.01 ypos 0.1:
        $ xalig = 0.17
        $ yalig = 0.01
        for x in teachers:
            imagebutton idle im.FactorScale(x.picto,0.5) hover im.FactorScale(x.picto,0.6) xalign xalig yalign yalig action NullAction() hovered [SetVariable('showHover',x),Show('charInfoLeft')]
            $ xalig += 0.15
            if xalig >= 0.99:
                $ yalig += 0.15
                $ xalig = 0.17

screen charInfoLeft:
    vbox xpos 0.01 ypos 0.1:
        if showHover.age > 0:
            add showHover.picto
            null height 10
            $ playerName = player.fullName()
            text '[showHover.name]' style style.my_text
            $ temp = showHover.age
            text 'Возраст [temp]' style style.my_text
            $ bsize = showHover.body.parts['грудь'].size
            if bsize > 0:
                $ temp = round(bsize, 1)
                text 'Размер груди [temp]' style style.my_text
            else:
                text '' style style.my_text

            $ temp = round(showHover.body.height,1)
            text 'Рост [temp]' style style.my_text
            $ temp = round(showHover.stats.education,1)
            text 'Образование [temp]' style style.my_text
            $ temp = round(showHover.stats.fun,1)
            text 'Счастье [temp]' style style.my_text
            $ temp = round(showHover.stats.loyalty,1)
            text 'Лояльность [temp]' style style.my_text
            $ temp = round(showHover.stats.corr,1)
            text 'Развратность [temp]' style style.my_text
            $ temp = round(showHover.stats.beauty,1)
            text 'Красота [temp]' style style.my_text

screen personalInfo:
    tag notebookList
    fixed xpos 0.01 ypos 0.1:
        vbox:
            python:
                name = player.fullName()
                age = str(player.age)
                sex = player.body.sex()
                beauty = player.getBeauty()
                loyalty = player.getLoy()
                edu = player.getEdu()
                lust = player.getLust()
                corr = player.getCorr()
                fun = player.getFun()
                health = player.getHealth()
                height = round(showHover.body.height,1)
                money = player.money
                
                bsize = round(player.body.parts['грудь'].size, 1)
                vsize = round(player.body.parts['вагина'].size)
                asize = round(player.body.parts['анус'].size)
                
            add im.FactorScale(player.picto,.5)
            null height 10
            text '[name]' style style.my_text
            text 'Размер груди [bsize]' style style.my_text
            text 'Рост [height]' style style.my_text
            text 'Образование [edu]' style style.my_text
            text 'Счастье [fun]' style style.my_text
            text 'Развратность [corr]' style style.my_text
            text 'Красота [beauty]' style style.my_text
            text ''
            text 'Размер вагины [vsize]' style style.my_text
            text 'Размер ануса [asize]' style style.my_text
            text ''
            text 'Денег [money]' style style.my_text
            
    fixed xpos 0.2 ypos 0.1 :
        vbox xmaximum 800:
            text textgen(player) style style.my_text
