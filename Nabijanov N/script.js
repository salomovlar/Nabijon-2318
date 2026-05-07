let books = [];
let totalBooks = 0;
let soldBooks = 0;
let availableBooks = 0;

async function loadBooks() {
    try {
        const response = await fetch('data.json');
        books = await response.json();
        totalBooks = books.length;
        soldBooks = books.filter(b => b.sold).length;
        availableBooks = totalBooks - soldBooks;
        return true;
    } catch (error) {
        console.error('Kitoblarni yuklashda xatolik:', error);
        return false;
    }
}

function createSnakes() {
    const container = document.getElementById('snakesContainer');
    const snake = document.createElement('div');
    snake.className = 'snake';
    snake.style.top = '200px';
    snake.style.animationDelay = '0s';
    snake.style.animationDuration = '20s';

    let snakeHTML = '<div class="snake-body">';
    for (let i = 0; i < 10; i++) {
        snakeHTML += '<div class="snake-segment"></div>';
    }
    snakeHTML += '<div class="snake-tongue"></div></div>';
    snake.innerHTML = snakeHTML;

    container.appendChild(snake);
}

function typeWriter(element, text, speed = 100, callback) {
    let i = 0;
    element.textContent = '';
    function type() {
        if (i < text.length) {
            element.textContent += text.charAt(i);
            i++;
            setTimeout(type, speed);
        } else if (callback) {
            callback();
        }
    }
    type();
}

function animateCounter(element, target, duration = 2000) {
    let start = 0;
    const increment = target / (duration / 16);
    function update() {
        start += increment;
        if (start >= target) {
            element.textContent = target;
        } else {
            element.textContent = Math.floor(start);
            requestAnimationFrame(update);
        }
    }
    update();
}

function displayBooks() {
    const grid = document.getElementById('booksGrid');
    books.forEach(book => {
        const card = document.createElement('div');
        card.className = 'book-card';
        card.innerHTML = `
            <h4>${book.name}</h4>
            <p>Muallif: ${book.author}</p>
            <p>Narx: ${book.price.toLocaleString()} so'm</p>
            <p>Holati: ${book.sold ? '<span style="color:red">Sotilgan</span>' : '<span style="color:#00ff00">Mavjud</span>'}</p>
        `;
        grid.appendChild(card);
    });
}

window.onload = async function() {
    createSnakes();

    const loaded = await loadBooks();
    if (!loaded) return;

    typeWriter(document.getElementById('mainTitle'), 'Nabijanov Kitob Do\'koni', 150, () => {
        typeWriter(document.getElementById('subtitle'), 'Sifatli va zamonaviy kitoblar shu yerda!', 80, () => {
            typeWriter(document.getElementById('statsTitle'), '📊 Statistika', 100, () => {
                animateCounter(document.getElementById('totalBooks'), totalBooks);
                animateCounter(document.getElementById('availableBooks'), availableBooks);
                animateCounter(document.getElementById('soldBooks'), soldBooks);

                setTimeout(() => {
                    typeWriter(document.getElementById('booksTitle'), '📚 Mavjud Kitoblar', 100, () => {
                        displayBooks();
                        typeWriter(document.getElementById('footerText'), '© 2026 Nabijanov. Barcha huquqlar himoyalangan.', 50);
                    });
                }, 1000);
            });
        });
    });
};
