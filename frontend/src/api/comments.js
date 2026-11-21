import { apiBaseUrl } from "./config";

// Alle Kommentare für gegebene Thread ID aus Backend holen
export async function getThreadComments(threadId) {
    const response = await fetch(apiBaseUrl + "/comments/thread/" + threadId);
    if (!response.ok)
        throw new Error("Kommentare konnten nicht geladen werden.");

    return response.json();
}
