<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Graphique des Capteurs</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <h1>Graphique des Capteurs</h1>
    <canvas id="sensorChart"></canvas>
    <script>
        var ctx = document.getElementById('sensorChart').getContext('2d');
        var sensorChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: [], // Les horodatages des mesures seront placés ici
                datasets: [{
                    label: 'DEMO1', // Nom du premier capteur
                    borderColor: 'red',
                    data: [] // Les données de température ou d'humidité du premier capteur seront placées ici
                }, {
                    label: 'DEMO2', // Nom du deuxième capteur
                    borderColor: 'blue',
                    data: [] // Les données de température ou d'humidité du deuxième capteur seront placées ici
                }, {
                    label: 'DEMO3', // Nom du troisième capteur
                    borderColor: 'green',
                    data: [] // Les données de température ou d'humidité du troisième capteur seront placées ici
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });

        // Fonction pour mettre à jour le graphique avec les données récupérées
        function updateChart(data_demo1, data_demo2, data_demo3) {
            var timestamps = []; // Liste pour stocker les horodatages des mesures
            var temps_demo1 = []; // Liste pour stocker les données de température du capteur DEMO1
            var humids_demo1 = []; // Liste pour stocker les données d'humidité du capteur DEMO1
            var temps_demo2 = []; // Liste pour stocker les données de température du capteur DEMO2
            var humids_demo2 = []; // Liste pour stocker les données d'humidité du capteur DEMO2
            var temps_demo3 = []; // Liste pour stocker les données de température du capteur DEMO3
            var humids_demo3 = []; // Liste pour stocker les données d'humidité du capteur DEMO3

            // Parcourir les données récupérées et les ajouter aux listes appropriées
            data_demo1.forEach(function(entry) {
                timestamps.push(entry.timestamp);
                temps_demo1.push(entry.temperature);
                humids_demo1.push(entry.humidity);
            });
            data_demo2.forEach(function(entry) {
                temps_demo2.push(entry.temperature);
                humids_demo2.push(entry.humidity);
            });
            data_demo3.forEach(function(entry) {
                temps_demo3.push(entry.temperature);
                humids_demo3.push(entry.humidity);
            });

            // Mettre à jour les données du graphique avec les nouvelles valeurs
            sensorChart.data.labels = timestamps; // Mettre à jour les horodatages
            sensorChart.data.datasets[0].data = temps_demo1; // Mettre à jour les données de température du capteur DEMO1
            sensorChart.data.datasets[0].label = 'DEMO1'; // Mettre à jour le label du capteur DEMO1
            sensorChart.data.datasets[1].data = temps_demo2; // Mettre à jour les données de température du capteur DEMO2
            sensorChart.data.datasets[1].label = 'DEMO2'; // Mettre à jour le label du capteur DEMO2
            sensorChart.data.datasets[2].data = temps_demo3; // Mettre à jour les données de température du capteur DEMO3
            sensorChart.data.datasets[2].label = 'DEMO3'; // Mettre à jour le label du capteur DEMO3

            // Actualiser le graphique
            sensorChart.update();
        }

        // Cette fonction est appelée lors du chargement initial de la page pour afficher les données actuelles des capteurs
        function loadInitialData() {
            fetch('/').then(function(response) {
                return response.json();
            }).then(function(data) {
                updateChart(data.data_demo1, data.data_demo2, data.data_demo3);
            }).catch(function(error) {
                console.error('Error loading initial data:', error);
            });
        }

        // Charger les données initiales lors du chargement de la page
        loadInitialData();
    </script>
</body>
</html>

