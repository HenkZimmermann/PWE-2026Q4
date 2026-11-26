import { apiBaseUrl } from "./config";

export async function requestLogin(email, password) {
    const response = await fetch(apiBaseUrl + "/users/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            email:email,
            password:password
        })
    });
    const data = await response.json()
    const accessToken = data?.accessToken;
    if (!response.ok)
        throw new Error("Login Credentials Falsch.");
    else return accessToken;
}
export async function requestUserData(accessToken) {
    const response = await fetch(apiBaseUrl + "/users/me",{
        headers:{
            Authorization: `Bearer ${accessToken}`,
        },
    });
    if(!response.ok){
        throw new Error("Benutzer konnte nicht authentifiziert werden!");
    }
    else return await response.json()
    
}
