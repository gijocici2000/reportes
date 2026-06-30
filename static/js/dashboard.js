// ===============================
// VARIABLES
// ===============================

let currentShift = 'shift1';

// ===============================
// SELECT TURN
// ===============================

function selectTurno(shift, element = null) {

    currentShift = shift;

    // guardar en sessionStorage (IMPORTANTE)
    sessionStorage.setItem('currentShift', shift);

    document.querySelectorAll('.turno-btn')
        .forEach(btn => btn.classList.remove('active'));

    if (element) {
        element.classList.add('active');
    }

    showHistoryByShift();
}

// ===============================
// MOSTRAR HISTORIAL POR TURNO
// ===============================

function showHistoryByShift() {

    const cards = document.querySelectorAll('.report-card');
    const container = document.getElementById('reportsContainer');

    if (!container) return;

    let visibleCount = 0;

    cards.forEach(card => {

        const shift = card.dataset.shift;

        if (shift === currentShift) {
            card.classList.remove('hidden');
            visibleCount++;
        } else {
            card.classList.add('hidden');
        }
    });

    toggleEmptyState(container, visibleCount);
}

// ===============================
// EMPTY STATE
// ===============================

function toggleEmptyState(container, count) {

    let empty = container.querySelector('.empty-state');

    if (count === 0) {

        if (!empty) {

            empty = document.createElement('div');
            empty.className = 'empty-state';

            empty.innerHTML = `
                <div class="empty-icon">📋</div>
                <h3>Sin historial</h3>
                <p>No hay reportes en este turno.</p>
            `;

            container.appendChild(empty);
        }

    } else {

        if (empty) {
            empty.remove();
        }
    }
}

// ===============================
// INIT
// ===============================

document.addEventListener('DOMContentLoaded', () => {

    // recuperar turno guardado
    const savedShift = sessionStorage.getItem('currentShift');

    if (savedShift) {
        currentShift = savedShift;
    }

    showHistoryByShift();
});



// ===============================
// count box
// ===============================



const cajas = document.getElementById('id_box');
const incremento = document.getElementById('id_incremento');

incremento.addEventListener('change', function() {
    cajas.step = this.value;
});