// Global Data
let appData = null;
let currentWorkout = {};

// Day mapping in Spanish
const dayMapping = {
    0: 'domingo',
    1: 'lunes',
    2: 'martes',
    3: 'miércoles',
    4: 'jueves',
    5: 'viernes',
    6: 'sábado'
};

// Initialize App
async function initApp() {
    try {
        const response = await fetch('data.json');
        appData = await response.json();
        
        // Set current date
        updateCurrentDate();
        
        // Setup navigation
        setupNavigation();
        
        // Load default view (Today)
        loadTodayView();
        
        // Setup button handlers
        setupButtons();
    } catch (error) {
        console.error('Error loading data:', error);
        alert('Error al cargar los datos. Verifica que data.json existe.');
    }
}

// Update Current Date
function updateCurrentDate() {
    const now = new Date();
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    const dateString = now.toLocaleDateString('es-ES', options);
    document.getElementById('currentDate').textContent = dateString;
}

// Setup Navigation
function setupNavigation() {
    const navItems = document.querySelectorAll('.nav-item');
    
    navItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            
            // Update active nav item
            navItems.forEach(nav => nav.classList.remove('active'));
            item.classList.add('active');
            
            // Show corresponding view
            const view = item.dataset.view;
            showView(view);
        });
    });
}

// Show View
function showView(viewName) {
    // Hide all views
    document.querySelectorAll('.view').forEach(view => {
        view.classList.remove('active');
    });
    
    // Update header
    const titles = {
        'today': { title: 'Entrenamiento de Hoy', subtitle: 'Registra tus series y progreso' },
        'progress': { title: 'Progreso', subtitle: 'Visualiza tu evolución semanal' },
        'exercises': { title: 'Biblioteca de Ejercicios', subtitle: 'Todos tus ejercicios disponibles' },
        'history': { title: 'Historial', subtitle: 'Entrenamientos anteriores' }
    };
    
    const header = titles[viewName];
    document.getElementById('pageTitle').textContent = header.title;
    document.getElementById('pageSubtitle').textContent = header.subtitle;
    
    // Show selected view and load content
    switch(viewName) {
        case 'today':
            document.getElementById('todayView').classList.add('active');
            loadTodayView();
            break;
        case 'progress':
            document.getElementById('progressView').classList.add('active');
            loadProgressView();
            break;
        case 'exercises':
            document.getElementById('exercisesView').classList.add('active');
            loadExercisesView();
            break;
        case 'history':
            document.getElementById('historyView').classList.add('active');
            loadHistoryView();
            break;
    }
}

// Load Today's Workout View
function loadTodayView() {
    const today = new Date();
    const dayName = dayMapping[today.getDay()];
    
    const container = document.getElementById('workoutContainer');
    container.innerHTML = '';
    
    // Group exercises by muscle group for today
    const todayMuscleGroups = appData.muscleGroups.filter(mg => 
        mg.days.includes(dayName)
    );
    
    if (todayMuscleGroups.length === 0) {
        container.innerHTML = `
            <div style="text-align: center; padding: 48px; color: var(--color-text-secondary);">
                <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin: 0 auto 16px;">
                    <path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/>
                </svg>
                <h3 style="font-size: 18px; margin-bottom: 8px;">¡Día de descanso!</h3>
                <p>No tienes entrenamientos programados para hoy.</p>
            </div>
        `;
        return;
    }
    
    todayMuscleGroups.forEach(muscleGroup => {
        const exercises = appData.exercises.filter(ex => 
            ex.muscleGroup === muscleGroup.id
        );
        
        if (exercises.length === 0) return;
        
        const muscleGroupEl = document.createElement('div');
        muscleGroupEl.className = 'muscle-group';
        
        let exercisesHTML = '';
        exercises.forEach(exercise => {
            const sets = Array.from({ length: exercise.targetSets }, (_, i) => `
                <div class="set-row">
                    <span class="set-number">S${i + 1}</span>
                    <input type="number" class="set-input" placeholder="${exercise.targetWeight} kg" 
                           data-exercise="${exercise.id}" data-set="${i}" data-field="weight">
                    <input type="number" class="set-input" placeholder="${exercise.targetReps} reps" 
                           data-exercise="${exercise.id}" data-set="${i}" data-field="reps">
                    <input type="text" class="set-input" placeholder="Observaciones..." 
                           data-exercise="${exercise.id}" data-set="${i}" data-field="notes">
                </div>
            `).join('');
            
            exercisesHTML += `
                <div class="exercise-item">
                    <div class="exercise-header">
                        <span class="exercise-name">${exercise.name}</span>
                        <span class="exercise-target">${exercise.targetSets} × ${exercise.targetReps} @ ${exercise.targetWeight}kg</span>
                    </div>
                    <div class="sets-container">
                        ${sets}
                    </div>
                </div>
            `;
            
            // Initialize workout data structure
            if (!currentWorkout[exercise.id]) {
                currentWorkout[exercise.id] = {
                    exerciseId: exercise.id,
                    sets: Array(exercise.targetSets).fill(null).map(() => ({
                        weight: null,
                        reps: null,
                        notes: ''
                    }))
                };
            }
        });
        
        muscleGroupEl.innerHTML = `
            <div class="muscle-group-header">
                <div class="muscle-icon ${muscleGroup.id}">${muscleGroup.icon}</div>
                <h2 class="muscle-group-title">${muscleGroup.name}</h2>
            </div>
            <div class="exercise-list">
                ${exercisesHTML}
            </div>
        `;
        
        container.appendChild(muscleGroupEl);
    });
    
    // Add event listeners to inputs
    document.querySelectorAll('.set-input').forEach(input => {
        input.addEventListener('input', handleSetInput);
    });
}

