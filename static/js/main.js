// Parsear los datos de manera segura
let jugadoresPorEquipo = {};
try {
    const jsonData = document.getElementById('jugadores-data').textContent.trim();
    jugadoresPorEquipo = JSON.parse(jsonData);
} catch (error) {
    console.error('Error al parsear los datos:', error);
    jugadoresPorEquipo = {};
}

document.querySelectorAll('.equipo').forEach(div => {
    div.addEventListener('click', () => {
        const equipo = div.getAttribute('data-equipo');
        mostrarJugadores(equipo);
    });
});

function actualizarContadorJugadores() {
    const jugadoresSeleccionados = document.querySelectorAll('input[name="jugadores"]:checked').length;
    const contadorElement = document.getElementById('jugadores-seleccionados');
    const submitButton = document.querySelector('.enviar-btn');
    const errorMessage = document.getElementById('error-message');
    
    contadorElement.textContent = `Jugadores seleccionados: ${jugadoresSeleccionados}/4`;
    submitButton.disabled = jugadoresSeleccionados === 0;
    errorMessage.style.display = 'none';

    if (jugadoresSeleccionados > 4) {
        submitButton.disabled = true;
        errorMessage.style.display = 'block';
    }
}

function mostrarJugadores(equipo) {
    const contenedor = document.getElementById('jugadores');
    const lista = document.getElementById('lista-jugadores');
    const nombreEquipo = document.getElementById('nombre-equipo');

    lista.innerHTML = '';
    nombreEquipo.textContent = equipo;

    try {
        const jugadores = jugadoresPorEquipo[equipo] || [];
        if (jugadores.length > 0) {
            jugadores.forEach(j => {
                let nombre;
                let dorsal = '';
                if (typeof j === 'string') {
                    nombre = j;
                } else if (typeof j === 'object' && j !== null) {
                    nombre = j.Nombre || j.nombre || '';
                    dorsal = (j.Dorsal !== undefined) ? j.Dorsal : (j.dorsal !== undefined ? j.dorsal : '');
                } else {
                    return;
                }

                const li = document.createElement('li');
                li.className = 'jugador-card';

                const checkbox = document.createElement('input');
                checkbox.type = 'checkbox';
                checkbox.name = 'jugadores';
                checkbox.value = nombre;
                checkbox.id = `jugador-${String(nombre).replace(/[^a-z0-9]/gi, '-')}`;

                const label = document.createElement('label');
                label.htmlFor = checkbox.id;

                const numeroSpan = document.createElement('div');
                numeroSpan.className = 'jugador-numero';
                numeroSpan.textContent = dorsal !== '' && dorsal !== null ? String(dorsal) : '-';

                const nombreSpan = document.createElement('div');
                nombreSpan.textContent = nombre;

                label.appendChild(numeroSpan);
                label.appendChild(nombreSpan);
                li.appendChild(checkbox);
                li.appendChild(label);
                lista.appendChild(li);

                // Agregar efecto de selección
                li.addEventListener('click', function(e) {
                    if (e.target.tagName !== 'INPUT') {
                        checkbox.click();
                    }
                });

                // Agregar evento change al checkbox
                checkbox.addEventListener('change', function() {
                    const totalSeleccionados = document.querySelectorAll('input[name="jugadores"]:checked').length;
                    if (totalSeleccionados > 4 && this.checked) {
                        this.checked = false;
                    }
                    // Actualizar clase selected
                    li.classList.toggle('selected', this.checked);
                    actualizarContadorJugadores();
                });
            });
        } else {
            const li = document.createElement('li');
            li.textContent = 'No hay jugadores registrados para este equipo';
            lista.appendChild(li);
        }
    } catch (error) {
        console.error('Error al mostrar jugadores:', error);
        const li = document.createElement('li');
        li.textContent = 'Error al cargar los jugadores';
        lista.appendChild(li);
    }

    contenedor.style.display = 'block';
    contenedor.scrollIntoView({ behavior: 'smooth' });
}

function cerrarJugadores() {
    document.getElementById('jugadores').style.display = 'none';
}