async function getLocation() {
    const apiURL = 'http://ip-api.com/json/';
    const resp = await fetch(apiURL);
    const response = await resp.json();

    const city = response.city;
    const country = response.country;

    document.getElementById("city").innerHTML = city;
    document.getElementById("country").innerHTML = country;
}

getLocation();
