import { apiBaseUrl } from "./config";

export async function requestRegistration(username,email, password) {
    const response = await fetch(apiBaseUrl + "/users/create", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            username:username,
            email:email,
            password:password
        })
    });
    if (!response.ok)
        throw new Error("Registrierung Fehlgeschlagen");
    return await response.json();
}
