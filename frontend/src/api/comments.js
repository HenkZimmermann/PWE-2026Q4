import { apiBaseUrl } from "./config";

// Alle Kommentare für gegebene Thread ID aus Backend holen
export async function getThreadComments(threadId) {
    const response = await fetch(apiBaseUrl + "/comments/thread/" + threadId);
    if (!response.ok)
        throw new Error("Kommentare konnten nicht geladen werden.");

    return response.json();
}

// Kommenatr anlegen unter gegebenen Thread
export async function createComment({threadId, message, userId}) {
    const response = await fetch(apiBaseUrl + "/comments/create", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            thread_id: threadId,
            message,
            votes: 0,
            user_id: userId
        })
    });

    if (!response.ok)
        throw new Error("Kommentar konnte nicht gespeichert werden.");
}

export async function editComment(commentId, message) {
    const token = localStorage.getItem("accessToken");
    const response = await fetch(apiBaseUrl + "/comments/" + encodeURIComponent(commentId), {
        method: "PUT",
        headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
        },
        body: JSON.stringify({message}),
    });

    if (!response.ok)
        throw new Error("Änderungen konnten nicht gespeichert werden.");
}

export async function deleteComment(commentId) {
    const token = localStorage.getItem("accessToken");
    const response = await fetch(apiBaseUrl + "/comments/" + encodeURIComponent(commentId), {
        method: "DELETE",
        headers: {Authorization: `Bearer ${token}`},
    });

    if (!response.ok)
        throw new Error("Kommentar konnte nicht gelöscht werden.");

    return response.json();
}