// Handle Set Input
function handleSetInput(e) {
    const exerciseId = e.target.dataset.exercise;
    const setIndex = parseInt(e.target.dataset.set);
    const field = e.target.dataset.field;
    const value = e.target.value;
    
    if (!currentWorkout[exerciseId]) {
        currentWorkout[exerciseId] = { exerciseId, sets: [] };
    }
    
    if (!currentWorkout[exerciseId].sets[setIndex]) {
        currentWorkout[exerciseId].sets[setIndex] = { weight: null, reps: null, notes: '' };
    }
    
    if (field === 'weight' || field === 'reps') {
        currentWorkout[exerciseId].sets[setIndex][field] = value ? parseFloat(value) : null;
    } else {
        currentWorkout[exerciseId].sets[setIndex][field] = value;
    }
    
    // Visual feedback
    e.target.style.borderColor = value ? 'var(--color-success)' : 'var(--color-border)';
}

// Load Progress View
function loadProgressView() {
    // Calculate stats from workout history
    const weekAgo = new Date();
    weekAgo.setDate(weekAgo.getDate() - 7);
    
    const thisWeekWorkouts = appData.workoutHistory.filter(w => 
        new Date(w.date) >= weekAgo
    );
    
    const totalVolume = thisWeekWorkouts.reduce((sum, w) => sum + (w.totalVolume || 0), 0);
    const totalWorkouts = thisWeekWorkouts.length;
    const totalTime = thisWeekWorkouts.reduce((sum, w) => sum + (w.duration || 0), 0);
    
    document.getElementById('statVolume').textContent = `${totalVolume.toLocaleString()} kg`;
    document.getElementById('statWorkouts').textContent = totalWorkouts;
    document.getElementById('statTime').textContent = `${totalTime} min`;
    
    // Create chart
    createVolumeChart(thisWeekWorkouts);
}

// Create Volume Chart
function createVolumeChart(workouts) {
    const ctx = document.getElementById('volumeChart');
    
    // Destroy existing chart if any
    if (window.volumeChartInstance) {
        window.volumeChartInstance.destroy();
    }
    
    // Aggregate volume by muscle group
    const volumeByMuscle = {};
    
    workouts.forEach(workout => {
        workout.exercises.forEach(ex => {
            const exercise = appData.exercises.find(e => e.id === ex.exerciseId);
            if (!exercise) return;
            
            const muscleGroup = appData.muscleGroups.find(mg => mg.id === exercise.muscleGroup);
            if (!muscleGroup) return;
            
            const volume = ex.sets.reduce((sum, set) => 
                sum + (set.weight * set.reps), 0
            );
            
            volumeByMuscle[muscleGroup.name] = (volumeByMuscle[muscleGroup.name] || 0) + volume;
        });
    });
    
    const labels = Object.keys(volumeByMuscle);
    const data = Object.values(volumeByMuscle);
    
    window.volumeChartInstance = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Volumen (kg)',
                data: data,
                backgroundColor: [
                    'rgba(35, 131, 226, 0.7)',
                    'rgba(15, 123, 108, 0.7)',
                    'rgba(144, 101, 176, 0.7)',
                    'rgba(253, 121, 168, 0.7)',
                    'rgba(85, 239, 196, 0.7)'
                ],
                borderColor: [
                    'rgba(35, 131, 226, 1)',
                    'rgba(15, 123, 108, 1)',
                    'rgba(144, 101, 176, 1)',
                    'rgba(253, 121, 168, 1)',
                    'rgba(85, 239, 196, 1)'
                ],
                borderWidth: 2,
                borderRadius: 8
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    grid: {
                        color: 'rgba(0, 0, 0, 0.05)'
                    }
                },
                x: {
                    grid: {
                        display: false
                    }
                }
            }
        }
    });
}

