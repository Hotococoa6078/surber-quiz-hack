from pyperclip import *
def fix(a):
    e = a.replace('버수', '왘').replace('died','왘').replace(':keyboard:','왘')
    e = e.replace('숩어','쾅').replace('옼','왘').replace('dkhz', '왘').replace('obabrebrus','왘')
    e = e.replace('sad', '쾅').replace('수버핑', '쾅').replace('수버역할핑','쾅')
    e = e.replace(':died:','왘').replace('내부 헤에로 과부하!','쾅')
    e = e.replace(':surber:','쾅').replace(':sad:','쾅').replace("수버", '쾅')
    e = e.replace('내부 헤에로 과부하', '쾅').replace('surber','쾅')
    e = e.replace('하부과','왘').replace('jqnt', '왘').replace('숩버', '쾅')
    e = e.replace('rebrus', '왘').replace('헤에','쾅').replace('tnqj', '쾅')
    e = e.replace('녀귣ㄱ', '쾅').replace('숩','쾅').replace('rotinom','왘')
    e = e.replace('ㄱ듀견','왘').replace('모니터', "쾅").replace('터니모','왘')
    e = e.replace('SurberHD_', '쾅').replace('ｒｅｂｒｕＳ', '왘').replace('JnL','왘')
    e = e.replace('SurberHD', '쾅').replace(':computer:', '쾅').replace('술버','쾅')
    e = e.replace('suber','왘').replace('ㅓ붓', '왘').replace('스윽','쾅')
    e = e.replace('에헤', '왘').replace('녀ㅠㄷㄱ','왘').replace('Ｓｕｒｂｅｒ','쾅')
    e = e.replace('ㅣㅏ','왘').replace('얃ㅇ', '왘').replace('genius', '왘')
    e = e.replace('천재', '왘').replace('ㅔ', '쾅').replace('슥','쾅')
    e = e.replace('-수-', '쾅').replace('바부', '쾅').replace('긋','왘')
    e = e.replace('ㄴㅁㅇ', '쾅').replace('밥부', '쾅').replace('과부하', '쾅')
    e = e.replace('das', '왘').replace('knalb', '왘').replace('버스', '왘')


    e = e.replace(' ', '').replace(":", "")
    return(e)
while True:
    a = input(' ')
    print(fix(a))
    copy(fix(a))
    
