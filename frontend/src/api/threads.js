import { apiBaseUrl } from "./config";

// Die neusten Threads vom Backend laden, maximal die "limit" neusten Threads
export async function getThreadFeed(limit, groupId = "") {
    let url = apiBaseUrl + "/threads/feed?limit=" + limit;
    if (groupId)
        url += "&group_id=" + groupId;

    const response = await fetch(url);
    if (!response.ok)
        throw new Error("Feed konnte nicht geladen werden.");

    return response.json();
}

// Threads anhand vom Titel durchsuchen
export async function searchThreads(term, groupId, limit) {
    const params = new URLSearchParams({search_term: term, limit});
    if (groupId)
        params.set("group_id", groupId);

    const response = await fetch(apiBaseUrl + "/threads/search?" + params);
    if (!response.ok)
        throw new Error("Suche konnte nicht geladen werden.");

    return response.json();
}

// Thread anhand ID abrufen
export async function getThreadById(threadId) {
    const response = await fetch(apiBaseUrl + "/threads/" + encodeURIComponent(threadId));
    if (response.status === 404)
        return null;
    
    if (!response.ok)
        throw new Error("Beitrag konnte nicht geladen werden.");

    return response.json();
}

// Thread löschen
export async function deleteThread(threadId) {
    const token = localStorage.getItem("accessToken");
    const response = await fetch(apiBaseUrl + "/threads/" + encodeURIComponent(threadId), {
        method: "DELETE",
        headers: {Authorization: `Bearer ${token}`},
    });

    if (!response.ok)
        throw new Error("Beitrag konnte nicht gelöscht werden.");
}

// Thread bearbeiten
export async function editThread(threadId, {title, content}) {
    const token = localStorage.getItem("accessToken");
    const response = await fetch(apiBaseUrl + "/threads/" + encodeURIComponent(threadId), {
        method: "PUT",
        headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
        },
        body: JSON.stringify({title, message: content}),
    });

    if (!response.ok)
        throw new Error("Änderungen konnten nicht gespeichert werden.");
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
