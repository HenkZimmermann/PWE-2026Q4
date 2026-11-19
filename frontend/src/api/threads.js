import { apiBaseUrl } from "./config";

export async function getThreadFeed(limit, signal) {
    const response = await fetch(apiBaseUrl + "/threads/feed?limit=" + limit, {signal});
    if (!response.ok)
        throw new Error("Feed konnte nicht geladen werden.");

    return response.json();
}

export async function createThread({ title, content, groupId, userId }) {
    const response = await fetch(apiBaseUrl + "/threads/create", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            title,
            message: content,
            group_id: groupId,
            user_id: userId,
        }),
    });
    
    if (!response.ok)
        throw new Error("Beitrag konnte nicht gespeichert werden.");
}
