import { apiBaseUrl } from "./config";

export async function getGroups() {
    const response = await fetch(apiBaseUrl + "/groups/all");
    if (!response.ok)
        throw new Error("Gruppen konnten nicht geladen werden.");
    
    const data = await response.json();
    if (!Array.isArray(data))
        throw new Error("Gruppen konnten nicht geladen werden.");

    return data.map(([id, name]) => ({ id, name }));
}
