document.addEventListener("DOMContentLoaded", function () {
    const dataList = document.getElementById("data-list");

    // Charger le fichier JSON automatiquement
    fetch("/static/info.json")
        .then(response => response.json())
        .then(data => {
            // Parcourir les données et les afficher dans une liste
            for (const key in data) {
                if (data.hasOwnProperty(key)) {
                    const person = data[key];
                    const listItem = document.createElement("li");
                    listItem.textContent = `Nom du joueur : ${person.nom} | Meilleur score : ${person.best_score} $`;
                    dataList.appendChild(listItem);
                }
            }
        })
        .catch(error => {
            console.error("Une erreur s'est produite lors de la récupération des données :", error);
        });

    // Rafraîchir la page toutes les 10 secondes en utilisant setInterval
    setInterval(function () {
        location.reload();
    }, 20000);
});
