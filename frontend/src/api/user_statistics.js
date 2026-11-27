import { apiBaseUrl } from "./config";

export async function getUserStatistics(userId) {
    const response = await fetch(apiBaseUrl + "/stats/" + userId);
    if (response.status === 404)
        throw new Error("Benutzer konnte nicht geladen werden");
    
    if (!response.ok)
        throw new Error("Fehler beim laden der Statistik." + response.status);
    const data =response.json()
    console.log(data)
    return data;
}
