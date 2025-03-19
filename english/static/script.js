let currentTheme;
let words = {};
let currentWordIndex = 0;
let spellingWords = [];
let learningWords = [];

//Загрузить тему
async function loadTheme(theme) {
    currentTheme = theme;
    const response = await fetch(`/words/${theme}`);
    words = await response.json();
    updateDictionaryList();
    document.getElementById('themes').classList.add('hidden');
    document.getElementById('modes').classList.remove('hidden');
    document.getElementById('navigation').classList.remove('hidden');
    document.getElementById('title').textContent = 'Выберите режим';
}




// Функция для показа словаря
function showDictionary() {
    document.getElementById('modes').classList.add('hidden');
    document.getElementById('dictionary-mode').classList.remove('hidden');
    updateDictionaryList();
}

// Обновление списка слов
function updateDictionaryList() {
    const list = document.getElementById('dictionary-list');
    list.innerHTML = '';
    
    for(const [word, translation] of Object.entries(words)) {
        const div = document.createElement('div');
        div.className = 'word-pair';
        div.innerHTML = `
            <span>${word}</span>
            <span>${translation}</span>
        `;
        list.appendChild(div);
    }
}

// Показать режим карточек
function showCards() {
    document.getElementById('modes').classList.add('hidden');
    document.getElementById('cards-mode').classList.remove('hidden');
    currentWordIndex = 0;
    showCard();
}

// Показать текущую карточку
function showCard() {
    const word = Object.keys(words)[currentWordIndex];
    const translation = words[word];
    const cardFront = document.querySelector('.card-front');
    const cardBack = document.querySelector('.card-back');
    cardFront.textContent = word;
    cardBack.textContent = translation;
}

// Переключение на следующую карточку
document.getElementById('next-btn').addEventListener('click', () => {
    currentWordIndex = (currentWordIndex + 1) % Object.keys(words).length;
    showCard();
});

// Переключение на предыдущую карточку
document.getElementById('prev-btn').addEventListener('click', () => {
    currentWordIndex = (currentWordIndex - 1 + Object.keys(words).length) % Object.keys(words).length;
    showCard();
});

// Переворот карточки
document.querySelector('.card').addEventListener('click', () => {
    document.querySelector('.card').classList.toggle('flipped');
});

// Показать режим правописания
function showSpelling() {
    document.getElementById('modes').classList.add('hidden');
    document.getElementById('spelling-mode').classList.remove('hidden');
    spellingWords = Object.entries(words);
    shuffleArray(spellingWords);
    currentWordIndex = 0;
    showSpellingWord();
}

// Показать слово для правописания
function showSpellingWord() {
    if (currentWordIndex < spellingWords.length) {
        const [word, translation] = spellingWords[currentWordIndex];
        document.getElementById('spelling-word').textContent = translation;
        document.getElementById('spelling-input').value = '';
        document.getElementById('spelling-result').textContent = '';
    } else {
        document.getElementById('spelling-result').textContent = 'Вы прошли все слова!';
    }
}

// Проверить правописание
function checkSpelling() {
    const [word, translation] = spellingWords[currentWordIndex];
    const answer = document.getElementById('spelling-input').value.trim().toLowerCase();
    const resultElement = document.getElementById('spelling-result');

    if (!answer) {
        resultElement.textContent = 'Введите слово!';
        resultElement.style.color = 'orange';
        return;
    }

    if (answer === word.toLowerCase()) {
        resultElement.textContent = 'Правильно!';
        resultElement.style.color = 'green';
    } else {
        resultElement.textContent = `Неправильно! Правильный ответ: ${word}`;
        resultElement.style.color = 'red';
        spellingWords.push([word, translation]);
    }

    currentWordIndex++;
    if (currentWordIndex < spellingWords.length) {
        showSpellingWord();
    } else {
        resultElement.textContent += ' Вы прошли все слова!';
    }
}

// Показать режим заучивания
function showLearning() {
    document.getElementById('modes').classList.add('hidden');
    document.getElementById('learning-mode').classList.remove('hidden');
    learningWords = Object.entries(words);
    shuffleArray(learningWords);
    currentWordIndex = 0;
    showLearningWord();
}

// Показать слово для заучивания
function showLearningWord() {
    if (currentWordIndex < learningWords.length) {
        const [word, translation] = learningWords[currentWordIndex];
        document.getElementById('learning-word').textContent = translation;

        // Генерация вариантов ответа
        const options = [word];
        while (options.length < 4) {
            const randomWord = Object.keys(words)[Math.floor(Math.random() * Object.keys(words).length)];
            if (!options.includes(randomWord)) {
                options.push(randomWord);
            }
        }
        shuffleArray(options);

        const optionButtons = document.querySelectorAll('.option-btn');
        optionButtons.forEach((button, index) => {
            button.textContent = options[index];
            button.onclick = () => checkLearningAnswer(options[index], word);
        });
    } else {
        document.getElementById('learning-result').textContent = 'Вы прошли все слова!';
    }
}

// Проверить ответ в режиме заучивания
function checkLearningAnswer(selectedWord, correctWord) {
    const resultElement = document.getElementById('learning-result');
    if (selectedWord === correctWord) {
        resultElement.textContent = 'Правильно!';
        resultElement.style.color = 'green';
        currentWordIndex++;
    } else {
        resultElement.textContent = `Неправильно! Правильный ответ: ${correctWord}`;
        resultElement.style.color = 'red';
    }
    showLearningWord();
}

// Перемешать массив
function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

// Вернуться к темам
function backToThemes() {
    document.getElementById('dictionary-mode').classList.add('hidden');
    document.getElementById('modes').classList.add('hidden');
    document.getElementById('cards-mode').classList.add('hidden');
    document.getElementById('spelling-mode').classList.add('hidden');
    document.getElementById('learning-mode').classList.add('hidden');
    document.getElementById('themes').classList.remove('hidden');
    document.getElementById('navigation').classList.add('hidden');
    document.getElementById('title').textContent = 'Выберите тему';
}

// Сменить режим
function changeMode() {
    document.getElementById('cards-mode').classList.add('hidden');
    document.getElementById('spelling-mode').classList.add('hidden');
    document.getElementById('learning-mode').classList.add('hidden');
    document.getElementById('modes').classList.remove('hidden');
}

// Общая функция для скрытия всех режимов
function hideAllModes() {
    const modes = [
        'cards-mode', 
        'spelling-mode', 
        'learning-mode', 
        'dictionary-mode'
    ];
    
    modes.forEach(mode => {
        document.getElementById(mode).classList.add('hidden');
    });
}

// Переписываем функции показа режимов
function showCards() {
    hideAllModes();
    document.getElementById('cards-mode').classList.remove('hidden');
    currentWordIndex = 0;
    showCard();
}

function showSpelling() {
    hideAllModes();
    document.getElementById('spelling-mode').classList.remove('hidden');
    // ... остальной код
}

function showLearning() {
    hideAllModes();
    document.getElementById('learning-mode').classList.remove('hidden');
    // ... остальной код
}

function showDictionary() {
    hideAllModes();
    document.getElementById('dictionary-mode').classList.remove('hidden');
    updateDictionaryList();
}

// Обновляем функцию возврата к темам
function backToThemes() {
    hideAllModes();
    document.getElementById('themes').classList.remove('hidden');
    document.getElementById('navigation').classList.add('hidden');
    document.getElementById('title').textContent = 'Выберите тему';
}