// Load Exercises Library View
function loadExercisesView() {
    const container = document.getElementById('exerciseLibrary');
    container.innerHTML = '';
    
    appData.exercises.forEach(exercise => {
        const muscleGroup = appData.muscleGroups.find(mg => mg.id === exercise.muscleGroup);
        
        const card = document.createElement('div');
        card.className = 'exercise-card';
        card.innerHTML = `
            <div class="exercise-card-header">
                <span class="muscle-icon ${exercise.muscleGroup}">${muscleGroup.icon}</span>
                <h3 class="exercise-card-title">${exercise.name}</h3>
            </div>
            <div class="exercise-card-meta">
                <span class="badge">${muscleGroup.name}</span>
                <span class="badge">${exercise.targetSets} series</span>
                <span class="badge">${exercise.targetReps} reps</span>
                <span class="badge">${exercise.targetWeight} kg</span>
            </div>
            <p style="margin-top: 12px; font-size: 13px; color: var(--color-text-secondary);">${exercise.notes}</p>
        `;
        
        container.appendChild(card);
    });
}

// Load History View
function loadHistoryView() {
    const container = document.getElementById('historyContainer');
    container.innerHTML = '';
    
    if (appData.workoutHistory.length === 0) {
        container.innerHTML = `
            <div style="text-align: center; padding: 48px; color: var(--color-text-secondary);">
                <p>Aún no hay entrenamientos registrados.</p>
            </div>
        `;
        return;
    }
    
    // Sort by date (newest first)
    const sortedHistory = [...appData.workoutHistory].sort((a, b) => 
        new Date(b.date) - new Date(a.date)
    );
    
    sortedHistory.forEach(workout => {
        const date = new Date(workout.date);
        const dateStr = date.toLocaleDateString('es-ES', { 
            weekday: 'long', 
            year: 'numeric', 
            month: 'long', 
            day: 'numeric' 
        });
        
        const exerciseCount = workout.exercises.length;
        const cardioCount = workout.cardio?.length || 0;
        
        const item = document.createElement('div');
        item.className = 'history-item';
        item.innerHTML = `
            <div class="history-date">${dateStr}</div>
            <div class="history-summary">
                ${exerciseCount} ejercicio${exerciseCount !== 1 ? 's' : ''} • 
                Volumen: ${workout.totalVolume.toLocaleString()} kg • 
                Duración: ${workout.duration} min
                ${cardioCount > 0 ? ` • ${cardioCount} cardio` : ''}
            </div>
        `;
        
        container.appendChild(item);
    });
}

// Setup Button Handlers
function setupButtons() {
    document.getElementById('btnSave').addEventListener('click', saveWorkout);
    document.getElementById('btnExport').addEventListener('click', exportData);
}

// Save Workout
function saveWorkout() {
    const today = new Date().toISOString().split('T')[0];
    const dayName = dayMapping[new Date().getDay()];
    
    // Filter out empty exercises
    const exercises = Object.values(currentWorkout).filter(ex => 
        ex.sets.some(set => set.weight || set.reps)
    );
    
    if (exercises.length === 0) {
        alert('No hay datos para guardar. Completa al menos un ejercicio.');
        return;
    }
    
    // Calculate total volume
    const totalVolume = exercises.reduce((sum, ex) => {
        return sum + ex.sets.reduce((setSum, set) => 
            setSum + ((set.weight || 0) * (set.reps || 0)), 0
        );
    }, 0);
    
    const newWorkout = {
        date: today,
        day: dayName,
        exercises: exercises,
        cardio: [],
        totalVolume: totalVolume,
        duration: 0 // Could be tracked with a timer
    };
    
    // Add to history
    appData.workoutHistory.push(newWorkout);
    
    // In a real app, this would save to a backend
    console.log('Workout saved:', newWorkout);
    
    // Show confirmation
    alert(`¡Entrenamiento guardado!\n\nVolumen total: ${totalVolume.toLocaleString()} kg\nEjercicios: ${exercises.length}`);
    
    // Reset current workout
    currentWorkout = {};
    
    // Reload view
    loadTodayView();
}

// Export Data
function exportData() {
    const dataStr = JSON.stringify(appData, null, 2);
    const dataBlob = new Blob([dataStr], { type: 'application/json' });
    const url = URL.createObjectURL(dataBlob);
    
    const link = document.createElement('a');
    link.href = url;
    link.download = `training-data-${new Date().toISOString().split('T')[0]}.json`;
    link.click();
    
    URL.revokeObjectURL(url);
}

// Initialize on load
document.addEventListener('DOMContentLoaded', initApp);
