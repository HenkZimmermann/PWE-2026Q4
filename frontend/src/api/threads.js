import { apiBaseUrl } from "./config";

// Die neusten Threads vom Backend laden, maximal die "limit" neusten Threads
export async function getThreadFeed(limit) {
    const response = await fetch(apiBaseUrl + "/threads/feed?limit=" + limit);
    if (!response.ok)
        throw new Error("Feed konnte nicht geladen werden.");

    return response.json();
}

// Thread mit gegebenen Inhalt erstellen und ans Backend schicken
export async function createThread({title, content, groupId, userId}) {
    const response = await fetch(apiBaseUrl + "/threads/create", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            title,
            message: content,
            group_id: groupId,
            user_id: userId,
        })
    });
    
    if (!response.ok)
        throw new Error("Beitrag konnte nicht gespeichert werden.");
}
