 // Example JSON response

console.log("im running")
 const animalData = [
    {
        "animal_id": 1,
        "name": "Lakshmi",
        "species": "Cow",
        "breed": "Gir",
        "dob": "2020-05-10",
        "gender": "Female",
        "date_added": "2023-01-15",
        "disease_history": "Mastitis",
        "treatement_history": "Antibiotics",
        "status": "Healthy",
        "remark": "Fully recovered"
    },
    {
        "animal_id": 2,
        "name": "Shyam",
        "species": "Goat",
        "breed": "Boer",
        "dob": "2019-11-25",
        "gender": "Male",
        "date_added": "2023-02-20",
        "disease_history": "Foot Rot, Anthrax",
        "treatement_history": "Vaccine, Salve",
        "status": "Under Treatment",
        "remark": "Needs further attention"
    }
];

const getData = async () => {
    console.log("getting data...");
    let responce = await fetch('http://127.0.0.1:5000/data')
    console.log(response);
};

// Function to populate table
const populateTable = (data) => {
    const tableBody = document.getElementById("animalTable").querySelector("tbody");

    data.forEach(record => {
        const row = document.createElement("tr");

        Object.values(record).forEach(value => {
            const cell = document.createElement("td");
            cell.textContent = value;
            row.appendChild(cell);
        });

        tableBody.appendChild(row);
    });
};

// Populate table with the provided data
populateTable(animalData);