import { apiBaseUrl } from "./config";

export async function getThreadVote(threadId) {
    const token = localStorage.getItem("accessToken");
    const url = apiBaseUrl + "/threads/" + encodeURIComponent(threadId) + "/vote";
    const response = await fetch(url, {
        headers: {Authorization: `Bearer ${token}`},
    });

    if (!response.ok)
        throw new Error("Stimmen konnten nicht geladen werden.");

    return response.json();
}

export async function setThreadVote(threadId, direction) {
    const token = localStorage.getItem("accessToken");
    const url = apiBaseUrl + "/threads/" + encodeURIComponent(threadId) + "/vote";
    const response = await fetch(url, {
        method: "PUT",
        headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
        },
        body: JSON.stringify({direction}),
    });

    if (!response.ok)
        throw new Error("Stimme konnte nicht gespeichert werden.");

    return response.json();
}
