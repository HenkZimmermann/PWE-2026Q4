import { apiBaseUrl } from "./config";
export async function editUser(userId, username, email, roleId) {
    const accessToken = localStorage.getItem("accessToken");
    const response = await fetch(apiBaseUrl + "/users/" + userId,{
        method: "PUT",
        headers: { "Content-Type": "application/json",
                    Authorization: `Bearer ${accessToken}`,
         },
        body: JSON.stringify({
            username:username,
            email:email,
            role_id: String(roleId)
        })
    });
    if (!response.ok)
        throw new Error("Profil konnte nicht gespeichert werden.");
    else return response.json();
}

export async function deleteUser(userId) {
    const accessToken = localStorage.getItem("accessToken");
    const response = await fetch(apiBaseUrl+"/users/"+userId, {
        method: "DELETE",
        headers: {
            Authorization: `Bearer ${accessToken}`,
        },
    });
    if (!response.ok) {
        throw new Error("Account konnte nicht gelöscht werden (HTTP ${response.status}).");
    }
    return response.json();
}