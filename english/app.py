from flask import Flask, jsonify, request, render_template

# Создаем приложение Flask
app = Flask(__name__)

# Данные: словарь с темами и словами
data = {
    "Фразовые глаголы": {
        "check in": "регестрироваться",
        "come on": "появляться/давай",
        "get up": "вставать",
        "go away": "уехать",
        "go back": "возвращаться",
        "go out": "выходить",
        "sit down": "сесть",
        "stand up": "встать",
        "wake up": "просыпаться",
        "call back": "перезвонить",
        "drop off": "подвозить",
        "give back": "возвращать,отдать",
        "pay back": "вернуть деньги",
        "pick up": "подобрать/подвозить",
        "put away": "положить",
        "send back": "отослать",
        "take back": "вернуть/сдать",
        "take out": "вынести",
        "try on": "примерять",
        "turn off": "выключить",
        "turn on": "включить",
        "write down": "записывать",
        "go on ": "продолжить",
        "get on": "сесть/залезть",
        "get on with": "ладить с кем то",
        "look for": "искать",
        "look round": "осмотреться",
        "run out of": "исчерпать"
    },
    "Готовка": {
        "baked": "запеченый",
        "boild": "вареный",
        "fried": "жаренный на плите",
        "griled": "гриль",
        "roast": "жаренный в духовке",
        "steamed": "на пару",
        "cut down on": "сократить употребление",
        "cut out": "исключить"
    },
    "Финансы": {
        "inherit": "наследовать",
        "save money": "откладывать",
        "to lend = give": "одалживать / давать в долг",
        "borrow": "занимать деньги  у кого то",
        "waste": "тратиться впустую",
        "can affrod": "мочь позволить себе",
        "charges": "расходы",
        "owe": "быть должным",
        "invest": "инвестировать",
        "earn": "зарабатывать",
        "is worth": "стоимость, стоить, ценность",
        "to rise money": "собирать деньги",
        "rise money for chairty": "собирать деньги на балотворительность",
        "bill ": "чек",
        "tax": "налог",
        "loan": "кредит",
        "budget": "бюджет",
        "mortgage": "ипотека",
        "contactless payment": "безконтактная оплата",
        "insurance": "страхование"
    },
    "Этикет": {
        "advise on": "давать советы",
        "etiquette": "этикет",
        "enquiries": "запросы",
        "acceptable": "примелемый",
        "to trouble": "беспокоить (в голове) напрягать ",
        "appropriate": "подходящий, уместный ",
        "impersonal": "обезличенный ",
        "according to": "согласно чему то",
        "avoid": "избегать",
        "inconsiderate": "нелюбезный",
        "recline your seat": "наклонить сидение ",
        "give up your seat to": "предложить свое место, уступить",
        "decline the offer": "отклонить предложение",
        "be served": "быть обслуженным",
        "unless": "если не",
        "diners": "обедающие",
        "permition": "разрешение"
    },
    "Человеческие качества": {
        "reliable": "надежный, верный",
        "rebellious": "мятежный, бунтарский",
        "generous": "щедрый, великодушный",
        "mean": "жадный",
        "insecure": "неуверенный",
        "selfish": "эгоистичный, себялюбивый",
        "competitive": "конкурентоспособный",
        "spoilt": "избалованный, испорченный",
        "aggressive": "агрессивный",
        "charming": "очаровательный",
        "sensible": "благоразумный, здравомыслящий; здравый",
        "sociable": "общительный, компанейский",
        "anxious": "тревожный, беспокойный",
        "moody": "угрюмый, унылый",
        "independent": "независимый, самостоятельный",
        "bossy": "властный, любящий командовать",
        "affectionate": "любящий, нежный",
        "sensitive": "чувствительный, впечатлительный",
        "ambitious": "амбициозный, целеустремленный",
        "stubborn": "упрямый; непреклонный",
        "clever": "умный, сообразительный",
        "stupid": "глупый, тупой",
        "self-confident": "самоуверенный, уверенный в себе",
        "lazy": "ленивый",
        "hard-working": "работящий, трудолюбивый, усердный",
        "quiet": "тихий, спокойный",
        "talkative": "разговорчивый, болтливый",
        "shy": "застенчивый, стеснительный",
        "outgoing": "дружелюбный, коммуникабельный, общительный",
        "unambitious": "неамбициозный",
        "unfriendly": "недружелюбный",
        "dishonest": "нечестный",
        "unimaginative": "лишенный воображения",
        "unkind": "недобрый, злой",
        "disorganized": "неорганизованный",
        "unreliable": "ненадежный",
        "unselfish": "бескорыстный, неэгоистичный",
        "unsociable": "необщительный, замкнутый",
        "untidy": "неопрятный, неаккуратный",
        "immature": "незрелый, юный",
        "impatient": "нетерпеливый",
        "irresponsible": "безответственный",
        "insensitive": "бесчувственный, равнодушный",
        "sympathetic": "сочувствующий",
        "honest": "честный, искренний",
        "imaginative": "с хорошим воображением",
        "mature": "зрелый, взрослый",
        "patient": "терпеливый",
        "extroverted": "экстраверт",
        "funny": "забавный, смешной",
        "serious": "серьезный",
        "responsible": "ответственный, надёжный, достойный доверия"
    },
    "Тема про благотворительность": {
        "charity": "благотворительность; благотворительная организация",
        "sunflower": "подсолнух",
        "lorry": "грузовик",
        "orphan": "сирота",
        "head teacher": "завуч",
        "set up": "устраивать, организовывать, создавать",
        "shelter": "приют, убежище",
        "malnutrition": "недоедание",
        "seeds": "семена",
        "AIDS": "СПИД",
        "palm": "пальма",
        "water tank": "бак, резервуар для воды",
        "literacy": "грамотность",
        "kayak": "байдарка",
        "disadvantaged people": "малоимущие люди",
        "weird": "странный",
        "supplies": "запасы",
        "scenery": "пейзаж, вид",
        "manage to": "удаваться, справиться",
        "morale": "боевой дух",
        "put up camp": "разбить лагерь",
        "admit": "признавать",
        "end up doing sth": "сделать что-то в конечном итоге",
        "frightened of": "испуганный чем-то",
        "trek": "пересекать, идти пешком",
        "sledge": "сани",
        "set off": "отправляться (в путь)",
        "exhausted": "истощенный, изнуренный",
        "freezing": "очень холодный, морозный, ледяной",
        "awful": "ужасный, отвратительный",
        "filthy": "очень грязный",
        "furious": "взбешенный, разъяренный",
        "tiny": "очень маленький, крошечный",
        "terrified": "в ужасе",
        "fascinating": "обворожительный, очаровательный, пленительный",
        "starving": "ужасно голодный",
        "huge, enormous": "огромный, громадный",
        "boiling": "очень жаркий (обычно о погоде)",
        "delighted": "восхищенный, радостный",
        "hilarious": "очень смешной, уморительный",
        "positive": "уверенный, позитивный",
        "delicious": "очень вкусный",
        "amazed": "изумлённый, поражённый",
        "stress reliever": "средство для снятия стресса",
        "sponge cake": "бисквитный торт"
    },
    "Разное из творчества": {
        "Poetry": "поэзия ",
        "inspire": "вдохновлять",
        "lyrics": "текст песни",
        "incredible": "невероятный",
        "roud": "грубый",
        "prison": "тюрьма",
        "obviously": "очевидно",
        "character": "персонаж",
        "coincidence": "стечение обстоятельств  / совпадение ",
        "to be honest": "честно говоря ",
        "bully": "издеваться ",
        "confidence": "уверенный",
        "arrogant": "высокомерный",
        "jealous": "ревнивый"
    },
    "Еще несколько фразовых": {
        "Be over": "Закончиться",
        "goes off": "срабатывать",
        "set off": "отправляться ",
        "give up": "прекратить",
        "throw away": "выбрасывать",
        "Turn up / down": "прибавить / убавить",
        "look up": "искать (в книге, словаре)",
        "fill in": "заполнить",
        "find out": "выяснить",
        "put on": "надеть",
        "take off": "снять",
        "looking after": "присматривать",
        "looking forward": "ждать с нетерпением"
    },
    "Разное из темы про органы": {
        "it suit us": "нам это подходит",
        "disruting": "нарушение / ломать",
        "vice cersa": "наоборот",
        "recent study": "недавнее исследовани",
        "to skip": "пропускать",
        "likely to be at ..": "вероятно будет в ...",
        "risk of heart disease": "риск болезни сердца",
        "alert": "бодрый",
        "carried out": "выполненный",
        "digest": "переваривать",
        "stomach": "желудок",
        "produce": "производить",
        "acid": "кислота",
        "meal": "прием пищи",
        "nutritionist": "диетолог",
        "cause diabetes": "вызывать диабет",
        "liver": "печень",
        "effecient": "эффективный ",
        "muscles": "мускулы",
        "capacity": "вместимость ",
        "lung": "легкие ",
        "endurance": "выносливость"
    },
    "Телефонные разговоры": {
    "to dail number": "набирать номер",
    "to text sb": "отправлять сообщение",
    "to massage ": "отправлять сообщение, смс и тд",
    "to hang up ": "повесить трубку",
    "to choose a ringtone": "выбирать ринготон",
    "to call back": "перезвонить",
    "to leave a massage on sb's vicemail": "оставить голосовое сообщение",
    "the line is engaged": "линия занята",
    "to swipe through": "листать фото",
    "to go off": "сработать",
    "to put sb on hold": "поставить на удержание",
    "be cut off": "связь оборволась"
    },
    "Семейство": {
        "immediate family": "близкие родственники",
        "extended family": "дальние родственники",
        "sibling": "брат или сестра",
        "stepmother": "мачеха",
        "spouse": "супруг, супруга",
        "in-laws": "родня со стороны мужа или жены",
        "nuclear family": "семья включающая только родителей с детьми",
        "adopted child": "приемный (усыновленный) ребенок",
        "half-sister": "сводная сестра",
        "an only child": "единственный ребенок в семье",
        "row": "ссора, скандал, спор",
        "refuse": "отказываться",
        "birth rate": "уровень рождаемости",
        "lack": "не хватать, недоставать",
        "let out": "выпускать, освобождать",
        "family get-together": "семейная встреча, сбор, посиделки",
        "couple": "пара",
        "argue about": "спорить о",
        "recent survey": "недавний опрос"
    },
    "Слова с предлогами": {
        "belong to": "принадлежать кому-то",
        "remind of": "напоминать о",
        "be fond of": "любить, увлекаться",
        "be keen on": "увлекаться",
        "be pleased with": "быть довольным",
        "be rude to": "быть грубым",
        "be scared of sb/sth": "бояться чего-то",
        "be afraid of": "бояться чего-то",
        "be different from": "отличающийся от",
        "be excited about": "быть взволнованным из-за",
        "be fed up with": "быть сытым по горло",
        "be famous for": "быть знаменитым чем-либо",
        "be kind to": "быть добрым к",
        "be proud of": "гордиться",
        "be tired of": "быть уставшим от",
        "apologize to sb for sth": "извиняться перед кем-то за что-то",
        "arrive in": "прибывать (город, страна)",
        "arrive at": "прибывать (место)",
        "argue with sb about sth": "спорить с кем-то о чем-то",
        "ask for": "просить что-то",
        "believe in": "верить во что-то",
        "choose between": "выбирать между",
        "depend on": "зависеть от",
        "dream about": "мечтать о",
        "laugh at": "смеяться над",
        "look forward to": "ждать с нетерпением",
        "pay for": "платить за",
        "spend on": "тратить на",
        "be angry with sb about sth": "злиться на кого-то из-за чего-то",
        "be good/bad at": "(не) преуспевать в чем-то",
        "be good for": "быть полезным для",
        "be close to": "быть близким к",
        "be interested in": "интересоваться чем-то",
        "be married to": "быть замужем за",
        "be worried about": "беспокоиться о",
        "talk to sb about sth": "говорить с кем-то о чем-то",
        "agree with sb about sth": "соглашаться с кем-то о чем-то"
    },
    "Спортивное": {
        "coach": "тренер, инструктор",
        "referee, umpire": "судья",
        "spectator": "зритель",
        "a sports hall": "спортивный зал",
        "a stadium": "стадион",
        "tennis /basketball court": "площадка для игры в теннис, баскетбол",
        "football/rugby/hockey pitch": "поле для игры в футбол, регби, хоккей",
        "formula 1 circuit": "трасса Формулы 1",
        "golf course": "поле для гольфа",
        "ski slope": "лыжный склон",
        "swimming/diving pool": "бассейн для плавания, дайвинга",
        "athletics track": "беговая дорожка",
        "win/lose": "побеждать - проигрывать",
        "draw": "заканчивать игру вничью",
        "beat": "победить кого-то",
        "score": "забить гол",
        "warm up": "разминаться",
        "work out": "тренироваться",
        "knock out": "выбивать, оглушить",
        "kick a ball": "пинать мяч",
        "bounce a ball": "отбивать мяч от земли",
        "throw a ball": "бросить мяч",
        "get fit": "прийти в форму",
        "get injured": "получить травму"
    },
    "Части тела": {
        "arms": "руки ",
        "back": "спина",
        "chin": "подбородок",
        "ears": "уши",
        "eyes": "глаза",
        "face": "лицо",
        "feet": "",
        "fingers": "пальцы",
        "hands": "",
        "head": "голова",
        "knees": "колени",
        "legs": "ноги",
        "lips": "губы",
        "mouth": "рот",
        "neck": "шея",
        "nose": "нос",
        "shoulders": "плечи",
        "stomach": "желудок",
        "teeth": "зубы",
        "thumb": "большой палец",
        "toes": "пальцы ног",
        "tongue": "язык",
        "ankles ": "щиколотки ",
        "elbows": "локти",
        "hips": "бедра",
        "thighs": "жопа",
        "lower back": "жопа",
        "bottom": "жопа",
        "waist": "талия",
        "chest": "грудь",
        "breast": "грудь",
        "forehead": "лоб",
        "wrist": "запастье ",
        "belly": "живот ",
        "belly bottom": "пупок"
    }

}

# Главная страница
@app.route('/')
def index():
    return render_template('index.html', themes=data.keys())

# Получить слова по теме
@app.route('/words/<theme>')
def get_words(theme):
    if theme in data:
        return jsonify(data[theme])
    return jsonify({"error": "Theme not found"}), 404

# Проверка правописания
@app.route('/check_spelling', methods=['POST'])
def check_spelling():
    word = request.json.get('word')
    answer = request.json.get('answer')
    theme = request.json.get('theme')
    
    if theme in data and word in data[theme]:
        correct_translation = data[theme][word]
        return jsonify({"correct": answer.lower() == correct_translation.lower()})
    return jsonify({"error": "Word or theme not found"}), 404

# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)